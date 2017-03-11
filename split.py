import os
import numpy as np
import Image
import shutil

print '... spliting'

source_dir='recognized/'
dest_dir='number/'

if os.path.exists(dest_dir):
	shutil.rmtree(dest_dir)

os.mkdir(dest_dir)
list=os.listdir(source_dir)
directory='123456780abcdefghijklmnpqrstuvwxy'
cnt={}
for i in directory:
	if not os.path.exists(dest_dir+i):
		os.mkdir(dest_dir+i+'/')
	cnt[i]=0

for name in list:
	img=Image.open(source_dir+name)
	img.crop((5,2,17,20)).save(dest_dir+name[0]+'/'+str(cnt[name[0]]),'png')
	cnt[name[0]]+=1
	img.crop((17,2,29,20)).save(dest_dir+name[1]+'/'+str(cnt[name[1]]),'png')
	cnt[name[1]]+=1
	img.crop((29,2,41,20)).save(dest_dir+name[2]+'/'+str(cnt[name[2]]),'png')
	cnt[name[2]]+=1
	img.crop((41,2,53,20)).save(dest_dir+name[3]+'/'+str(cnt[name[3]]),'png')
	cnt[name[3]]+=1
