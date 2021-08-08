import numpy as np
import random
import copy

from environment import WappoEnvironment


class QValues(object):

    def __init__(self, initialization_strategy='normal'):
        '''Initialize with empty lookup table.'''
        self.values = {}
        self.initialization_strategy = initialization_strategy

    def get_value(self, state, action):
        '''Return stored q value for (state, action) pair or a random number if unknown.'''
        if state not in self.values:
            self.values[state] = {}
        if action not in self.values[state]:
            if self.initialization_strategy == 'normal':
                init_val = np.random.normal(loc=0.0, scale=0.1)
                if init_val < -0.5:
                    init_val = -0.5
                elif init_val > 0.5:
                    init_val = 0.5
            elif self.initialization_strategy == 'zero':
                init_val = 0
            else:
                raise NotImplementedError('Unknown initialization_strategy')
            self.values[state][action] = init_val

        return self.values[state][action]

    def set_value(self, state, action, value):
        '''Stored q value for (state, action) pair.'''
        if state not in self.values:
            self.values[state] = {}
        if action not in self.values[state]:
            self.values[state][action] = None
        self.values[state][action] = value

    def max_action(self, state, actions, learning=True):
        '''Return the action with highest q value for given state and action list.'''
        if not learning and state not in self.values:
            return actions[0] if actions else None

        max_value = -np.inf
        max_action = actions[0] if actions else None
        for action in actions:
            if not learning and action not in self.values[state]:
                continue

            value = self.get_value(state, action)
            if value > max_value:
                max_value = value
                max_action = action
            elif value == max_value and learning:
                max_action = random.choice([max_action, action])
        return max_action

    def epsilon_greedy(self, state, actions, epsilon):
        '''Returns max_action or random action with probability of epsilon.'''
        if np.random.rand() < epsilon:
            return random.choice(actions)
        return self.max_action(state, actions)


def evaluate_q_wappo(q, level_dict, max_eval_steps=500):
    env = WappoEnvironment(level_dict)
    env.reset()
    res_path = []

    for _ in range(max_eval_steps):
        state = env.get_state()
        actions = env.get_actions()
        action = q.max_action(state, actions, learning=False)
        if actions is None:
            break  # final state reached
        next_state, _ = env.execute(action)
        res_path.append((state, action))
    # env.draw()
    win_trigger = False
    if env.get_state()[0] == env.goal:
        win_trigger = True
    q_scores = {'win_trigger': win_trigger,
                'steps_number': len(res_path)}
    return q_scores


