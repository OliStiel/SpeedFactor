from collections import defaultdict
from pandas import Series


class CombatEncounter(object):

    def __init__(self, monster_list):
        self.monster_list = monster_list
        self.slain_monsters = list()
        self.round_num = 0

    def start_next_round(self):
        self.round_num += 1

        initiatives = defaultdict(list)
        for monster in self.monster_list:
            monster.roll_initiative()
            initiatives[monster.initiative].append(monster)

        for initiative_roll, monsters in initiatives.items():

            # if we have duplicate initiative rolls in the group
            if len(monsters) > 1:
                # force a reroll of the winners/shit the bed
                pass
            # otherwise we're just gravy

        # return our final sorted initiative order
        sorted_initiatives = sorted(initiatives.items(), key=lambda kv: kv[0], reverse=True)

        print(sorted_initiatives)

    def add_to_combat(self, monster):
        self.monster_list.append(monster)

    def slay_from_combat(self, monster_name):
        for monster in self.monster_list:
            if monster.name == monster_name:
                self.monster_list.remove(monster)
                self.slain_monsters.append(monster)
