import os
import numpy as np
import shutil

folder = 'road_2s_28f'
directory = './datasets/MRBT_DATASET/'+folder+'_out'
try:
	os.stat(directory)
except:
	os.mkdir(directory)
	print('creating output directory: '+folder+'_out')




data = os.listdir('./datasets/MRBT_DATASET/'+folder)
data =  np.asarray(data)
for prvok in data:
	print('########################## prebieha vypocet pre :'+prvok)
	os.system('./darknet detect cfg/yolov3.cfg yolov3.weights datasets/MRBT_DATASET/'+folder+'/' + prvok)	
	tmp = os.path.splitext(prvok)[0]
	print(tmp)
	shutil.move('./predictions.png','./datasets/'+tmp+'.png')





