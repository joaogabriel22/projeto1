
# coding: utf-8

# In[28]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os
from astropy.io import fits
from astropy.utils.data import download_file
from matplotlib.colors import LogNorm

def bias(y):
    x = '/home2/joao15/tda_joao15/xo2b/bias/'
    a = glob.glob(x+"*.fits")
    masterbias = []
    for i in range(len(a)):
        img = fits.getdata(a[i])
        img = img.astype(np.float64)
        masterbias.append(img)
    if y == 1:
        return np.median(masterbias,axis=0)
    else:
        outfile = '/home2/joao15/tda_joao15/xo2b/bias/master_bias.fits'
        hdu = fits.PrimaryHDU() #criando o HDU 
        hdu.data = np.median(masterbias,axis=0)
        hdu.writeto(outfile)


# In[29]:


bias(0)


# In[39]:


def flat(y):
    x = '/home2/joao15/tda_joao15/xo2b/flat/'
    a = glob.glob(x+"*.fits")
    masterflat = []
    masterflatbias = []
    for i in range(len(a)):
        img = fits.getdata(a[i])
        img = img.astype(np.float64)
        masterflat.append(img)
        masterflatbias.append((masterflat[i] - bias(1)/np.median(masterflat))
        mastercu.append(masterflatbias[i]/np.median(masterflatbias[i]))
    if y == 1:
        return np.median(masterflatbias,axis=0)
    else:
        outfile = '/home2/joao15/tda_joao15/xo2b/flat/master_flat_bias.fits'
        hdu = fits.PrimaryHDU() #criando o HDU 
        hdu.data = np.median(masterflatbias,axis=0)
        hdu.writeto(outfile)


# In[38]:


flat(0)

