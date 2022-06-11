BIOMARCADORES = {
    'name':'BIOMARCADORES',
    'input_path':r'E:\Academico\Universidad\Posgrado\Tesis\Datos\BASESDEDATOS\BIOMARCADORES_BIDS',
    #'input_path':r'F:\BIOMARCADORES',
    'layout':{'extension':'.vhdr', 'task':'CE','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[60]},
    'group_regex':'(.+).{3}',
    'events_to_keep':None,
    'run-label':'restCE',
    'session':'V'
}

BIOMARCADORESMini = {
    'name':'BIOMARCADORES',
    'input_path':r'E:\Academico\Universidad\Posgrado\Tesis\CodificadoBIDSMini',
    'layout':{'extension':'.vhdr', 'task':'CE','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[60]},
    'group_regex':'(.+).{3}',
    'events_to_keep':None,
    'run-label':'restCE'
}

BIOMARCADORES_test = {
    'name':'BIOMARCADORES',
    'input_path':r'D:\WEB\backend\filesSaved\BIOMARCADORES_TEST',
    'layout':{'extension':'.vhdr', 'task':'CE','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[60]},
    'group_regex':'(.+).{3}',
    'events_to_keep':None,
    'run-label':'restCE',
    'session':'V'
}
CHBMP = {
    'name':'CHBMP',
    'input_path':r'D:\BASESDEDATOS\CHBMP',
    'layout':{'extension':'.edf', 'task':'protmap','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[60],},
    'group_regex':None,
    'events_to_keep':[65],
    'run-label':'restCE',
    'session':None
}

LEMON = {
    'name':'LEMON',
    'input_path':r'D:\BASESDEDATOS\LEMON_BIDS',
    'layout':{'extension':'.vhdr', 'task':'resting','suffix':'eeg', 'return_type':'filename'},
    'args':{'resample':1000,'line_freqs':[50],},
    'group_regex':None,
    'events_to_keep':[5],
    'run-label':'restEC',
    'session':None
}


SRM_test = {
    'name':'SRM',
    'input_path':r'D:\WEB\backend\filesSaved\SRMPrueba',
    'layout':{'extension':'.edf', 'task':'resteyesc','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[50]},
    'group_regex':None,
    'events_to_keep':None,
    'run-label':'restCE',
    'session':'V'
}

