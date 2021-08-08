import sys

from environment import WappoEnvironment
from q_learning import q_learning
from visualizer import get_q_animation
from environment import WAPPO_LEVELS


def run_configuration1(level_name, out_filename=None, random_seed=None):
    if level_name not in WAPPO_LEVELS:
        raise NotImplementedError('Unknown Wappo level `{}`; please check and update '
                                  'environment.WAPPO_LEVELS'.format(level_name))
    env = WappoEnvironment(WAPPO_LEVELS[level_name])
    q, _ = q_learning(env, q=None, nr_episodes=1500, nr_episodes_between_eval=150,
                      nr_steps=100, epsilon=0.3, alpha=0.7, gamma=0.95,
                      epsilon_strategy='fixed', alpha_strategy='fixed',
                      random_seed=random_seed)
    if out_filename is None:
        out_filename = '{}.mp4'.format(level_name)
    anim = get_q_animation(q, env, out_filename=out_filename)
    return anim


def run():
    if len(sys.argv) != 2:
        print('Usage: python run_wappo_level.py [level number]')
    run_configuration1(level_name='level_{}'.format(sys.argv[1]))


if __name__ == "__main__":
    # run_configuration1('level_8', 12349)
    # run_configuration1('level_88', 1234232)
    # run_configuration1('level_120', 9452527)
    # run_configuration1('level_142', 3399887)
    run()
