#Preprocess image
import argparse
import os
from PIL import Image
import img_plot
import binarize
import numpy as np
import pickle
#todo: creating image object and add all these funcs as methods
#attr = name,size

#Process cli arguments, positional and optional
parser = argparse.ArgumentParser()
parser.add_argument('path', help='directory name', type=str)
parser.add_argument('--ext', help='the extension of image file', action="store_true")
parser.add_argument('--resize', help="resize image")
parser.add_argument('--grey', help="convert to grey scale", action="store_true")
parser.add_argument('--rotate',help="rotate picture counterclockwise", action="store_true")

# class Image: #actually, use OOP here instead of putting it all in find_path()?
#     def __init__(self,path,size):
#         self.path = path
#         self.instance = Image.open(path)
#         self.size = self.instance.size
#######################################################

def find_path(args):
    given_path = args.path
    
    file_list = os.listdir(given_path)
        
    files = [file for file in file_list if os.path.isfile(given_path+'/'+file)
             and file.endswith("jpg")]
    files = [os.path.join(given_path, file) for file in files]
    print(files)
    print(f"Image files in the directory: {given_path}")
    print(*files, sep='\n')

    img_files = [Image.open(img) for img in files]
    return img_files

def convert(img_files,show=True): #might be just show all images in a jupyter notebook if "y" chosen + modify cli to accept arg for "show"
    
    greyed_files = [img_file.convert('L') for img_file in img_files]
    print('succesffully converted to grey scale')
    if show:
        option = input('Wanna show all pictures?')
        if option.lower() == 'y':
            # [pic.show() for pic in greyed_files]
            return greyed_files
        elif int(option)+1:
            # greyed_files[int(option)].show()
            return greyed_files[int(option)]
        else:
            print('none specified')
            return greyed_files
   
    

def resize(img_files,size): #list comprehension doesn't work here?
    print('functionality bug - not fixed yet')
    # img_files[0].resize(size)
    
    resized = [img.resize(size) for img in img_files]
    print('resized\n')
    print(resized)
    return resized
    

def rotate(img_files,angle):
    return [img.rotate(angle) for img in img_files]

def main():
    args = parser.parse_args()
    files = find_path(args)
    
    if args.resize:
        new_size = args.resize
        print('\nResizing to',new_size,'...\n')
        files = resize(files,new_size)
        print('Done')
   
    if args.grey:
        print('\nGreying...')
        grey_files = np.array(convert(files))
        shape = grey_files.shape
        grey_files = grey_files.flatten()
        print('\nDone')

    if args.rotate:
        print('\nRotating...')
        rotate(files)
        print('\nDone')
    
    print('\nThresholding...')
 
    out_binary = binarize.binarize_func(grey_files)
    out_binary = [255 if pix==1 else 0 for pix in out_binary]    
    out_binary = np.array(out_binary,dtype=np.uint8)
    
    out_image = out_binary.reshape(shape)
    with open('binary_arr.pkl', 'wb') as f:
        pickle.dump(out_image, f)
   
    #if want to show img, use the load_unpickle file 

if __name__ == "__main__":
    main()
   
