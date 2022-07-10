'''
@autor: Luisa María Zapata Saldarriaga, Universidad de Antioquia, luisazapatasaldarriaga@gmail.com  
@autor: Valeria Cadavid Castro,  Universidad de Antioquia
@autor: Veronica Henao Isaza,  Universidad de Antioquia

'''

from tkinter.tix import Control
from tokenize import group
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
from .functionsImages import fig2img_encode
import numpy as np
import pandas as pd 


# *************************** COMPARISON BETWEEN NORMALIZE DATA AND PROCESSING DATA **************
# TOTAL
def compare_all_nD_ncomp_power(data,plot=False,encode=False):
    '''
    Componentes de interés
    C14, C15, C18, C20, C22, C23, C24, C25 

    Parameters
    ----------
        data: dataframe
        plot: Boolean 
        encode: Boolean

    Returns 
    ----------
        img_encode
    '''
    components=['C14', 'C15','C18', 'C20', 'C22','C23', 'C24', 'C25' ]
    filter=data[data.Components.isin(components)]
    axs=sns.catplot(x='Bands',y="Powers",data=filter,hue="Stage",dodge=True, kind="box",col='Components',col_wrap=4,palette='winter_r',legend=False)
    plt.title("")
    plt.yticks(np.arange(0,1,0.1))
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.fig.suptitle('Relative power bands of normalized and preprocessed data given in components')
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    axs.set_xticklabels(rotation=45)
    axs.fig.subplots_adjust(top=0.857,bottom=0.155, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Frequency bands', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode
    return 

# ESTUDIOS
def compare_nD_ncomp_power(data,name_band,plot=False,encode=False):
    filter=data["Bands"]==name_band
    filter_band=data[filter]
    components=['C14', 'C15','C18', 'C20', 'C22','C23', 'C24', 'C25' ]
    filter_dataset=filter_band[filter_band.Components.isin(components)]
    axs=sns.catplot(x='Study',y="Powers",data=filter_dataset,hue="Stage",kind="box",col='Components',col_wrap=3,palette='winter_r',legend=False)
    axs.fig.suptitle('Relative power bands of normalized and preprocessed data given in components by '+name_band)
    axs.fig.subplots_adjust(top=0.857,bottom=0.155, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode


# GRUPOS
def compare_norm_1D_1G_nB_ncomp_power(data,name_dataset,name_group,num_columns=4,save=False,plot=False,encode=False):
    '''
    Componentes de interés
    C14, C15, C18, C20, C22, C23, C24, C25 

    Parameters
    ----------
        data: dataframe
        name_dataset: str 
        name_group: str 
        save: Boolean
        plot: Boolean 
        encode: Boolean

    Returns 
    ----------
        img_encode
    '''
    data['Session']=data['Session'].replace({'VO':'V0'})
    #data['Group']=data['Group'].replace({'G2':'CTR'})
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    components=['C14', 'C15','C18', 'C20', 'C22','C23', 'C24', 'C25' ]
    filter_group_dataset=filter_group_dataset[filter_group_dataset.Components.isin(components)]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    axs=sns.catplot(x='Bands',y="Powers",data=filter_group_dataset,hue="Stage",dodge=True, kind="box",col='Components',col_wrap=num_columns,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    plt.yticks(np.arange(0,1,0.1))
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    #Title:'Relative power bands of normalized and preprocessed data given by '+name_group +' in components'
    axs.fig.suptitle('Análisis de potencia relativa para datos normalizados y procesados en ' +name_group+ 'en componentes neuronales')
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    axs.set_xticklabels(rotation=45)
    axs.fig.subplots_adjust(top=0.857,bottom=0.155, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Frequency bands', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if save==True:
        plt.savefig('Resultados\Graphics_components\Groups\{name_dataset}_{name_group}_components.png'.format(name_dataset=name_dataset,name_group=name_group))
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode
    return 

# SESIONES 
def compare_norm_1D_1G_1B_nV_ncomp_power(data,name_dataset,name_group,name_band,num_columns=4, save=False,plot=False,encode=False):
    '''
    Componentes de interés
    C14, C15, C18, C20, C22, C23, C24, C25 

    Parameters
    ----------
        data: dataframe
        name_dataset: str
        name_group: str
        name_band: str 
        save: Boolean 
        plot: Boolean 
        encode: Boolean

    Returns 
    ----------
        img_encode
    '''
    data['Session']=data['Session'].replace({'VO':'V0'})
    #data['Group']=data['Group'].replace({'G2':'CTR'})
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    components=['C14', 'C15','C18', 'C20', 'C22','C23', 'C24', 'C25' ]
    filter_component=filter_group_dataset[filter_group_dataset.Components.isin(components) & filter_group_dataset.Bands.isin([name_band])] 
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    axs=sns.catplot(x='Session',y="Powers",data=filter_component,hue='Stage',dodge=True, kind="box",col='Components',col_wrap=num_columns,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    plt.yticks(np.arange(0,1,0.1))
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    if name_group=="CTR":
        name_group="healthy "
    #axs.fig.suptitle('Relative '+r'$\bf{' +name_band+r'}$'+ ' power of normalized and preprocessed data given by '+r'$\bf{' +name_group+ '-control'+r'}$'+' in components and all visits')
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    axs.fig.subplots_adjust(top=0.857,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Sessions', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if save==True:
        plt.savefig('Resultados\Graphics_components\Visits\{name_dataset}_{name_group}_{name_band}_components.png'.format(name_dataset=name_dataset,name_group=name_group,name_band=name_band))
        plt.close()
    if plot:
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode
    return 

def compare_norm_1D_1G_1B_nV_all_comp_power(data,name_dataset,name_group,num_columns=4, save=False,plot=False,encode=False):
    '''
    Componentes de interés
    C14, C15, C18, C20, C22, C23, C24, C25 

    Parameters
    ----------
        data: dataframe
        name_dataset: str
        name_group: str
        name_band: str 
        save: Boolean 
        plot: Boolean 
        encode: Boolean

    Returns 
    ----------
        img_encode
    '''
    data['Session']=data['Session'].replace({'VO':'V0'})
    #data['Group']=data['Group'].replace({'G2':'CTR'})
    filter=np.logical_and(data["Study"]==name_dataset, data["Group"]==name_group)
    filter_group_dataset=data[filter]
    sns.set(rc={'figure.figsize':(11.7,8.27)})
    sns.set_theme(style="white")
    axs=sns.catplot(x='Session',y="Powers",data=filter_group_dataset,hue="Stage",dodge=True, kind="box",col='Bands',col_wrap=num_columns,palette='winter_r',legend=False)
    plt.yticks(np.arange(0,1,0.1))
    axs.fig.suptitle('Relative power bands of normalized and preprocessed data given by '+name_group+" and all visits")
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.95),ncol=2)
    axs.fig.subplots_adjust(top=0.857,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Sessions', ha='center', va='center')
    axs.fig.text(0.01, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    
    if save:
         plt.savefig('Resultados\Graphics_components\Visits\{name_dataset}_{name_group}_visits_all_components.png'.format(name_dataset=name_dataset,name_group=name_group))
    if plot: 
        plt.show()
    if encode:
        img_encode=fig2img_encode(axs)
        plt.cla()
        plt.close()
        return img_encode
    return 


