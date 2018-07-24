## Must have:
 
Python 3.5

## Packages (pip3):

numpy
pandas
requests
textgenrnn
tensorflow

## How To Run

All the necessary data files have been gathered and cleaned. If one wishes to run these steps for some reason they can:

1. Run `python3 gather_data.py` to gather the card json information from a hearthstone API. This will create a file called cards.json.

2. Run `python3 clean_cards.py cards.json cleaned_cards.json`. This will only keep minion type cards, remove unusable cards and filter/clean the card text.

3. Generate new minion cards by using [Max Woolf's RNN Text Generator](https://github.com/minimaxir/textgenrnn): `python3 textgen.py cleaned_cards.json generated_cards.txt`
