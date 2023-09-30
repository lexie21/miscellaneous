import numpy as np
from PIL import Image as im
import pickle

# Load the array with Pickle
with open('binary_arr.pkl', 'rb') as f:
    loaded_array = pickle.load(f)

def main():
    data = im.fromarray(loaded_array)
    data.save('dummy_pic.png')
  
if __name__ == "__main__":
  main()
