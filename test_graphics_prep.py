#from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from sovaViolin.functions_stage_prep import compare_all_nD_prep
from sovaViolin.functions_stage_prep import compare_1D_nV_nM_prep
from sovaViolin.functions_stage_prep import compare_1D_nG_prep
from sovaViolin.functions_stage_prep import compare_nD_prep
from sovaViolin.functions_dataframes import concat_df
import pandas as pd 

save_path='D:\XIMENA\BIDS\Estudiantes2021\derivatives\Long_format'
data_prep= pd.read_feather(save_path+ '\data_CE_PREP.feather')

#data_prep=concat_df(save_path+'*/*/*PREP.feather')

# Renombrando del inglés al español 
data_prep['Metric'] = data_prep['Metric'].map(
    {'bad_by_nan':'Canales malos tipo NAN',
    'bad_by_flat':'Canales malos tipo planos',
    'bad_by_deviation':'Canales malos por desviación',
    'bad_by_hf_noise':'Canales malos por ruido de alta frecuencia',
    'bad_by_correlation':'Canales malos por correlación',
    'bad_by_SNR':'Canales malos por relación señal-ruido ',
    'bad_by_dropout':'Canales malos por dropout',
    'bad_by_ransac':'Canales malos por ransac',
    'bad_all':'Canales malos en general'
    },
    na_action=None)

data_prep['State'] = data_prep['State'].map(
    {'original':'Señal original',
    'before_interpolation':'Antes de interpolar',
    'after_interpolation':'Después de interpolar'
    },
    na_action=None)

# Overall

#compare_all_nD_prep(data_prep,color="hsv_r",plot=True,encode=False)

# n studies 
#compare_nD_prep(data_prep,color='hsv_r',plot=True,encode=False)

# n sessions 

compare_1D_nV_nM_prep(data_prep,'CHBMP',color='hsv_r',plot=True,encode=False)
#compare_1D_nV_nM_prep(data_prep,'SRM',color='hsv_r',plot=True,encode=False)


# n Groups
#compare_1D_nG_prep(data_prep,'Biomarcadores',color='hsv_r',plot=True,encode=False)
#compare_1D_nG_prep(data_prep,'SRM',color='hsv_r',plot=True,encode=False)
#compare_1D_nG_prep(data_prep,'CHBMP',color='hsv_r',plot=True,encode=False)



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