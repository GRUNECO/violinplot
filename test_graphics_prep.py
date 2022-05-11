from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.GetDataframes import get_dataframe_prep
from Graphics.functions_stage_prep import compare_nD,compare_1D_nM_prep,compare_nD_nM_prep,compare_nD_nG_nB_prep, compare_1D_nV_nM_prep
import pandas as pd 

#Studies=[SRM,BIOMARCADORES_test]
#dataPrep=get_dataframe_prep(Studies)
#dataPrep.to_csv('dataframe_prep.csv',index=False) # saved dataframe
datos=pd.read_csv(r'D:\WEB\paquetes\violinplot\dataframe_prep.csv',sep=",")

# Total
compare_nD(datos)

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

