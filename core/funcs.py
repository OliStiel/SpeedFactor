import pandas as pd

def csv_to_monster_list(file_path):
    file_contents = pd.read_csv(filepath_or_buffer=file_path, engine='python')

    return file_contents


def cleanse_list(monster_frame):
    for column in monster_frame:
        monster_frame[column] = monster_frame[column].apply(lambda x: x.lower() if isinstance(x, str) else x)

    return monster_frame

test = csv_to_monster_list('C:/data/speedfactor/monster_list.csv')
print(test.columns)
test = cleanse_list(test)
print(test)