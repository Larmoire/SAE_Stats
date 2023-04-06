import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
immat = pd.read_csv('csv/data_immat.csv', sep=';')
rgc = pd.read_csv('csv/RGC_2013.csv', sep=';')

def anomalies():
    prefecture =  rgc[rgc['ADMI']<4][['DEP', 'COM', 'NOM']]
    prefecture['CODCOM'] = prefecture['DEP'].astype(str).str.zfill(2) + prefecture['COM'].astype(str).str.zfill(3)
    dep = prefecture[['NOM', 'CODCOM']]
    corrige = pd.merge(immat, dep, 'inner', left_on='code commune', right_on='CODCOM')
    #Si code commune != codcom alors on remplace code commune par codcom
    corrige['code commune'] = np.where(corrige['code commune'] != corrige['CODCOM'], corrige['CODCOM'], corrige['code commune'])
    corrige = corrige.drop(['CODCOM'], axis=1)
    corrige = corrige.drop(['NOM'], axis=1)
    print(corrige['libelle commune'])
    print(corrige[corrige['libelle commune'] == 'Nantes'])


anomalies()