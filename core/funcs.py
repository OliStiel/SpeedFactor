import pandas as pd


def csv_to_monster_list(filepath):
    file_contents = pd.read_csv(filepath_or_buffer=filepath, engine='python')

    return file_contents


def cleanse_list(monster_frame):
    monster_frame['monster_size'].apply(lambda x: x.lower())


test = csv_to_monster_list('C:/data/speedfactor')
print(test)