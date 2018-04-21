import os
import numpy as np
import shutil
import time
import sys


folder = 'road_2s_28f'
directory = './datasets/MRBT_DATASET/'+folder+'_out'
try:
	os.stat(directory)
except:
	os.mkdir(directory)
	print('creating output directory: '+folder+'_out')

Zadany_subor = sys.argv[-1]
## CPU mode only for single & multiple picture object classification
# choose single or multishot mode



# Single shot mode for single picture 

if Zadany_subor != 'video.py':
	start_time = time.time()
	print('########################## prebieha vypocet pre vybraty obrazok')
	os.system('./darknet detect cfg/yolov3.cfg yolov3.weights datasets/MRBT_DATASET/'+folder+'/' + sys.argv[-1])	
	shutil.move('./predictions.png','./datasets/'+sys.argv[-1])
	print('Done in '+np.around(time.time()-start_time)+'!')
		


# Multi shot mode for video sequence

if Zadany_subor == 'video.py':
	start_time = time.time()
	data = os.listdir('./datasets/MRBT_DATASET/'+folder)
	data =  np.asarray(data)
	for prvok in data:
		print('########################## prebieha vypocet pre :'+prvok)
		os.system('./darknet detect cfg/yolov3.cfg yolov3.weights ./datasets/MRBT_DATASET/'+folder+'/' + prvok)	
		tmp = os.path.splitext(prvok)[0]
		print(tmp)
		shutil.move('./predictions.png','./datasets/'+tmp+'.png')
	print('Done in ', np.around(time.time()-start_time) , 's, with average pic Time', np.around((time.time()-start_time)/len(data)), 's!')





