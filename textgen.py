import sys
from textgenrnn import textgenrnn


def main(input_text):

    textgen = textgenrnn()
    textgen.train_from_file(input_text, num_epochs=5)
    textgen.generate()


if __name__ == "__main__":
    main(sys.argv[1])