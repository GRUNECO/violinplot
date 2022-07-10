from sovaViolin.functions_stage_reject import compare_all_nD_reject
from sovaViolin.functions_stage_reject import compare_nD_reject
from sovaViolin.functions_stage_reject import compare_1D_nG_nM_reject
from sovaViolin.functions_stage_reject import compare_1D_nV_nM_reject
from sovaViolin.functions_dataframes import concat_df
import pandas as pd 

save_path='D:/TDG/filesSaved/'
datosReject=concat_df(save_path+'*/*/*reject.feather')

# Renombrando del inglés al español 
datosReject['Metric'] = datosReject['Metric'].map(
    {'i_kurtosis_min':'Curtosis inicial mínima',
    'i_kurtosis_max':'Curtosis inicial máxima',
    'i_amplitude_min':'Amplitud inicial mínima',
    'i_amplitude_max':'Amplitud inicial máxima',
    'i_trend':'Tendencia inicial',
    'f_kurtosis_min':'Curtosis final mínima',
    'f_kurtosis_max':'Curtosis final máxima',
    'f_amplitude_min':'Amplitud final mínima',
    'f_amplitude_max':'Amplitud final máxima',
    'f_trend':'Tendencia final',
    'f_spectrum_min':'Espectro final mínimo',
    'f_spectrum_max':'Espectro final máximo'
    },
    na_action=None)


# TOTAL
compare_all_nD_reject(datosReject,color='hsv_r',plot=True,encode=False)

#  n estudios 
compare_nD_reject(datosReject,color="hsv_r",plot=True,encode=False)

# n group 
compare_1D_nG_nM_reject(datosReject,'Biomarcadores',color='hsv_r',plot=True,encode=False)
compare_1D_nG_nM_reject(datosReject,'SRM',color='hsv_r',plot=True,encode=False)
compare_1D_nG_nM_reject(datosReject,'CHBMP',color='hsv_r',plot=True,encode=False)

#n sessions
compare_1D_nV_nM_reject(datosReject,'SRM',color='hsv_r',plot=True,encode=False)
compare_1D_nV_nM_reject(datosReject,'Biomarcadores',color='hsv_r',plot=True,encode=False)





'''
# 1 estudio
compare_1S_0C_nM_reject(datosReject,'BIOMARCADORES') 

'''


