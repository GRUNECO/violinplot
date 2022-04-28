BIOMARCADORES = {
    'name':'BIOMARCADORES',
    'input_path':r'D:\BASESDEDATOS\BIOMARCADORES_BIDS',
   # 'input_path':r'D:\BASESDEDATOS\biomarcadoresprueba',
    'layout':{'extension':'.vhdr', 'task':'OE','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[60]},
    'group_regex':'(.+).{3}',
    'events_to_keep':None,
    'run-label':'restEC',
<<<<<<< HEAD
    'session':'x'
=======
    'session':'V'
>>>>>>> 3731e34a24da39f34090feb8df58b1e833cf852a
}

SRM= {
    'name':'SRM',
<<<<<<< HEAD
    'input_path':r'D:\BASESDEDATOS\SRM',
=======
    'input_path':r'D:\WEB\backend\filesSaved\SRM',
    #'input_path':r'E:\Academico\Universidad\Posgrado\Tesis\Datos\BASESDEDATOS\SRM',
>>>>>>> 3731e34a24da39f34090feb8df58b1e833cf852a
    'layout':{'extension':'.edf', 'task':'resteyesc','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[50]},
    'group_regex':None,
    'events_to_keep':None,
    'run-label':'restEC',
<<<<<<< HEAD
    'session':'x'
=======
    'session':'V'
>>>>>>> 3731e34a24da39f34090feb8df58b1e833cf852a
}
CHBMP = {
    'name':'CHBMP',
    'input_path':r'D:\BASESDEDATOS\CHBMP',
    'layout':{'extension':'.edf', 'task':'protmap','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[60],},
    'group_regex':None,
    'events_to_keep':[65],
    'run-label':'restEC',
    'session':None
}

LEMON = {
    'name':'LEMON',
    'input_path':r'E:\Academico\Universidad\Posgrado\Tesis\Datos\BASESDEDATOS\LEMON_BIDS',
    'layout':{'extension':'.vhdr', 'task':'resting','suffix':'eeg', 'return_type':'filename'},
    'args':{'resample':1000,'line_freqs':[50],},
    'group_regex':None,
    'events_to_keep':[5],
    'run-label':'restEC',
    'session':None
}

<<<<<<< HEAD
=======

BIOMARCADORES_test = {
    'name':'BIOMARCADORES',
    'input_path':r'D:\WEB\backend\filesSaved\PRUEBA',
    'layout':{'extension':'.vhdr', 'task':'OE','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[60]},
    'group_regex':'(.+).{3}',
    'events_to_keep':None,
    'run-label':'restEC',
    'session':'V'
}

SRM_test = {
    'name':'SRM',
    'input_path':r'D:\WEB\backend\filesSaved\SRMPrueba',
    'layout':{'extension':'.edf', 'task':'resteyesc','suffix':'eeg', 'return_type':'filename'},
    'args':{'line_freqs':[50]},
    'group_regex':None,
    'events_to_keep':None,
    'run-label':'restEC',
    'session':'V'
}
>>>>>>> 3731e34a24da39f34090feb8df58b1e833cf852a
