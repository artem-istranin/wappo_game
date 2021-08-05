import matplotlib.pyplot as plt
from matplotlib import animation


def visualize_q_Wappo(q, env, max_steps_animation=500):
    env.reset()
    res_path = []
    env.draw()
    for _ in range(max_steps_animation):
        state = env.get_state()
        actions = env.get_actions()
        action = q.max_action(state, actions, learning=False)
        if actions is None:
            break # final state reached
        next_state, _ = env.execute(action)
        print(state, action, '->', next_state)
        res_path.append((state, action))
        env.draw()

def get_q_animation(q, env, max_steps_animation=500, split_player_monster_moves=True):
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
            break # final state reached
        next_state, _ = env.execute(action)
        res_path.append((state, action))
    res_path.append((next_state, None)) # Append last state

    if split_player_monster_moves:
        splited_res_path = []
        for i in range(len(res_path) * 2):
            (state, action) = res_path[int(i / 2)]
            if i == 0:
                splited_res_path.append((state, action))
            elif i % 2 == 0 and i > 0: # player step
                splited_res_path.append(((state[0], splited_res_path[-1][0][1]), action))
            elif i % 2 == 1 and 0 < i < (len(res_path) * 2 - 1): # monster step
                splited_res_path.append(((splited_res_path[-1][0][0], state[1]), action))
        res_path = splited_res_path

    fig, ax = plt.subplots(figsize=(env.field_size[0], env.field_size[1] - 1))
    env.draw_playground_to_ax(ax)

    monster_scat = ax.scatter(None, None, marker='X', c='red', s=400)
    player_scat = ax.scatter(None, None, marker='d', c='blue', s=200)

    def animate(i):
        position = res_path[i][0][0]
        position_monster = res_path[i][0][1]
        player_scat.set_offsets([position[0], position[1]])
        monster_scat.set_offsets([position_monster[0], position_monster[1]])
        return monster_scat, player_scat,

    anim = animation.FuncAnimation(fig, animate,
                                   frames=len(res_path), interval=500,
                                   blit=True, repeat=False)
    plt.show()
    return anim