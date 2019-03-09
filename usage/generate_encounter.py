from SpeedFactor.core import funcs, monster, combat_structure

monster_group = funcs.csv_to_monster_list('C:/data/speedfactor/monster_list.csv')

monster_list = list()

for i, row in monster_group.iterrows():
    monster_list.append(monster.Monster(name=row['monster_name'] + str(i),
                                        dexterity_mod=row['dexterity_mod'],
                                        size=row['monster_size']))

encounter = combat_structure.CombatEncounter(monster_list)

encounter.start_next_round()
#encounter.slay_from_combat('guardsman0')
