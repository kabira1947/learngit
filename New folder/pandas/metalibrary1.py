import pandas as pd

from matplotlib import pyplot as p

y=[2,34,5,67,4,3]
x=[2001,2002,2003,2004,2005,2006]

p.plot(x,y)
#p.plot(y,x)
p.title('data')
p.xlabel('food corps')
p.ylabel('years')
p.show()
