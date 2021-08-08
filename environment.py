import matplotlib.pyplot as plt


WAPPO_LEVELS = {
    'level_0': {
        'field_size': [6, 6],
        'start': (3, 2),
        'start_monster': (1, 5),
        'goal': (7, 4),
        'walls': [((1, 5), (1, 6)),
                  ((1, 5), (2, 5)),
                  ((1, 4), (2, 4)),
                  ((1, 3), (2, 3))],
        'pentagrams': []
    },
    'level_1': {
        'field_size': [6, 6],
        'start': (4, 5),
        'start_monster': (6, 5),
        'goal': (4, 0),
        'walls': [((2, 4), (2, 5)),
                  ((4, 5), (4, 6)),
                  ((5, 1), (6, 1)),
                  ((5, 5), (6, 5)),
                  ((6, 5), (6, 6))],
        'pentagrams': [(2, 5)]
    },
    'level_2': {
        'field_size': [6, 6],
        'start': (5, 2),
        'start_monster': (6, 1),
        'goal': (2, 0),
        'walls': [((1, 1), (1, 2)),
                  ((1, 4), (1, 5)),
                  ((2, 1), (2, 2)),
                  ((4, 2), (4, 3)),
                  ((5, 1), (5, 2))],
        'pentagrams': [(3, 5)]
    },
    'level_3': {
        'field_size': [6, 6],
        'start': (6, 1),
        'start_monster': (4, 4),
        'goal': (3, 0),
        'walls': [((1, 1), (2, 1)),
                  ((1, 4), (2, 4)),
                  ((2, 1), (3, 1)),
                  ((3, 3), (3, 4)),
                  ((3, 5), (3, 6)),
                  ((4, 1), (4, 2)),
                  ((4, 2), (4, 3)),
                  ((4, 3), (4, 4)),
                  ((4, 1), (5, 1)),
                  ((4, 5), (5, 5)),
                  ((5, 1), (5, 2)),
                  ((5, 5), (5, 6))],
        'pentagrams': [(4, 2), (6, 3)]
    },
    'level_4': {
        'field_size': [6, 6],
        'start': (1, 2),
        'start_monster': (1, 6),
        'goal': (7, 3),
        'walls': [((1, 2), (1, 3)),
                  ((1, 1), (1, 2)),
                  ((2, 4), (2, 5)),
                  ((2, 4), (3, 4)),
                  ((2, 6), (3, 6)),
                  ((4, 1), (5, 1)),
                  ((5, 4), (5, 5)),
                  ((5, 4), (6, 4)),
                  ((3, 6), (4, 6))],
        'pentagrams': [(3, 2)]
    },
    'level_5': {
        'field_size': [6, 6],
        'start': (2, 6),
        'start_monster': (3, 5),
        'goal': (6, 7),
        'walls': [((1, 4), (1, 5)),
                  ((2, 1), (2, 2)),
                  ((2, 2), (3, 2)),
                  ((2, 3), (3, 3)),
                  ((3, 4), (3, 5)),
                  ((5, 2), (5, 3)),
                  ((5, 4), (5, 5)),
                  ((5, 6), (6, 6)),
                  ((6, 2), (6, 3))],
        'pentagrams': [(1, 5)]
    },
    'level_6': {
        'field_size': [6, 6],
        'start': (4, 2),
        'start_monster': (6, 3),
        'goal': (6, 7),
        'walls': [((1, 3), (2, 3)),
                  ((1, 4), (2, 4)),
                  ((2, 2), (2, 3)),
                  ((2, 4), (2, 5)),
                  ((3, 2), (4, 2)),
                  ((5, 4), (5, 5)),
                  ((5, 4), (6, 4)),
                  ((6, 2), (6, 3)),
                  ((6, 3), (6, 4))],
        'pentagrams': [(2, 1), (6, 2)]
    },
    'level_7': {
        'field_size': [6, 6],
        'start': (6, 3),
        'start_monster': (5, 1),
        'goal': (2, 0),
        'walls': [((1, 1), (2, 1)),
                  ((1, 5), (1, 6)),
                  ((1, 5), (2, 5)),
                  ((2, 5), (2, 6)),
                  ((2, 2), (3, 2)),
                  ((3, 1), (3, 2)),
                  ((4, 3), (4, 4)),
                  ((5, 1), (5, 2)),
                  ((6, 4), (6, 5))],
        'pentagrams': [(3, 5), (5, 6)]
    },
    'level_8': {
        'field_size': [6, 6],
        'start': (4, 1),
        'start_monster': (3, 4),
        'goal': (1, 7),
        'walls': [((1, 4), (2, 4)),
                  ((1, 6), (2, 6)),
                  ((2, 3), (2, 4)),
                  ((2, 3), (3, 3)),
                  ((2, 5), (3, 5)),
                  ((3, 1), (3, 2)),
                  ((3, 4), (4, 4)),
                  ((4, 1), (4, 2)),
                  ((4, 2), (4, 3))],
        'pentagrams': [(6, 2), (5, 5)]
    },
    'level_9': {
        'field_size': [6, 6],
        'start': (5, 2),
        'start_monster': (2, 3),
        'goal': (1, 7),
        'walls': [((1, 2), (1, 3)),
                  ((2, 2), (2, 3)),
                  ((2, 3), (3, 3)),
                  ((4, 1), (4, 2)),
                  ((4, 2), (4, 3)),
                  ((4, 4), (5, 4)),
                  ((5, 1), (6, 1)),
                  ((5, 2), (5, 3))],
        'pentagrams': [(2, 2)]
    },
    'level_10': {
        'field_size': [6, 6],
        'start': (3, 1),
        'start_monster': (2, 5),
        'goal': (0, 3),
        'walls': [((1, 5), (2, 5)),
                  ((2, 4), (2, 5)),
                  ((2, 1), (3, 1)),
                  ((3, 3), (3, 4)),
                  ((4, 4), (4, 5)),
                  ((4, 5), (5, 5)),
                  ((5, 5), (5, 6)),
                  ((6, 1), (6, 2))],
        'pentagrams': [(3, 2)]
    },
    'level_20': {
        'field_size': [6, 6],
        'start': (2, 4),
        'start_monster': (3, 2),
        'goal': (7, 2),
        'walls': [((1, 1), (1, 2)),
                  ((1, 5), (1, 6)),
                  ((3, 2), (4, 2)),
                  ((3, 3), (3, 4)),
                  ((4, 3), (4, 4)),
                  ((6, 1), (6, 2))],
        'pentagrams': [(4, 2), (4, 5)]
    },
    'level_30': {
        'field_size': [6, 6],
        'start': (2, 5),
        'start_monster': (6, 5),
        'goal': (6, 7),
        'walls': [((2, 1), (3, 1)),
                  ((2, 5), (2, 6)),
                  ((2, 5), (3, 5)),
                  ((3, 1), (3, 2)),
                  ((3, 3), (4, 3)),
                  ((4, 4), (4, 5)),
                  ((5, 3), (5, 4)),
                  ((6, 3), (6, 4))],
        'pentagrams': [(5, 2)]
    },
    'level_48': {
        'field_size': [6, 6],
        'start': (4, 5),
        'start_monster': (1, 5),
        'goal': (1, 7),
        'walls': [((1, 3), (1, 4)),
                  ((1, 5), (1, 6)),
                  ((2, 1), (2, 2)),
                  ((2, 2), (3, 2)),
                  ((2, 4), (2, 5)),
                  ((3, 3), (3, 4)),
                  ((3, 5), (4, 5)),
                  ((4, 1), (4, 2)),
                  ((5, 1), (6, 1)),
                  ((5, 4), (5, 5)),
                  ((5, 6), (6, 6)),
                  ((6, 4), (6, 5))],
        'pentagrams': [(4, 1), (6, 3)]
    },
    'level_51': {
        'field_size': [6, 6],
        'start': (1, 5),
        'start_monster': (5, 3),
        'goal': (0, 3),
        'walls': [((1, 1), (1, 2)),
                  ((1, 3), (1, 4)),
                  ((2, 1), (3, 1)),
                  ((2, 5), (2, 6)),
                  ((4, 2), (5, 2)),
                  ((4, 4), (4, 5)),
                  ((4, 4), (5, 4)),
                  ((5, 2), (5, 3)),
                  ((5, 2), (6, 2)),
                  ((5, 6), (6, 6))],
        'pentagrams': [(4, 5), (6, 2)]
    },
    'level_60': {
        'field_size': [6, 6],
        'start': (6, 1),
        'start_monster': (1, 5),
        'goal': (0, 5),
        'walls': [((1, 4), (1, 5)),
                  ((1, 4), (2, 4)),
                  ((1, 5), (2, 5)),
                  ((2, 1), (2, 2)),
                  ((3, 1), (3, 2)),
                  ((3, 2), (3, 3)),
                  ((3, 3), (4, 3)),
                  ((4, 1), (4, 2)),
                  ((4, 4), (5, 4)),
                  ((4, 2), (5, 2)),
                  ((5, 2), (5, 3)),
                  ((5, 2), (6, 2)),
                  ((5, 3), (5, 4)),
                  ((6, 1), (6, 2))],
        'pentagrams': []
    },
    'level_70': {
        'field_size': [6, 6],
        'start': (6, 5),
        'start_monster': (2, 3),
        'goal': (2, 7),
        'walls': [((1, 2), (1, 3)),
                  ((2, 1), (2, 2)),
                  ((2, 2), (2, 3)),
                  ((2, 2), (3, 2)),
                  ((3, 2), (3, 3)),
                  ((3, 3), (4, 3)),
                  ((2, 5), (3, 5)),
                  ((3, 6), (4, 6)),
                  ((5, 1), (5, 2)),
                  ((5, 3), (5, 4))],
        'pentagrams': [(5, 5), (6, 3)]
    },
    'level_88': {
        'field_size': [6, 6],
        'start': (2, 1),
        'start_monster': (2, 5),
        'goal': (7, 2),
        'walls': [((1, 2), (2, 2)),
                  ((1, 3), (2, 3)),
                  ((2, 2), (2, 3)),
                  ((2, 4), (3, 4)),
                  ((3, 1), (3, 2)),
                  ((3, 3), (3, 4)),
                  ((3, 4), (4, 4)),
                  ((4, 2), (5, 2)),
                  ((4, 3), (4, 4)),
                  ((4, 4), (4, 5)),
                  ((4, 4), (5, 4)),
                  ((5, 1), (5, 2)),
                  ((6, 1), (6, 2)),
                  ((6, 4), (6, 5))],
        'pentagrams': [(2, 4), (3, 1)]
    },
    'level_92': {
        'field_size': [6, 6],
        'start': (1, 3),
        'start_monster': (6, 4),
        'goal': (6, 0),
        'walls': [((1, 2), (2, 2)),
                  ((2, 1), (2, 2)),
                  ((2, 2), (2, 3)),
                  ((4, 1), (4, 2)),
                  ((4, 2), (5, 2)),
                  ((4, 4), (4, 5)),
                  ((6, 3), (6, 4))],
        'pentagrams': [(1, 5), (5, 1)]
    },
    'level_101': {
        'field_size': [6, 6],
        'start': (6, 4),
        'start_monster': (4, 6),
        'goal': (1, 0),
        'walls': [((1, 4), (2, 4)),
                  ((1, 5), (2, 5)),
                  ((2, 1), (3, 1)),
                  ((2, 6), (3, 6)),
                  ((3, 1), (3, 2)),
                  ((3, 2), (4, 2)),
                  ((3, 4), (3, 5)),
                  ((4, 1), (5, 1)),
                  ((4, 5), (4, 6)),
                  ((5, 3), (5, 4)),
                  ((5, 6), (6, 6)),
                  ((6, 2), (6, 3)),
                  ((6, 5), (6, 6))],
        'pentagrams': [(2, 4), (6, 2)]
    },
    'level_110': {
        'field_size': [6, 6],
        'start': (4, 6),
        'start_monster': (4, 1),
        'goal': (2, 7),
        'walls': [((1, 4), (1, 5)),
                  ((3, 1), (3, 2)),
                  ((3, 6), (4, 6)),
                  ((4, 2), (5, 2)),
                  ((4, 3), (5, 3)),
                  ((4, 4), (4, 5)),
                  ((5, 1), (5, 2))],
        'pentagrams': [(4, 5)]
    },
    'level_120': {
        'field_size': [6, 6],
        'start': (1, 5),
        'start_monster': (1, 3),
        'goal': (1, 0),
        'walls': [((1, 4), (2, 4)),
                  ((2, 1), (3, 1)),
                  ((3, 1), (3, 2)),
                  ((4, 1), (4, 2)),
                  ((4, 2), (4, 3)),
                  ((4, 3), (4, 4)),
                  ((4, 5), (4, 6)),
                  ((4, 2), (5, 2)),
                  ((4, 4), (5, 4)),
                  ((5, 5), (6, 5)),
                  ((6, 1), (6, 2)),
                  ((6, 2), (6, 3)),
                  ((6, 3), (6, 4))],
        'pentagrams': [(2, 5)]
    },
    'level_130': {
        'field_size': [6, 6],
        'start': (1, 2),
        'start_monster': (3, 1),
        'goal': (6, 4),
        'walls': [((1, 2), (2, 2)),
                  ((1, 4), (2, 4)),
                  ((2, 2), (2, 3)),
                  ((2, 4), (3, 4)),
                  ((2, 5), (3, 5)),
                  ((3, 3), (4, 3)),
                  ((4, 4), (3, 4)),
                  ((4, 6), (3, 6)),
                  ((4, 5), (4, 6))],
        'pentagrams': [(2, 5), (4, 5)]
    },
    'level_142': {
        'field_size': [6, 6],
        'start': (2, 2),
        'start_monster': (4, 2),
        'goal': (6, 6),
        'walls': [((1, 4), (2, 4)),
                  ((2, 2), (3, 2)),
                  ((2, 3), (3, 3)),
                  ((3, 2), (3, 3)),
                  ((3, 3), (3, 4)),
                  ((4, 5), (5, 5)),
                  ((5, 2), (5, 3)),
                  ((5, 4), (6, 4)),
                  ((5, 5), (5, 6)),
                  ((5, 6), (6, 6))],
        'pentagrams': [(4, 4)]
    },
    'level_148': {
        'field_size': [6, 6],
        'start': (3, 6),
        'start_monster': (1, 5),
        'goal': (4, 4),
        'walls': [((2, 3), (2, 4)),
                  ((4, 1), (4, 2)),
                  ((4, 2), (4, 3)),
                  ((4, 2), (5, 2)),
                  ((4, 4), (5, 4)),
                  ((4, 5), (4, 6))],
        'pentagrams': [(4, 5), (5, 3)]
    }
}


