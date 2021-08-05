import json

from enviroment import Wappo_Environment
from q_learning import q_learning
from visualizer import get_q_animation
from enviroment import Wappo_levels


def save_json(outpath, data):
    with open(outpath, 'w') as f:
        json.dump(data, f)


def load_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data


def train_q_configuration_1(level_name, random_seed=None):
    env = Wappo_Environment(Wappo_levels[level_name])
    q, _ = q_learning(env, q=None, initialization_strategy='normal',
                      nr_episodes=1500, nr_episodes_between_eval=150,
                      nr_steps=100, epsilon=0.3, alpha=0.7, gamma=0.95,
                      epsilon_strategy='fixed', alpha_strategy='fixed',
                      random_seed=random_seed)
    anim = get_q_animation(q, env)
    return anim


def test():
    env = Wappo_Environment(Wappo_levels['level_1'])
    q_test, evaluation_report = q_learning(env, q=None, nr_episodes=3, nr_episodes_between_eval=10,
                                           optimization_by_evals=False, nr_steps=20,
                                           epsilon=0.1, alpha=0.1, gamma=0.98,
                                           random_seed=123451, debug=True)  # debugging


if __name__ == "__main__":
    train_q_configuration_1('level_8', 12349)
    # train_q_configuration_1('level_88', 1234232)
    # train_q_configuration_1('level_120', 9452527)
    # train_q_configuration_1('level_142', 3399887)
