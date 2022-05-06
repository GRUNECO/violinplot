from datasets import BIOMARCADORES,SRM,BIOMARCADORES_test,SRM_test
from Graphics.GetDataframes import get_dataframe_prep
from Graphics.functions_stage_prep import compare_nD,compare_1S_nM_prep,compare_nS_nM_prep,compare_nS_nG_nB_prep, compare_1S_nV_nM_prep

Studies=[BIOMARCADORES,SRM]
Studies_test=[BIOMARCADORES_test,SRM_test]
dataPrepOriginal,dataPrepBefore,dataPrepAfter=get_dataframe_prep(Studies)


# Total
compare_nD(dataPrepOriginal,'ORIGINAL')
compare_nD(dataPrepBefore,'BEFORE')
compare_nD(dataPrepAfter,'AFTER')

# 1 estudio
compare_1S_nM_prep(dataPrepOriginal,'BIOMARCADORES','ORIGINAL')
compare_1S_nM_prep(dataPrepBefore,'BIOMARCADORES','BEFORE')
compare_1S_nM_prep(dataPrepAfter,'BIOMARCADORES','AFTER')

# n estudios 
compare_nS_nM_prep(dataPrepOriginal,'ORIGINAL')
compare_nS_nM_prep(dataPrepBefore,'BEFORE')
compare_nS_nM_prep(dataPrepAfter,'AFTER')

#n grupos
group_dict={
    'BIOMARCADORES':['CTR','G1','G2','DCL'],
    'SRM':['SRM']
}


group_dict2={
    'BIOMARCADORES':['CTR','G1','G2','DCL']
}
compare_nS_nG_nB_prep(dataPrepOriginal,group_dict,'ORIGINAL')
compare_nS_nG_nB_prep(dataPrepBefore,group_dict,'BEFORE')
compare_nS_nG_nB_prep(dataPrepAfter,group_dict,'AFTER')
compare_nS_nG_nB_prep(dataPrepOriginal,group_dict2,'ORIGINAL')
compare_nS_nG_nB_prep(dataPrepBefore,group_dict2,'BEFORE')
compare_nS_nG_nB_prep(dataPrepAfter,group_dict2,'AFTER')

# n visitas 
compare_1S_nV_nM_prep(dataPrepOriginal,'BIOMARCADORES','ORIGINAL')
compare_1S_nV_nM_prep(dataPrepBefore,'BIOMARCADORES','BEFORE')
compare_1S_nV_nM_prep(dataPrepAfter,'BIOMARCADORES','AFTER')
