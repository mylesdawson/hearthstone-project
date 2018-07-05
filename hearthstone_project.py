import sys
import numpy as np
import pandas as pd


def clean_data(df):
    unused_columns = ['artist', 'cardId', 'cardSet', 'collectible', 'dbfId', 'locale', 'flavor', 'howToGet', 'howToGetGold', 'img', 'imgGold', 'multiClassGroup', 'elite', 'classes', 'faction']
    df = df.drop(unused_columns, axis=1)
    df = df[df['type'] != 'Hero']
    return df

def main():
    # Please use the provided cards.json file as the argument
    filename = sys.argv[1]

    data = pd.read_json(filename, lines=True)

    # We now have 3 types of cards: Weapon, Minion, Spell
    data = clean_data(data)
    print(data)


if __name__ == '__main__':
    main()