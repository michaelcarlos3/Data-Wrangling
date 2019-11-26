import pandas as pd


w={'Student':['Ice Bear', 'Panda', 'Grizzly'],
   'Math':[80, 95, 79]}
a=pd.DataFrame(w, columns=['Student', 'Math'])

x={'Student':['Ice Bear', 'Panda', 'Grizzly'],
   'Electronics':[85, 81, 93]}
b=pd.DataFrame(x, columns=['Student', 'Electronics'])

y={'Student':['Ice Bear', 'Panda', 'Grizzly'],
   'GEAS':[90, 79, 93]}
c=pd.DataFrame(y, columns=['Student', 'GEAS'])

z={'Student':['Ice Bear', 'Panda', 'Grizzly'],
   'ESAT':[93, 89, 88]}
d=pd.DataFrame(z, columns=['Student', 'ESAT'])

result=pd.merge(a, b, how='right', on='Student')
result2=pd.merge(c, d, how='right', on='Student')
result3=pd.merge(result, result2, how='right', on='Student')