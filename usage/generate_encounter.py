from SpeedFactor.core import funcs, monster

monster_group = funcs.csv_to_monster_list('C:/data/speedfactor/monster_list.csv')

monster_list = list()

for i, row in monster_group.iterrows():
    monster_list.append(monster.Monster(name=row['monster_name'],
                                        dexterity_mod=row['dexterity_mod'],
                                        size=row['monster_size']))

combatRound = monster.RoundOfCombat(monster_list)

combatRound.start_next_round()