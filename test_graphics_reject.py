from sovaViolin.functions_stage_reject import compare_all_nD_reject,compare_1S_0C_nM_reject,compare_nS_0C_nM_reject,compare_nS_nG_nB_reject,compare_1S_nV_nM_reject
import pandas as pd 

datosReject=pd.read_excel(r'D:\WEB\backend\filesSaved\BIOMARCADORES_TEST\derivatives\data_reject.xlsx')

# TOTAL
compare_all_nD_reject(datosReject,plot=True,encode=False)
# 1 estudio
compare_1S_0C_nM_reject(datosReject,'BIOMARCADORES') 
#  n estudios 
compare_nS_0C_nM_reject(datosReject)
# n group 
group_dict={
    'BIOMARCADORES':['CTR','G1','G2','DCL'],
    'SRM':['SRM'] # assume datasets with no groups have Group=Study
}
compare_nS_nG_nB_reject(datosReject,group_dict)
#n visit
compare_1S_nV_nM_reject(datosReject,'BIOMARCADORES') 

