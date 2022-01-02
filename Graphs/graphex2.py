import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
df=pd.DataFrame(np.random.randn(40,4),columns=['a','b','c','d'])
colors=np.random.randn(40)
print(df)
print(colors)
df.plot.scatter(x='a',y='b',s=(np.random.randn(40))*1000,c=colors)

pt.show()

