import cPickle,os,Image,ImageFilter,theano,sys,time
import numpy as np
from logistic_sgd import LogisticRegression
from util import *



def recognize(pic='test'):
	im=Image.open(pic)

	#split
	image=[]
	image.append(im.crop((5,2,17,20)))
	image.append(im.crop((17,2,29,20)))
	image.append(im.crop((29,2,41,20)))
	image.append(im.crop((41,2,53,20)))

	#package
	arr=[]
	for img in image:
		img=blur1(img)
		cnt1=seed_fill(img)
		cnt2=count_fill(img)
		cnt2=(cnt2-50)/50
		cnt3=count_border(img)
		cnt3=(cnt3-50)/50
		img=blur2(img)
		array=np.array(img)
		array=array.reshape(12*18).astype('int').astype('bool').astype('float32')
		array=array.tolist()
		array.append(cnt1)
		array.append(cnt2)
		array.append(cnt3)
		array=np.array(array).astype('float32')
		arr.append(array)

	arr=np.array(arr)

	#predict
	classifier = cPickle.load(open('best_model.pkl'))
	predict_model = theano.function(inputs=[classifier.input],outputs=classifier.y_pred)
	predicted_values = predict_model(arr)
	dict='012345678abcdefghijklmnpqrstuvwxy'
	pred=[]
	for i in range(len(predicted_values)):
		pred.append(dict[predicted_values[i]])
	return pred[0]+pred[1]+pred[2]+pred[3]


def recur_recognize(path):
	if not path[-1]=='/':
		path.join('/')
	files=os.listdir(path)
	cost=time.time()
	for i in files:
		#print '.',	
		#sys.stdout.flush()
		old_name=path+str(i)
		name=recognize(old_name)
		new_name=path+str(name)
		os.rename(old_name,new_name)
		
	return time.time()-cost,len(files)
	

if __name__ == '__main__':
	if len(sys.argv) <2:
		print 'Please enter the file'
	else:	
		if os.path.isdir(sys.argv[1]):
			cost,size= recur_recognize(sys.argv[1])
			print '\nRecognized '+str(size)+' pictures , in '+str(cost)+' s\n'
		else:
			print recognize(sys.argv[1])
