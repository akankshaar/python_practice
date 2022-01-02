from google.colab import drive
drive.mount('/gdrive')
%cd /gdrive

# Run this cell to mount your Google Drive.
from google.colab import drive
drive.mount('/content/drive')
import os
import glob
import matplotlib.pyplot as pt
import matplotlib.image as mimg
import cv2
import numpy as np
path='/content/drive/My Drive/Images'
all_img_paths= glob.glob(os.path.join(path,'*/*.ppm'))
images=[]
np.random.shuffle(all_img_paths)
label=[]
c=0
print(len(all_img_paths))
for im_path in all_img_paths:
  c=c+1
  #if (c==500):
    #break
  vd= im_path.split('/')
  clas=vd[-2]
  label.append(int(clas))
  im=mimg.imread(im_path)
  im_r=im[:,:,0]
  im_r=cv2.resize(im_r,(64,64))
  im_r.reshape(1,64,64)
  images.append(im_r)
  #print(c)
print(len(images))
#print(label)
data= np.array(images, dtype="float32")
data=data.reshape(data.shape[0],1,64,64)
print(data.shape)


from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K


K.set_image_dim_ordering("th")
seed=7
np.random.seed(seed)

x_train=data[:700,:]
x_test=data[700:,:]
print(len(x_train))
print(len(x_test))
label=np.array(label,dtype='float32')
y_train=label[:700]
y_test=label[700:]
print(len(y_train))
print(len(y_test))
x_train=x_train.reshape(x_train.shape[0],1,64,64).astype('float32')
x_test=x_test.reshape(x_test.shape[0],1,64,64).astype('float32')
x_train=x_train/255
x_test=x_test/255
y_train=np_utils.to_categorical(y_train)
y_test=np_utils.to_categorical(y_test)
num_classes=y_test.shape[1]
print(num_classes)
model=Sequential()

model.add(Conv2D(32,(5,5), input_shape=(1,64,64),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10, batch_size=200, verbose=2)
