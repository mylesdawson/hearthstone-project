## Must have:
 
Python 3.5

## Packages (pip3):

See requirements.txt. Use pip3 to install.

## How To Run

All the necessary data files have been gathered and cleaned. It is recommended to skip the first step as it requires creating an account and generating an API key:

1. To Run `python3 gather_data.py` you must first create an account here: [mashape-hearthstone-api](https://market.mashape.com/omgvamp/hearthstone) and generate an API key. This key can be used as an imput argument to `gather_data.py`. The cards have already been gathered (see cards.json file) and useless ones have been discarded.

2. Run `python3 clean_cards.py cards.json <output_file.txt>`. cards.json is the input and the other file is the output of the cleaned data (in .txt format). card_texts.txt contains the cleaned output.

3. Generate new minion cards by using [Max Woolf's RNN Text Generator](https://github.com/minimaxir/textgenrnn): `python3 textgen.py card_texts.txt`. This will create 3 txt files (after some time) that contain generated cards at different temperatures. Temperatures closer to 1 have more freedom in creating wild output combinations. By default `num_epochs=10`. This will go over the dataset 10 times to enforce the training and increase accuracy of output. num_epochs is set to a large number due to the small size of the cards dataset. To see some results without having to wait long set `num_epochs=1`.

