import sys
from textgenrnn import textgenrnn


def main(input_text):

    textgen = textgenrnn(name="new_model")
    textgen.train_from_file(input_text, num_epochs=10, rnn_bidirectional=True)
    textgen.generate_to_file('generated_output-0.5.txt', temperature=0.2, n=20)
    textgen.generate_to_file('generated_output-0.2.txt', temperature=0.5, n=20)
    textgen.generate_to_file('generated_output-1.txt', temperature=1, n=20)



if __name__ == "__main__":
    main(sys.argv[1])