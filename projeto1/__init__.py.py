
# coding: utf-8

# In[13]:





# In[53]:





import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import os
from astropy.io import fits
from astropy.utils.data import download_file
from matplotlib.colors import LogNorm

x = './trab/desktop/xo2b'

def bias(y):
    a = glob.glob(x+"/bias/*.fits")
    masterbias = []
    for i in range(len(a)):
        img = fits.getdata(a[i])
        img = img.astype(np.float64)
        masterbias.append(img)
    if y == 1:
        return np.median(masterbias,axis=0)
    else:
        outfile = x + '/master_bias.fits'
        hdu = fits.PrimaryHDU() #criando o HDU 
        hdu.data = np.median(masterbias,axis=0)
        hdu.writeto(outfile)


# In[54]:


bias(1)


# In[55]:


def flat(d):
    b = glob.glob(x+"/flat/*.fits")
    masterflat = []
    masterflatbias = []
    for i in range(len(b)):
        img = fits.getdata(b[i])
        img = img.astype(np.float64)
        masterflat.append(img)
        masterflatbias.append((masterflat[i] - bias(1))/np.median(masterflat[i]))
    if d == 1:
        return np.median(masterflatbias,axis=0)
    else:
        outfile = x + '/master_flat_bias.fits'
        hdu = fits.PrimaryHDU() #criando o HDU 
        hdu.data = np.median(masterflatbias,axis=0)
        hdu.writeto(outfile)


# In[56]:


flat(1)


# In[59]:


def science():
    c = glob.glob(x+'/science/*.fits')
    for i in range(len(c)):
        img = fits.getdata(c[i])
        img = img.astype(np.float64)
        sci_clean = (img-bias(1))/flat(1)
        outfile = c[i][:-5] + "_clean.fits"
        hdu = fits.PrimaryHDU()
        hdu.data = sci_clean
        hdu.writeto(outfile)
        
        


# In[50]:





# In[51]:




