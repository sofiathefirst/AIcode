import pandas as pd

b= pd.read_csv('b.csv', sep=',',dtype={'id':str})
 
#
print('shape:',b.shape)

#行访问
print('show a row:\n',b.iloc[0],'\nshow row end\n*************\n' )  

#减一行
print('befor drop row2 \n',b,'\n**********\n')
b=b.drop(2)
#b=b.drop(3)
print('after drop row2 \n',b,'\n**********\n')
#加一行
b.loc[4]=b.loc[1]
print(b)

#列访问
print('colum name:\n',b['name'])

print('colum id:\n',b['id'])

#加一列
b['nid']=None

#减一列
del b['nid']

#提取年月日
b['year']=b['id'].str[6:10]
b['mon']=b['id'].str[10:12]
b['day']=b['id'].str[12:14]
#修改类型
b['year']=pd.to_numeric(b['id'].str[6:10])
print(b)
print('\n\niterrows:****************\n')
for key,row in b.iterrows():
	print(key,row, row['id'])

#save file
b.to_csv('newb.csv')
#good pandas tutorils link
#https://www.yiibai.com/pandas/python_pandas_iteration.html

	

