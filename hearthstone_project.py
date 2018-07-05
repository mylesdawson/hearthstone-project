import sys
import numpy as np
import pandas as pd



def main():
    filename = sys.argv[1]

    data = pd.read_json(filename, lines=True)
    print(data)




if __name__ == '__main__':
    main()