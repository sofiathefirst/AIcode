import pandas as pd
import matplotlib.pyplot as plt 
'''
粗略统计二胎年龄差距
se 为1 主申请人，多数为爸爸
se为2共同申请人，多为妈妈和孩子
se为0，others
'''
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

