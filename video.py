#!/usr/bin/env python3

try:
	import os
	import numpy as np
	import shutil
	import time
	import sys
except:
	print('Err[1]: import err')

#directory managing
folder = 'road_2s_28f'
directory = './datasets/MRBT_DATASET/'+folder+'_out'

try:
	os.stat(directory)
except:
	os.mkdir(directory)
	print('creating output directory: '+folder+'_out')

try:
	os.stat('./datasets/datalog.txt')
except:
	fp = open('./datasets/datalog.txt','a') 
	print('creating datalog:    [log.txt]')
	fp.close()

Zadany_subor = sys.argv[-1]

## CPU mode only for single & multiple picture object classification
# choose single or multishot mode



# Single shot mode for single picture 

if Zadany_subor != 'video.py':
	start_time = time.time()
	print('########################## prebieha vypocet pre vybraty obrazok')
	os.system('./darknet detect cfg/yolov3.cfg yolov3.weights datasets/MRBT_DATASET/'+folder+'/' + sys.argv[-1])	
	shutil.move('./predictions.png','./datasets/'+sys.argv[-1])
	print('Done in ',np.around(time.time()-start_time),'!')
	fp= open('./datasets/datalog.txt','a') 
	fp.write('\n'+ time.ctime() + "\nSingleshot:\n" + str(time.time()-start_time) + '\n')
	fp.close()

			


# Multi shot mode for video sequence

if Zadany_subor == 'video.py':
	start_time = time.time()
	data = os.listdir('./datasets/MRBT_DATASET/'+folder)
	data =  np.asarray(data)
	fp= open('./datasets/datalog.txt','a') 
	fp.write("\n"+time.ctime()+"\n"+'Multishot:\n')
	for prvok in data:
		print('########################## prebieha vypocet pre :'+prvok)
		os.system('./darknet detect cfg/yolov3.cfg yolov3.weights ./datasets/MRBT_DATASET/'+folder+'/' + prvok)	
		tmp = os.path.splitext(prvok)[0]
		print(tmp)
		shutil.move('./predictions.png','./datasets/'+tmp+'.png')
		fp.write(str(time.time()-start_time)+'\n')
		start_time = time.time()
	print('Done in ', np.around(time.time()-start_time) , 's, with average pic Time', np.around((time.time()-start_time)/len(data)), 's!')	
	fp.write('\n')	
	fp.close()