class WappoEnvironment(object):

    def __init__(self, level_dict):
        self.level_dict = level_dict
        self.field_size = level_dict['field_size']
        self.start = level_dict['start']
        self.start_monster = level_dict['start_monster']
        self.goal = level_dict['goal']
        self.position = self.start
        self.position_monster = self.start_monster
        self.move = {'left': (-1, 0),
                     'right': (1, 0),
                     'up': (0, 1),
                     'down': (0, -1)}
        self.walls = level_dict['walls']
        self.append_field_boundaries()
        self.pentagrams = level_dict['pentagrams']  # list of pentagrams
        self.pentagram_counter = 0  # counter, damit Monster über 3 Runden stehen bleibt
        self.monster_pentagram_frozen_steps = 0  # Schritte, die Monster in einem Pentagramm steht
        self.rewads_dict = {
            'home_reward': 1.00,
            'died_reward': -1.00,
            'step_cost': -0.04,
            'pentagram_reward': 0
        }

    def reset(self):
        self.position = self.start
        self.position_monster = self.start_monster
        self.pentagram_counter = 0

    def get_state(self):
        return self.position, self.position_monster, self.pentagram_counter

    def append_field_boundaries(self):
        for x in range(1, self.field_size[0] + 1):
            for y in [0, self.field_size[1]]:
                # zwischen goal und field keine wall:
                if self.goal not in [(x, y), (x, y + 1)]:
                    self.walls.append(((x, y), (x, y + 1)))  # horizontale Spielfeldbegrenzung
        for y in range(1, self.field_size[1] + 1):
            for x in [0, self.field_size[0]]:
                if self.goal not in [(x, y), (x + 1, y)]:
                    self.walls.append(((x, y), (x + 1, y)))  # vertikale Spielfeldbegrenzung

    def get_actions(self, get_actions_monster=False):
        if not get_actions_monster:
            ref_position = self.position
            # Terminale Zustaende, keine weitere Aktionen:
            if ref_position == self.goal:
                return None
            if ref_position == self.position_monster:
                return None
            if ref_position in self.pentagrams:
                return None
        else:
            ref_position = self.position_monster
        actions = []
        shit_action = None
        for action, coordinate_change in self.move.items():
            state_move = (ref_position,
                          (ref_position[0] + coordinate_change[0], ref_position[1] + coordinate_change[1]))
            # Aktion auf Monster zu:
            if not get_actions_monster and state_move[1] == self.position_monster:
                shit_action = action
                continue
            # Aktion auf Pentagramm:
            if not get_actions_monster and (state_move[1] in self.pentagrams):
                shit_action = action
                continue
            # Aktion gegen eine Wand:
            if (state_move in self.walls) or (state_move[::-1] in self.walls):
                continue
            actions.append(action)
        # Wenn nur Aktion auf Monster oder Pentagramm übrig bleibt:
        if len(actions) == 0:
            return [shit_action]
        else:
            return actions

    def monster_move(self):
        # Monster macht zwei Schritte:
        for i in range(2):
            # Überprüfung, ob Monster bereits eingeholt hat:
            if self.position_monster == self.position:
                break
            # Überprüfung, ob Monster auf Pentagramm steht:
            if self.position_monster in self.pentagrams and self.monster_pentagram_frozen_steps < 3:
                self.pentagram_counter += 1
                if self.pentagram_counter < 5:  # in 1. Runde kommt Monster rauf und soll über 3 Runden stehen bleiben
                    self.monster_pentagram_frozen_steps += 1
                    break
            else:
                self.pentagram_counter = 0
            actions_monster = self.get_actions(get_actions_monster=True)  # Monsteraktionen
            old_position_monster = self.position_monster
            # 1.Versuch: horizontale Annäherung:
            if (self.position_monster[0] - self.position[0]) < 0 and 'right' in actions_monster:
                self.position_monster = (self.position_monster[0] + 1, self.position_monster[1])
            elif (self.position_monster[0] - self.position[0]) > 0 and 'left' in actions_monster:
                self.position_monster = (self.position_monster[0] - 1, self.position_monster[1])
            else:  # 2.Versuch: vertikale Annäherung:
                if (self.position_monster[1] - self.position[1]) > 0 and 'down' in actions_monster:
                    self.position_monster = (self.position_monster[0], self.position_monster[1] - 1)
                elif (self.position_monster[1] - self.position[1]) < 0 and 'up' in actions_monster:
                    self.position_monster = (self.position_monster[0], self.position_monster[1] + 1)
                    # Sobald Monster von Pentagramm runter:
            if old_position_monster != self.position_monster:
                self.monster_pentagram_frozen_steps = 0
            # Wenn Monster mit 2.ter Aktion auf Pentagramm kommt:
            if self.position_monster in self.pentagrams and self.monster_pentagram_frozen_steps < 3:
                self.pentagram_counter += 1
                break

    def reward(self):
        if self.position in self.pentagrams:
            return self.rewads_dict['died_reward']
        if self.position == self.goal:
            return self.rewads_dict['home_reward']
        if self.position == self.position_monster:
            return self.rewads_dict['died_reward']
        if self.pentagram_counter == 1:
            return self.rewads_dict['pentagram_reward']
        return self.rewads_dict['step_cost']

    def execute(self, action):
        coordinate_change = self.move[action]
        self.position = (self.position[0] + coordinate_change[0], self.position[1] + coordinate_change[1])
        self.monster_move()
        return self.get_state(), self.reward()

    def __str__(self):
        return 'Player position: {}; Monster position: {}'.format(
            self.position, self.position_monster)

    def draw_playground_to_ax(self, ax):
        ax.set_xticks([x for x in range(0, self.field_size[0] + 2)])
        ax.set_xticklabels([str(i) for i in range(0, self.field_size[0] + 2)], ha='center')
        ax.set_xlim(-0.5, self.field_size[0] + 1.5)
        for x in range(0, self.field_size[0] + 2):
            ax.axvline(x + 0.5, linestyle='-', color='grey', linewidth=0.5)

        ax.set_yticks([y for y in range(0, self.field_size[1] + 2)])
        ax.set_yticklabels([str(i) for i in range(0, self.field_size[1] + 2)], ha='center')
        ax.set_ylim(-0.5, self.field_size[1] + 1.5)
        for y in range(0, self.field_size[1] + 2):
            ax.axhline(y + 0.5, linestyle='-', color='grey', linewidth=0.5)

        for wall in self.walls:
            if wall[0][1] == wall[1][1]:
                ax.plot([(wall[0][0] + wall[1][0]) / 2] * 2, [wall[0][1] - 0.5, wall[0][1] + 0.5],
                        linewidth=5, color='black')
            elif wall[0][0] == wall[1][0]:
                ax.plot([wall[0][0] - 0.5, wall[0][0] + 0.5], [(wall[0][1] + wall[1][1]) / 2] * 2,
                        linewidth=5, color='black')
        for pentagram in self.pentagrams:
            ax.scatter(pentagram[0], pentagram[1],
                       marker='*', c='orange', s=800)
            ax.scatter(pentagram[0], pentagram[1],
                       s=800, facecolors='none', edgecolors='orange')
        # draw house:
        ax.scatter(self.goal[0], self.goal[1] - 0.2,
                   marker='s', c='green', s=150)
        ax.scatter(self.goal[0], self.goal[1] + 0.2,
                   marker=6, c='green', s=350)
        ax.scatter(self.goal[0] + 0.10, self.goal[1] - 0.05,
                   marker='|', c='green', s=500)

    def draw(self):
        fig, ax = plt.subplots(figsize=(self.field_size[0], self.field_size[1] - 1))
        self.draw_playground_to_ax(ax)
        # draw monster:
        ax.scatter(self.position_monster[0], self.position_monster[1],
                   marker='X', c='red', s=400)
        # draw player:
        ax.scatter(self.position[0], self.position[1],
                   marker='d', c='blue', s=200)
        fig.tight_layout()
        plt.show()
