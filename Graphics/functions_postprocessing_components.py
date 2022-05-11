from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import create_collage,createCollage
import numpy as np
import pandas as pd 


# *************************** COMPARISON BETWEEN NORMALIZE DATA AND PROCESSING DATA **************

def compare_norm_1D_1G_nB_comp_power(data,name_dataset,name_group):
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    sns.boxplot(x='Bands',y="Powers",data=filter_group_dataset,hue="Stage",palette='winter_r',fliersize=1.5,linewidth=0.5)
    plt.title('Relative power bands of normalized and preprocessed data given by '+name_group)
    plt.yticks(np.arange(0,1,0.1))
    plt.show()

def compare_norm_1D_1G_nB_nV_power(data,name_dataset,name_group):
    
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    p=sns.catplot(x='Session',y="Powers",data=filter_group_dataset,hue="Stage",dodge=True, kind="box",col='Bands',col_wrap=4,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    plt.yticks(np.arange(0,1,0.1))
    p.set(xlabel=None)
    p.fig.subplots_adjust(top=0.925,bottom=0.130, right=0.970,left=0.051) # adjust the Figure in rp
    p.fig.suptitle('Relative power bands of normalized and preprocessed data given by '+name_group+" and all visits")
    plt.legend(loc='upper right',bbox_to_anchor=(0.95,0.95))
    plt.show()


# **************************** PROCESSING DATA WHITOUT NORMALIZING *********************************************
