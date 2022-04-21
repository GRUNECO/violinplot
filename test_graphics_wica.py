import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from datasets import BIOMARCADORES
from datasets import SRM
from Graphics.graphicsViolin import get_dataframe_wica
import numpy as np
import itertools
from pprint import pprint


Studies=[BIOMARCADORES,SRM]

datosWica=get_dataframe_wica(Studies)

# WICA  ESTUDIO

def compare_1S_wica(data,name_study,plot=False):
    s=data["Study"]==name_study
    filter_study=data[s]
    figure1=plt.figure(figsize=(30,60), dpi=30)
    sns.violinplot(x='Study',y='componentes',data=filter_study)
    plt.xticks(fontsize=70)
    plt.yticks(fontsize=70)
    figure1.tight_layout()
    if plot:
        plt.show()
    return figure1
def compare_nS_wica(data,plot=False):
    studies=data["Study"].unique()
    listofimages=[]
    for study in studies:
        compare_1S_wica(data,study,plot=False)
        plt.savefig('Images/wica/'+study+'.png')
        listofimages+=['Images/wica/'+study+'.png']

    return listofimages

'''
# Wica
compare_1S_wica(datosWica,'SRM',True)
create_collage(2,1,1100, 1000,compare_nS_wica(datosWica,plot=False))
'''