from tokenize import group
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
#from .functionsImages import create_collage,createCollage,fig2img_encode
import numpy as np
import pandas as pd 

 

def compare_norm_1D_1G_nB_nV_1ROI_power(data,name_dataset,name_roi,num_col=4,save=False,plot=False):
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
    #data['Session']=data['Session'].replace({'VO':'V0'})
    data['Group']=data['Group'].replace({'G2':'CTR'})
    filter=data["Study"]==name_dataset
    filter_group_dataset=data[filter]
    sns.set(rc={'figure.figsize':(5,5)})
    sns.set_theme(style="white")
    axs=sns.catplot(x='Session',y="Powers",data=filter_group_dataset,hue='Stage',dodge=True, kind="box",col='Bands',col_wrap=num_col,palette='winter_r',fliersize=1.5,linewidth=0.5,legend=False)
    plt.yticks(np.arange(0,0.8,0.1))
    axs.set(xlabel=None)
    axs.set(ylabel=None)
    if name_roi=='C':
        name_roi='Central'
    if name_roi=='T':
        name_roi='Temporal'
    if name_roi=='PO':
        name_roi='Parieto-occipital'
    if name_roi=='F':
        name_roi='Frontal'
    axs.fig.suptitle('Relative power of normalized and preprocessed data in ROI: '+ r'$\bf{' +name_roi+r'}$'+ ' for all sessions')
    axs.add_legend(loc='upper center',bbox_to_anchor=(.5,.96),ncol=2)
    #axs.fig.subplots_adjust(top=0.857,bottom=0.121, right=0.986,left=0.05, hspace=0.138, wspace=0.062) # adjust the Figure in rp
    axs.fig.subplots_adjust(top=0.824,bottom=0.12, right=0.88,left=0.129, hspace=0.276, wspace=0.143) # adjust the Figure in rp
    axs.fig.text(0.5, 0.04, 'Session', ha='center', va='center')
    axs.fig.text(0.08, 0.5,  'Relative powers', ha='center', va='center',rotation='vertical')
    if save==True:
        plt.savefig('violinplot\Resultados\Graphics_rois\{name_dataset}_CTR+G2_{name_roi}.png'.format(name_dataset=name_dataset,name_roi=name_roi))
        plt.close()
    if plot==True:
        plt.show()
    return 


    