def q_learning(env, q=None, initialization_strategy='normal',
               nr_episodes=100, nr_steps=20, epsilon=0.1, alpha=0.1, gamma=0.98,
               epsilon_strategy='fixed', epsilon_multiplicator=0.5, epsilon_episodes_steps=10,
               alpha_strategy='fixed', alpha_multiplicator=0.5, alpha_episodes_steps=10,
               alpha_summand=0.1, nr_episodes_between_eval=10, optimization_by_evals=True,
               show_intermediate_evals=True, random_seed=None, debug=False):
    if random_seed is None:
        random_seed = np.random.randint(100, 9999999)
    np.random.seed(random_seed)
    random.seed(random_seed + 5)
    print('random seed value: {}'.format(random_seed))

    if not q:
        q = QValues(initialization_strategy=initialization_strategy)

    level_dict = env.level_dict
    evaluation_report = evaluate_q_wappo(q, level_dict, max_eval_steps=nr_steps)
    if show_intermediate_evals:
        print('Episode 0: win = {}, steps_number = {}'.format(
            evaluation_report['win_trigger'], evaluation_report['steps_number']))
    if optimization_by_evals:
        best_q = copy.deepcopy(q)
        best_evaluation_report = copy.deepcopy(evaluation_report)
        best_episode = 0
    for curr_ep_nr in range(nr_episodes):
        env.reset()
        if debug:
            print('=' * 50)
            print('Spiel #', curr_ep_nr)
            env.draw()

        if epsilon_strategy == 'fixed':
            curr_ep_epsilon = epsilon
        elif epsilon_strategy == 'linear_smaller':
            curr_ep_epsilon = epsilon * (1 - (curr_ep_nr / nr_episodes))
        elif epsilon_strategy == 'episodes_multiplicator':
            steps_power = curr_ep_nr // epsilon_episodes_steps
            curr_ep_epsilon = epsilon * (epsilon_multiplicator ** steps_power)
            if (curr_ep_nr + 1) % epsilon_episodes_steps == 1:
                if show_intermediate_evals:
                    print('Epsilon in episode {}: {:.2f}'.format(
                        (curr_ep_nr + 1), curr_ep_epsilon))
        else:
            raise NotImplementedError('Unknown strategy for epsilon')

        if alpha_strategy == 'fixed':
            curr_ep_alpha = alpha
        elif alpha_strategy == 'episodes_multiplicator':
            steps_power = curr_ep_nr // alpha_episodes_steps
            curr_ep_alpha = alpha * (alpha_multiplicator ** steps_power)
            if (curr_ep_nr + 1) % alpha_episodes_steps == 1:
                if show_intermediate_evals:
                    print('Alpha in episode {}: {:.2f}'.format(
                        (curr_ep_nr + 1), curr_ep_alpha))
        elif alpha_strategy == 'episodes_summand':
            steps_mult = curr_ep_nr // alpha_episodes_steps
            curr_ep_alpha = alpha + (alpha_summand * steps_mult)
            if (curr_ep_nr + 1) % alpha_episodes_steps == 1:
                if show_intermediate_evals:
                    print('Alpha in episode {}: {:.2f}'.format(
                        (curr_ep_nr + 1), curr_ep_alpha))
        else:
            raise NotImplementedError('Unknown strategy for alpha')

        for _ in range(nr_steps):
            # Berechnung Q(S(t), A(t)):
            state = env.get_state()  # S(t)=(Position_self, Position_monster, pentagram_counter)
            actions = env.get_actions()  # alle in S(t) möglichen Aktionen

            action = q.epsilon_greedy(state, actions, curr_ep_epsilon)  # choose A(t) by epsilon-greedy
            q_old = q.get_value(state, action)  # Q(S(t), A(t))

            if debug:
                print('S(t) = ', state)
                print('A(t) = ', action)

            next_state, reward = env.execute(action)  # S(t + 1), R(t)
            if debug:
                print('S(t + 1) = ', next_state)
                print('R(t + 1) = ', reward)
                env.draw()

            if env.get_actions() is None:  # bei terminalem Zustand: Update von Q und Ende!
                if debug:
                    print('>>> S(t + 1) ist einen terminalen Zustand')
                    print('Update:')
                    print('\t q_old: {:.2f}'.format(q.get_value(state, action)))
                q_new = q_old + curr_ep_alpha * (reward + gamma * 0 - q_old)
                q.set_value(state, action, q_new)  # Update von Q(S(t), A(t))
                if debug:
                    print('\t q_new \t = q_old + alpha * (reward + gamma * 0 - q_old)\n'
                          '\t\t = {:.2f} + {} * ({} + {} * 0 - {:.2f})\n'
                          '\t\t = {:.2f}\n'.format(q_old, curr_ep_alpha, reward, gamma, q_old,
                                                   q.get_value(state, action)))
                break

            # Berechnung max_{A} (Q(S(t + 1), A(t + 1))):
            next_action = q.max_action(next_state, env.get_actions())  # choose A(t + 1) by greedy resp. max
            q_next = q.get_value(next_state, next_action)  # max_{A} (Q(S(t + 1), A(t + 1)))
            if debug:
                print('A(t + 1) = ', next_action)
                print('Update:')
                print('\t q_old: {:.2f}'.format(q.get_value(state, action)))

            # Update von Q(S(t), A(t)):
            q_new = q_old + curr_ep_alpha * (reward + gamma * q_next - q_old)
            q.set_value(state, action, q_new)
            if debug:
                print('\t q_new \t = q_old + alpha * (reward + gamma * q_next - q_old)\n'
                      '\t\t = {:.2f} + {} * ({} + {} * {:.2f} - {:.2f})\n'
                      '\t\t = {:.2f}\n'.format(q_old, curr_ep_alpha, reward, gamma, q_next, q_old,
                                               q.get_value(state, action)))
        if (curr_ep_nr + 1) % nr_episodes_between_eval == 0:
            evaluation_report = evaluate_q_wappo(q, level_dict, max_eval_steps=nr_steps)
            if show_intermediate_evals:
                print('Episode {:d}: win = {}, steps_number = {}'.format(
                    (curr_ep_nr + 1), evaluation_report['win_trigger'], evaluation_report['steps_number']))
            if optimization_by_evals:
                if best_evaluation_report['win_trigger'] and not evaluation_report['win_trigger']:
                    continue
                elif best_evaluation_report['win_trigger'] and evaluation_report['win_trigger']:
                    if best_evaluation_report['steps_number'] <= evaluation_report['steps_number']:
                        continue
                best_q = copy.deepcopy(q)
                best_evaluation_report = copy.deepcopy(evaluation_report)
                best_episode = curr_ep_nr
                best_evaluation_report.update({'episode_number': best_episode})

    if optimization_by_evals:
        print('>>> Optimal evaluation (episode {:d}): win = {}, steps_number = {}'.format(
            (best_episode + 1), best_evaluation_report['win_trigger'], best_evaluation_report['steps_number']))
        return best_q, best_evaluation_report
    else:
        evaluation_report = evaluate_q_wappo(q, level_dict, max_eval_steps=nr_steps)
        evaluation_report.update({'episode_number': curr_ep_nr})
        return q, evaluation_report


def test():
    from environment import WAPPO_LEVELS
    env = WappoEnvironment(WAPPO_LEVELS['level_1'])
    q_learning(env, q=None, nr_episodes=3, nr_episodes_between_eval=10,
               optimization_by_evals=False, nr_steps=20,
               epsilon=0.1, alpha=0.1, gamma=0.98,
               random_seed=123451, debug=True)
