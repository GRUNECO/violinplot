from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.GetDataframes import get_dataframe_reject
from Graphics.functions_stage_reject import compare_nD,compare_1S_0C_nM_reject,compare_nS_0C_nM_reject,compare_nS_nG_nB_reject,compare_1S_nV_nM_reject

Studies=[BIOMARCADORES,SRM]
Studies_test=[BIOMARCADORES_test,SRM_test]
datosReject=get_dataframe_reject(Studies)

# TOTAL
compare_nD(datosReject)
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

