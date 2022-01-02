import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimg
from sklearn.cluster import KMeans

#no. of cluster
km=KMeans(2)

# path of flower
x=mimg.imread('./f6.jpg')

r=x[:,:,0]
r1=r.reshape(-1,1)

g=x[:,:,1]
g1=g.reshape(-1,1)

b=x[:,:,2]
b1=b.reshape(-1,1)

a=np.concatenate((r1,g1,b1),axis=1)
km=km.fit(a)
newimg=km.labels_.reshape(x.shape[0], x.shape[1])


c1=np.zeros((x.shape[0], x.shape[1],3))
c2=np.zeros((x.shape[0], x.shape[1],3))
c3=np.zeros((x.shape[0], x.shape[1],3))
c4=np.zeros((x.shape[0], x.shape[1],3))
c5=np.zeros((x.shape[0], x.shape[1],3))
c6=np.zeros((x.shape[0], x.shape[1],3))

for k in range(0,3):
    for i in range (0,x.shape[0]):
        for j in range(0,x.shape[1]):
            if newimg[i,j]==0:
                c1[i,j,k]=x[i,j,k]
            if newimg[i,j]==1:
                c2[i,j,k]=x[i,j,k]
            if newimg[i,j]==2:
                c3[i,j,k]=x[i,j,k]
            if newimg[i,j]==3:
                c4[i,j,k]=x[i,j,k]
            if newimg[i,j]==4:
                c5[i,j,k]=x[i,j,k]
            if newimg[i,j]==5:
                c6[i,j,k]=x[i,j,k]
c1= c1.astype(np.uint8)
c2= c2.astype(np.uint8)
c3= c3.astype(np.uint8)
c4= c4.astype(np.uint8)
c5= c5.astype(np.uint8)
c6= c6.astype(np.uint8)
plt.figure(1)
plt.subplot(2,3,1)
plt.imshow(c1)
p1=(np.count_nonzero(c1)/(x.shape[0]*x.shape[1]*3))*100
plt.title('%d'%p1)

plt.subplot(2,3,2)
p2=(np.count_nonzero(c2)/(x.shape[0]*x.shape[1]*3))*100
plt.title('%d'%p2)
plt.imshow(c2)

plt.subplot(2,3,3)
p3=(np.count_nonzero(c3)/(x.shape[0]*x.shape[1]*3))*100
plt.title('%d'%p3)
plt.imshow(c3)

plt.subplot(2,3,4)
p4=(np.count_nonzero(c4)/(x.shape[0]*x.shape[1]*3))*100
plt.title('%d'%p4)
plt.imshow(c4)

plt.subplot(2,3,5)
p5=(np.count_nonzero(c5)/(x.shape[0]*x.shape[1]*3))*100
plt.title('%d'%p5)
plt.imshow(c5)

plt.subplot(2,3,6)
p6=(np.count_nonzero(c6)/(x.shape[0]*x.shape[1]*3))*100
plt.title('%d'%p6)
plt.imshow(c6)
plt.show()


cn=input('enter the cluster no.')

color=[]
for i in range(0,3):
    col=int(input('value of rgb ='))
    color.append(col)

a=a.reshape(x.shape[0], x.shape[1],3)
a=a.astype(int)
#c=[220,220,220]
for i in range (0,x.shape[0]-100):
    for j in range(0,x.shape[1]-100):
        if newimg[i,j]==int(cn)-1:
            c=[a[i,j,0],a[i,j,1],a[i,j,2]]
            #print('gfvagysdjj')
            break


b=np.zeros((x.shape[0], x.shape[1],3))

for k in range(0,3):
    for i in range (0,x.shape[0]):
        for j in range(0,x.shape[1]):
            if newimg[i,j]==int(cn)-1:
                b[i,j,k]=a[i,j,k]-c[k]

for k in range(0,3):
    for i in range (0,x.shape[0]):
        for j in range(0,x.shape[1]):
            if newimg[i,j]==int(cn)-1:
                a[i,j,k]=color[k]+b[i,j,k]
            if a[i,j,k]>255:
                a[i,j,k]=255
            if a[i,j,k]<0:
                a[i,j,k]=0



plt.subplot(1,2,2)
a= a.astype(np.uint8)
plt.imshow(a)

plt.subplot(1,2,1)
plt.imshow(x)
plt.show()
