
# coding: utf-8

# In[30]:


#importando os pacotes nescessarios
import numpy as np
import glob
from astropy.io import fits
# definindo o endereco x onde se encontram sua pasta, no caso xo2b, em que dentro dela havera as pastas bias,science e flat
x = './trab/desktop/xo2b'
# funcao bias que retorna o masterbias dos bias da pasta
def bias(y):
    '''
    This function recives a y variable that if == 1, it creates a fits file at the x adress. The fits is a masterbias of the paste bias.
    If y is diferent from 1, it returns only an array of the masterbias.
    '''
    #criando uma lista em que cada elemento fica como uma string do endereco de cada bias
    a = glob.glob(x+"/bias/*.fits")
    masterbias = []
    # laco for que ira jogar dentro da lista vazia masterbias os arrays de cada bias
    for i in range(len(a)):
        # usando o fits.getdata para retirar uma array de cada imagem bias
        img = fits.getdata(a[i])
        # transformando os elementos da array em float64
        img = img.astype(np.float64)
        # jogando essa array dentro da lista masterbias
        masterbias.append(img)
    # teste estatistico que mostra se o masterbias esta com uma media razoavel, menor que 20, ou nao.
    if np.mean(np.median(masterbias,axis=0)) > 20:
        return "Error: The masterbias mean is too higher(the mean is higher then 20)"
    # verificando a variavel y para retornar uma array da mediana da lista masterbias, caso y == 1 
    if y == 1:
        return np.median(masterbias,axis=0)
    # caso contrario, ele cria uma imagem fits masterbias no endereco x definido anteriormente
    else:
        outfile = x + '/master_bias.fits'
        hdu = fits.PrimaryHDU() #criando o HDU 
        hdu.data = np.median(masterbias,axis=0)
        hdu.writeto(outfile)


# In[31]:


# funcao flat que retorna o masterflat dos flats da pasta flat, ja reduzindo do masterbias
def flat(d):
    '''
    This function recives a d variable that if == 1, it creates a fits file reduced from bias at the x adress. 
    The fits is a masterflatbias of the paste flat.
    If d is diferent from 1, it returns only an array of the masterflatbias.
    '''
    #criando uma lista em que cada elemento fica como uma string do endereco de cada flat
    b = glob.glob(x+"/flat/*.fits")
    masterflat = []
    masterflatbias = []
    # laco for que ira jogar dentro da lista vazia masterflat os arrays de cada flat
    # e depois ira jogar dentro da lista vazia masteflarbias, os arrays de cada flat reduzido do bias
    for i in range(len(b)):
        img = fits.getdata(b[i])
        img = img.astype(np.float64)
        masterflat.append(img)
        masterflatbias.append((masterflat[i] - bias(1))/np.median(masterflat[i]))
    # verificando os valores de flat, se estao muito altos ou muito baixos
    if np.mean(np.median(masterflatbias,axis=0)) > 1.1:
            return "Error: The masterflat mean is too higher after normalization(the mean is higher then 1.1)"
    if np.mean(np.median(masterflatbias,axis=0)) < 0.9:
            return "Error: The masterflat mean is too lower after normalization(the mean is lower then 0.9)"
    # se a variavel for 1, entao ele retorna apenas o array da mediana do masterflatbias
    if d == 1:
        return np.median(masterflatbias,axis=0)
    # caso contrario, ele cria uma imagem fits dessa mediana do masterflatbias
    else:
        outfile = x + '/master_flat_bias.fits'
        hdu = fits.PrimaryHDU() #criando o HDU 
        hdu.data = np.median(masterflatbias,axis=0)
        hdu.writeto(outfile)


# In[32]:


# definindo a funcao science que ira reduzir todas as imagens de ciencia do masterflatbias e do masterbias
def science():
    '''
    This function has no atribute and creates all the science images cleaned by bias and flat at the science paste
    '''
    # criando uma lista com todos os enderecos de imagem de ciencia
    c = glob.glob(x+'/science/*.fits')
    # criando o laco for para que cada elemento da lista seja subtraido do masterbias, e depois dividido pelo masterflatbias
    # e em seguida cria uma imagem fits reduzida para cada imagem de ciencia
    for i in range(len(c)):
        img = fits.getdata(c[i])
        img = img.astype(np.float64)
        sci_clean = (img-bias(1))/flat(1)
        outfile = c[i][:-5] + "_clean.fits"
        hdu = fits.PrimaryHDU()
        hdu.data = sci_clean
        hdu.writeto(outfile)


# In[33]:


def test():
    '''
    This function has no atribute and creates a residual fits image that is xo2b.0006 subtracted from xo2b.0006_clean
    at the science paste, with the objective to realize a test to your reduction pipeline
    This function only works if you already did the science() function
    '''
    # criando uma funcao teste para a reducao, em que usei a imagem 0006 e sua versao reduzida de bias e flat
    # criei uma nova imagem com o modulo da diferenca entre a imagem e a imagem reduzida, e a chamei de residual
    # a nova imagem sera salva na mesma pasta science, e la poderemos checar sua aparencia a modo de saber se estao bem reduzidas
    img = fits.getdata(x+'/science/xo2b.0006.fits')
    img = img.astype(np.float64)
    img2 = fits.getdata(x+'./science/xo2b.0006_clean.fits')
    img2 = img2.astype(np.float64)
    residual = abs(img - img2)
    outfile = x + '/science/xo2b.0006_residual.fits'
    hdu = fits.PrimaryHDU()
    hdu.data = residual
    hdu.writeto(outfile)
    
    

