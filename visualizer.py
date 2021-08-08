import os
import matplotlib.pyplot as plt
from matplotlib import animation


def visualize_q_wappo(q, env, max_steps_animation=500):
    env.reset()
    res_path = []
    env.draw()
    for _ in range(max_steps_animation):
        state = env.get_state()
        actions = env.get_actions()
        action = q.max_action(state, actions, learning=False)
        if actions is None:
            break  # final state reached
        next_state, _ = env.execute(action)
        print(state, action, '->', next_state)
        res_path.append((state, action))
        env.draw()


def get_q_animation(q, env, max_steps_animation=500, split_player_monster_moves=True,
                    out_filename=None, show=False):
    '''
        anim = get_q_animation(q, env)
        anim
    '''
    env.reset()
    res_path = []
    for _ in range(max_steps_animation):
        state = env.get_state()
        actions = env.get_actions()
        action = q.max_action(state, actions, learning=False)
        if actions is None:
            break  # final state reached
        next_state, _ = env.execute(action)
        res_path.append((state, action))
    res_path.append((next_state, None))  # append last state

    if split_player_monster_moves:
        splitted_res_path = []
        for i in range(len(res_path) * 2):
            (state, action) = res_path[int(i / 2)]
            if i == 0:
                splitted_res_path.append((state, action))
            elif i % 2 == 0 and i > 0:  # player step
                splitted_res_path.append(((state[0], splitted_res_path[-1][0][1]), action))
            elif i % 2 == 1 and 0 < i < (len(res_path) * 2 - 1):  # monster step
                splitted_res_path.append(((splitted_res_path[-1][0][0], state[1]), action))
        res_path = splitted_res_path

    fig, ax = plt.subplots(figsize=(env.field_size[0], env.field_size[1] - 1))
    env.draw_playground_to_ax(ax)

    monster_scat = ax.scatter(None, None, marker='X', c='red', s=400)
    player_scat = ax.scatter(None, None, marker='d', c='blue', s=200)

    def animate(step_index):
        position = res_path[step_index][0][0]
        position_monster = res_path[step_index][0][1]
        player_scat.set_offsets([position[0], position[1]])
        monster_scat.set_offsets([position_monster[0], position_monster[1]])
        return monster_scat, player_scat,

    anim = animation.FuncAnimation(fig, animate,
                                   frames=len(res_path), interval=500,
                                   blit=True, repeat=False)
    if out_filename is not None:
        if os.path.splitext(out_filename)[-1] != '.mp4':
            raise ValueError('Video filename must have .mp4 extension')
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=3, metadata=dict(artist='Me'), bitrate=1800)
        anim.save(out_filename, writer=writer)
        print('Level animation is saved as {}'.format(out_filename))
    if show:
        plt.show()
    return anim
