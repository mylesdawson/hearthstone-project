## Must have:
 
Python 3.5

## Packages (pip3):

See requirements.txt. Use pip3 to install.

## How To Run

All the necessary data files have been gathered and cleaned. The first step below should be skipped because this step requires creating an account and generating an API key.

1. To Run `python3 gather_data.py` you must first create an account here: [mashape-hearthstone-api](https://market.mashape.com/omgvamp/hearthstone) and generate an API key. This key can be used as an input argument to `gather_data.py`. The cards have already been gathered (see cards.json file) and useless ones have been discarded.

2. Run `python3 clean_cards.py cards.json <output_file.txt>`. cards.json is the input and card_texts.txt is the output of the cleaned data.

3. Generate new minion cards by using [Max Woolf's RNN Text Generator](https://github.com/minimaxir/textgenrnn): `python3 textgen.py card_texts.txt`. Using the generator will create 3 .txt files (after some time) that contain generated cards at different temperatures. Temperatures closer to 1 have freedom in creating wild output combinations. To see results without having to wait, set `num_epochs=1` or view the provided generated_output.txt files. Running the generator will also create a model_weights.hdf5 file. This file is used to reuse the model without retraining (see step 4).

4. Reuse model by running `python3 textgen_from_weights.py new_model_weights.hdf5 <n_samples> <temperature>`. Performing this step will quickly generate n samples at specified temperature. Going above temperature 1 is not recommended.
