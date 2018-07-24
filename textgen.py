import sys
from textgenrnn import textgenrnn


def main(input_text, generated_output):

    textgen = textgenrnn()
    textgen.train_from_file(input_text, num_epochs=2)
    textgen.generate_to_file(generated_output, temperature=0.5, n=20)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])