import sys
from textgenrnn import textgenrnn


def main(model_weights, number_to_generate, temperature):

    try:
        number_to_generate = int(number_to_generate)
        temperature = float(temperature)
    except:
        exit()

    textgen = textgenrnn(model_weights)
    print('Temperature = {0}\n'.format(temperature))
    textgen.generate(number_to_generate, temperature=temperature)
    print('Temperature = 0.5\n')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])