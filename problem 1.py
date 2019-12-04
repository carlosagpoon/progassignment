import pandas as p

dt1 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
         'Math' :[80, 95, 79]}
dfdt1 = p.DataFrame (dt1, columns = ['Student', 'Math'])
dt2 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
        'Electronics' :[85, 81, 83]}
dfdt2 = p.DataFrame (dt2, columns = ['Student', 'Electronics'])
dt3 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
         'GEAS' :[90, 79, 93]}
dfdt3 = p.DataFrame (dt3, columns = ['Student', 'GEAS'])
dt4 = {'Student': ['Ice Bear', 'Panda', 'Grizzly'],
         'ESAT' :[93, 89, 99]}
dfdt4 = p.DataFrame (dt4, columns = ['Student', 'ESAT'])

Dt5 = p.merge(dfdt1, dfdt2, how = 'outer')
Dt6 = p.merge(dfdt3, dfdt4, how = 'outer')

MergedData = p.merge(Dt5, Dt6, how = 'outer')