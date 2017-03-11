import cPickle,os,Image,gzip
import numpy as np
from util import *

print '... packaging'

source_dir='number/'

os.chdir(source_dir)
list=os.listdir('./')
data=[]
ans=[]


dict='012345678abcdefghijklmnpqrstuvwxy'
for num in list:
	os.chdir(num)
	list_pic=os.listdir('./')
	for pic in list_pic:
		img=Image.open(pic)
		img=blur1(img)
		cnt1=seed_fill(img)
		cnt2=count_fill(img)
		cnt2=(cnt2-50)/10.0
		cnt3=count_border(img)
		cnt3=(cnt3-50)/10.0
		img=blur2(img)
		arr=np.array(img)
		arr=arr.reshape(12*18).astype('int').astype('bool').astype('float32')
		arr=arr.tolist()
		arr.append(cnt1)
		arr.append(cnt2)
		arr.append(cnt3)
		arr=np.array(arr).astype('float32')
		data.append(arr)
		ans.append(float(dict.find(num)))
	os.chdir('../')

os.chdir('../')
data=np.array(data)
ans=np.array(ans)

size=len(data)

rand_arr=np.arange(size)
np.random.shuffle(rand_arr)

rand_data=[]
rand_ans=[]

for i in rand_arr:
	rand_data.append(data[i])
	rand_ans.append(ans[i])

rand_data=np.array(rand_data)
rand_ans=np.array(rand_ans)

len_train=size*0.6
len_valid=size*0.2
len_test=size-len_train-len_valid

output=((rand_data[0:len_train],rand_ans[0:len_train]),(rand_data[len_train:len_train+len_valid],rand_ans[len_train:len_train+len_valid]),(rand_data[size-len_test:size],rand_ans[size-len_test:size]))

outputfile=open('vericode.pkl','wb')
cPickle.dump(output,outputfile)
outputfile.close()

outputfile=open('vericode.pkl','rb')
outputgzipfile=gzip.open('vericode.pkl.gz','wb')
outputgzipfile.writelines(outputfile)
outputfile.close()
outputgzipfile.close()
os.remove('vericode.pkl')

