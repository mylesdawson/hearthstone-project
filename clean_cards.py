import sys
import numpy as np
import pandas as pd
import re


def clean_data(df):
    unused_columns = ['artist', 'cardId', 'cardSet', 'collectible', 'dbfId', 'locale', 'flavor', 'howToGet', 'howToGetGold', 'img', 'imgGold', 'multiClassGroup', 'elite', 'classes', 'faction', 'armor', 'durability', 'mechanics']
    df = df.drop(unused_columns, axis=1)
    df['text'] = df['text'].astype(str)
    return df

def filter_text(x):
    remove_tags = re.compile(r'<.*?>')
    x = remove_tags.sub('', x)
    x = x.strip()
    x = x.replace('\\n', ' ')
    return x

def main(filename, card_text_file, card_name_file, card_rest_file):
    # Please use the provided cards.json file as the argument
    data = pd.read_json(filename, lines=True)

    data = clean_data(data)
    data['text'] = data['text'].apply(filter_text)

    data['text'].to_csv(card_text_file, header=None, index=None, sep=' ', mode='a')
    data['name'].to_csv(card_name_file, header=None, index=None, sep=' ', mode='a')
    data[['attack', 'cost', 'health', 'playerClass', 'race', 'rarity']].to_csv(card_rest_file, header=None, index=None, sep=' ', mode='a')


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])