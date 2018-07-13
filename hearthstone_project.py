import sys
import numpy as np
import pandas as pd
import re


def clean_data(df):
    unused_columns = ['artist', 'cardId', 'cardSet', 'collectible', 'dbfId', 'locale', 'flavor', 'howToGet', 'howToGetGold', 'img', 'imgGold', 'multiClassGroup', 'elite', 'classes', 'faction']
    df = df.drop(unused_columns, axis=1)
    df = df[df['type'] == 'Minion']
    df['text'] = df['text'].astype(str)
    return df

def transform_mechanics(x):
    flat = []
    if str(x) == 'nan':
        return flat
    for item in x:
        for key in item:
            flat.append(item[key])
    return flat

def filter_text(x):
    # Removes html tags </> from card text and square brackets []
    remove_x = re.compile(r'\[x\]')
    remove_brackets = re.compile(r'<.*?>')
    x = remove_x.sub('', x)
    x = remove_brackets.sub('', x)
    x = x.strip()
    x = x.replace('\\n', ' ')
    return x

def main(filename):
    # Please use the provided cards.json file as the argument
    data = pd.read_json(filename, lines=True)

    # We now only have one type of card: Minion
    data = clean_data(data)
    # Transform mechanics to 1-d array of strings
    data['mechanics'] = data['mechanics'].apply(transform_mechanics)
    # Filter out unneeded text 
    data['text'] = data['text'].apply(filter_text)

    # We may not need mechanics (remove?)
    # Try creating normal distribution and sampling from it to create new cards
    # Try using simple reccurence neural network to generate cards


    print(data)


if __name__ == '__main__':
    main(sys.argv[1])