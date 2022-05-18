#from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from sovaViolin.functions_stage_prep import compare_all_nD_prep,compare_1D_nM_prep,compare_nD_nM_prep,compare_nD_nG_nB_prep, compare_1D_nV_nM_prep
import pandas as pd 

datos=pd.read_excel(r'D:\WEB\backend\filesSaved\SRMPrueba\derivatives\data_PREP.xlsx')

# Total
compare_all_nD_prep(datos)

# 1 estudio
compare_1D_nM_prep(datos,'SRM')

# n estudios 
compare_nD_nM_prep(datos)

#n grupos
group_dict={
    'BIOMARCADORES':['CTR','G1','G2','DCL'],
    'SRM':['SRM']
}


group_dict2={
    'BIOMARCADORES':['CTR','G1','G2','DCL']
}
compare_nD_nG_nB_prep(datos,group_dict)

# n visitas 
compare_1D_nV_nM_prep(datos,'BIOMARCADORES')

