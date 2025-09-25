# print('hello world!')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal
from ecg_signal import *
# print("All imports successful!")

def main():
    '''
    This function, when called, prints "Hello, world!"

    Arguments: None
    '''
    print("Hello, world!")

if __name__ == "__main__":
    # main()
    # ecg = [1,2,3,4,5]
    # print(return_stats(ecg))

    ecg = ECGSignal([1,2,3,4,5])
    print(ecg.length())
    ecg.summary()
