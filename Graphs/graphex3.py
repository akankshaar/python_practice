#import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
#d={"2001":1000,"2002":5000,"2003":4000,"2005":8000,"2006":3500,"2007":9000}
x=np.random.randn(2,3)
df=pd.DataFrame(x,index=[2001,2002])
print(df)
pt.hist(df)
pt.show()
