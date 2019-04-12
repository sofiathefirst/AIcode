import pandas as pd
import matplotlib.pyplot as plt 
#difage = []
class family:
	def __init__(self):
		self.mainpyear= None
		self.comPyear=[]
		self.diff = []

	def diff_age(self):
		if len(self.comPyear)>2:
			self.comPyear = sorted(self.comPyear, reverse = True)
			#print(self.comPyear)
			if( self.comPyear[0]-self.comPyear[1]<18):
				self.diff.append( self.comPyear[0]-self.comPyear[1])
		self.comPyear=[]

if __name__ == '__main__':			
	b= pd.read_csv('a.csv', sep=',', dtype = {'id':str})
	b['year']=pd.to_numeric(b['id'].str[6:10])

	myf = family()
	for key,row in b.iterrows():
		if( row['se']==1):
			myf.mainpyear = row['year']
			myf.diff_age()
		elif( row['se']==2):
			myf.comPyear.append(row['year'])
			#myf.diff_age()
	

	#print(myf.diff)
	a = pd.Series(myf.diff)
	a.plot.hist(bins =19 )
	plt.show()

	'''
	#
	b.shape

	#行访问
	b.iloc[0]   

	#加一行
	b.loc[9]=b.loc[3]

	#减一行
	b.drop(4)

	#列访问
	b['name']

	#加一列
	b['nid']=None

	#减一列
	del b['nid']
	#提取年月日
	b['year']=b['id'].str[6:10]
	b['mon']=b['id'].str[10:12]
	b['day']=b['id'].str[12:14]
	#修改类型
	b['mon']=pd.to_numeric(b['id'].str[6:10])
	'''

	






