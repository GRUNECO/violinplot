from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.GetDataframes import get_dataframe_wica
from Graphics.functions_stage_wica import compare_1S_wica,compare_nS_wica,compare_1S_nV_wica,compare_nS_nG_wica,compare_nS_nG_wica


Studies=[BIOMARCADORES,SRM]
Studies_test=[BIOMARCADORES_test,SRM_test]
datosWica=get_dataframe_wica(Studies)


#TOTAL

# 1 estudio
compare_1S_wica(datosWica,'SRM',True)
# n estudios 
compare_nS_wica(datosWica)
# n grupos

# n visitas
compare_1S_nV_wica(datosWica,'BIOMARCADORES')


#N GRUPOS
group_dict1={
    'BIOMARCADORES':['CTR','DCL','G1','G2'],
    'SRM':['SRM'] # assume datasets with no groups have Group=Study
}
compare_nS_nG_wica(datosWica,group_dict1)

group_dict2={
    'BIOMARCADORES':['CTR','DCL','G1','G2'],
}
compare_nS_nG_wica(datosWica,group_dict2)
