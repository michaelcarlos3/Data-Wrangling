import pandas as pd

x = {'Box':'Box1','Dimension':['Length','Width','Height'],'Value':[6,4,2]}
Box1 = pd.DataFrame(x,columns = ['Box','Dimension','Value'])

y = {'Box':'Box2','Dimension':['Length','Width','Height'],'Value':[5,3,4]}
Box2 = pd.DataFrame(y,columns = ['Box','Dimension','Value'])

messy = Box1.append(Box2).reset_index().drop(columns = ['index'])

tidy = messy.pivot_table(index = 'Box',columns = 'Dimension',values = 'Value').reset_index()

z = {'Box':['Box1','Box2'],'Volume':[6*4*2,5*3*4]}
Volume = pd.DataFrame(z,columns = ['Box','Volume'])

tidyfinal = pd.merge(tidy,Volume, how='right',on='Box')