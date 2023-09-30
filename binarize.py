#todo: add func to compute geometric properties - area, position, center of mass integrals, segmentation
import numpy as np

def binarize_func(img): 
    imhist, bin_edges = np.histogram(img,256)
    print('\nTotal pixels:',len(img))
    print('\nSum imhist:',sum(imhist))
    print('\nbins range is:',len(bin_edges))

    #Compute mean value to threshold
    bins = [1/2*(bin_edges[i]+bin_edges[i+1]) for i in range(len(bin_edges)-1)]
    hist_pairs = zip(bins,imhist)
    weighted = 0
    for value,num in hist_pairs:
        weighted += value*num/len(img)    
    threshold = weighted
    binary_img = [1 if pixel >= threshold else 0 for pixel in img] 
    return binary_img
    

