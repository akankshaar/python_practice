import matplotlib.pyplot as pt
import numpy as np
x=[1000,2000,3000,4000]
y=[2,3,4,5]
pt.title("Houses Price In Delhi")
pt.xlabel("House Price ")
pt.ylabel("House Size")
#pt.plot(x,y,'r')
#pt.plot(x,y,'>')

pt.plot(x,y)
pt.show()
#pt.savefig("defaultchart.png",format="png")
