import sys
import numpy as np
import pandas as pd
import re


def clean_data(df):
    df = df[df['type'] == 'Minion']
    unused_columns = ['artist', 'cardId', 'cardSet', 'collectible', 'dbfId', 'locale', 'flavor', 'howToGet', 'howToGetGold', 'img', 'imgGold', 'multiClassGroup', 'elite', 'classes', 'faction', 'armor', 'durability', 'mechanics', 'type', 'playerClass', 'race', 'rarity']
    df = df.drop(unused_columns, axis=1)
    df['text'] = df['text'].astype(str)
    return df

def filter_text(x):
    remove_tags = re.compile(r'<.*?>')
    x = remove_tags.sub('', x)
    x = x.strip()
    x = x.replace('\\n', ' ')
    x = x.replace('nan', '')
    return x

def main(filename, card_text_file):
    # Please use the provided cards.json file as the argument
    data = pd.read_json(filename, lines=True)

    data = clean_data(data)
    data['text'] = data['text'].apply(filter_text)

    data.to_csv(card_text_file, header=None, index=None, sep=' ', float_format='%.f')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])