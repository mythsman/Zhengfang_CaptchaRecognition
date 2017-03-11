import Image,os,ImageFilter
import numpy as np
table1=[]
table2=[]
threshold1=18
for i in range(256):
	if i<threshold1:
		table1.append(0)
	else:
		table1.append(1)
threshold2=240
for i in range(256):
	if i<threshold2:
		table2.append(0)
	else:
		table2.append(1)

def blur1(im):
	im=im.convert('L')
	im=im.point(table1,'1')

	return im
def blur2(im):
	im=im.convert('L')
	im=im.filter(ImageFilter.GaussianBlur(1.5))
	im=im.point(table2,'1')
	return im

def seed_fill(im):
	arr=np.array(im.convert('L')).astype('bool').astype('int')
	height,width=arr.shape
	arr=arr.tolist()
	
	output=[]
	output.append(np.ones(width+2,).astype('int').tolist())
	for i in range(height):
		tmp=[]
		tmp.append(1)
		for j in range(width):
			tmp.append(arr[i][j])
		tmp.append(1)
		output.append(tmp)
	output.append(np.ones(width+2,).astype('int').tolist())
	arr=output
	height+=2
	width+=2
	def dfs(i,j):
		if(arr[i][j]==0):
			return 0
		arr[i][j]=0
		if(i>0):
			dfs(i-1,j)
		if(i<height-1):
			dfs(i+1,j)
		if(j>0):
			dfs(i,j-1)
		if(j<width-1):
			dfs(i,j+1)
		return 1
	cnt=0
	for i in range(height):
		for j in range(width):
			cnt+=dfs(i,j)
	return cnt

def count_border(im):
	arr=np.array(im.convert('L')).astype('bool').astype('int')
	height,width=arr.shape
	cnt=0
	for i in range(height):
		for j in range(width):
			if arr[i][j]==1:
				continue
			if i==0 or i==height-1 or j==0 or j==width-1 :
				cnt+=1
				continue
			if arr[i-1][j]==1 or arr[i+1][j]==1 or arr[i][j-1]==1 or arr[i][j+1]==1:
				cnt+=1
	return cnt


def count_fill(im):
	arr=np.array(im.convert('L')).astype('bool').astype('int')
	height,width=arr.shape
	cnt=0
	for i in range(height):
		for j in range(width):
			if arr[i][j]==0:
				cnt+=1
	return cnt


