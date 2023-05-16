#from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from sovaViolin.functions_stage_prep import compare_all_nD_prep
from sovaViolin.functions_stage_prep import compare_1D_nV_nM_prep
from sovaViolin.functions_stage_prep import compare_1D_nG_prep
from sovaViolin.functions_stage_prep import compare_nD_prep
from sovaViolin.functions_stage_reject import compare_nD_reject
from sovaViolin.functions_stage_wica import compare_nD_wica
from sovaViolin.functions_dataframes import concat_df
import pandas as pd 


save_path=r'C:\Users\veroh\OneDrive - Universidad de Antioquia\Datos_MsC_Veronica'


data_prep=concat_df(save_path+'/*/derivatives/*PREP.feather')
datosWica=concat_df(save_path+'/*/derivatives/*wICA.feather')
datosReject=concat_df(save_path+'/*/derivatives/*reject.feather')

# Renombrando del inglés al español 
data_prep['Metric'] = data_prep['Metric'].map(
    {'bad_by_nan':'Channels in nan',
    'bad_by_flat':'Flat channels ',
    'bad_by_deviation':'Channels by deviation',
    'bad_by_hf_noise':'Channels with high frequency noise',
    'bad_by_correlation':'Channels by correlation',
    'bad_by_SNR':'Channels by SNR',
    'bad_by_dropout':'Channels by dropout',
    'bad_by_ransac':'Channels by ransac',
    'bad_all':'Bad channels'
    },
    na_action=None)

data_prep['State'] = data_prep['State'].map(
    {'original':'Original signal',
    'before_interpolation':'Before interpolating',
    'after_interpolation':'After interpolating'
    },
    na_action=None)

# Renombrando del inglés al español 
datosReject['Metric'] = datosReject['Metric'].map(
    {'i_kurtosis_min':'Minimum initial kurtosis',
    'i_kurtosis_max':'Maximum initial kurtosis',
    'i_amplitude_min':'Minimum Initial Amplitude',
    'i_amplitude_max':'Maximum Initial Amplitude',
    'i_trend':'Initial trend',
    'f_kurtosis_min':'Minimum final kurtosis',
    'f_kurtosis_max':'Maximum final kurtosis',
    'f_amplitude_min':'Minimum final amplitude',
    'f_amplitude_max':'Maximum final amplitude',
    'f_trend':'End trend',
    'f_spectrum_min':'Minimum end spectrum',
    'f_spectrum_max':'Maximum end spectrum'
    },
    na_action=None)
# Overall

#compare_all_nD_prep(data_prep,color="hsv_r",plot=True,encode=False)

colors = ['#127369','#45C4B0','#10403B','#8AA6A3']
# n studies 
compare_nD_prep(data_prep,color=colors,plot=True,encode=False)
compare_nD_reject(datosReject,color=colors,plot=True,encode=False)
compare_nD_wica(datosWica,color=colors,plot=True,encode=False)

# n sessions 

#compare_1D_nV_nM_prep(data_prep,'CHBMP',color='hsv_r',plot=True,encode=False)
#compare_1D_nV_nM_prep(data_prep,'SRM',color='hsv_r',plot=True,encode=False)


# n Groups
#compare_1D_nG_prep(data_prep,'BIOMARCADORES',color='#127369',plot=True,encode=False)
#compare_1D_nG_prep(data_prep,'DUQUE',color=['#10403B'],plot=True,encode=False)
#compare_1D_nG_prep(data_prep,'SRM',color='#8AA6A3',plot=True,encode=False)
#compare_1D_nG_prep(data_prep,'CHBMP',color='#45C4B0',plot=True,encode=False)



'''
# 1 estudio
compare_1D_nM_prep(data_prep,'SRM')


#n grupos
group_dict={
    'BIOMARCADORES':['CTR','G1','G2','DCL'],
    'SRM':['SRM']
}


group_dict2={
    'BIOMARCADORES':['CTR','G1','G2','DCL']
}
compare_nD_nG_nB_prep(data_prep,group_dict)

'''