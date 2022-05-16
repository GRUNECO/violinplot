from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import create_collage,createCollage
import numpy as np
import pandas as pd 


# *************************** COMPARISON BETWEEN NORMALIZE DATA AND PROCESSING DATA **************

def compare_norm_1D_1G_nB_ncomp_power(data,name_dataset,name_group,save=False):
    '''
    Componentes de interés
    C14, C15, C18, C20, C22, C23, C24, C25 
    '''
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    components=['C14', 'C15','C18', 'C20', 'C22','C23', 'C24', 'C25' ]
    filter_group_dataset=filter_group_dataset[filter_group_dataset.Components.isin(components)]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    p=sns.catplot(x='Bands',y="Powers",data=filter_group_dataset,hue="Stage",dodge=True, kind="box",col='Components',col_wrap=4,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    plt.yticks(np.arange(0,1,0.1))
    p.set(xlabel=None)
    p.set(ylabel=None)
    p.fig.suptitle('Relative power bands of normalized and preprocessed data given by '+name_group +' in components')
    p.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    p.set_xticklabels(rotation=45)
    p.fig.subplots_adjust(top=0.857,bottom=0.155, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    p.fig.text(0.5, 0.04, 'Frequency bands', ha='center', va='center')
    p.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if save==True:
        plt.savefig('Resultados\Graphics_components\Groups\{name_dataset}_{name_group}_components.png'.format(name_dataset=name_dataset,name_group=name_group))
    return 
def compare_norm_1D_1G_1B_nV_ncomp_power(data,name_dataset,name_group,name_band, save=False):
    '''
    Componentes de interés
    C14, C15, C18, C20, C22, C23, C24, C25 
    '''
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    components=['C14', 'C15','C18', 'C20', 'C22','C23', 'C24', 'C25' ]
    filter_component=filter_group_dataset[filter_group_dataset.Components.isin(components) & filter_group_dataset.Bands.isin([name_band])] 
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    p=sns.catplot(x='Session',y="Powers",data=filter_component,hue='Stage',dodge=True, kind="box",col='Components',col_wrap=4,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    plt.yticks(np.arange(0,1,0.1))
    p.set(xlabel=None)
    p.set(ylabel=None)
    p.fig.suptitle('Relative '+ name_band+ ' power of normalized and preprocessed data given by '+name_group +' in components and all visits')
    p.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    p.fig.subplots_adjust(top=0.857,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    p.fig.text(0.5, 0.04, 'Frequency bands', ha='center', va='center')
    p.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if save==True:
        plt.savefig('Resultados\Graphics_components\Visits\{name_dataset}_{name_group}_{name_band}_components.png'.format(name_dataset=name_dataset,name_group=name_group,name_band=name_band))
    plt.show()
    return 
# **************************** PROCESSING DATA WHITOUT NORMALIZING *********************************************