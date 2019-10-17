from matplotlib import pyplot as p,style as s

s.use('ggplot')
x=[23,45,345,56,45,34,22]

y=[1,22,34,46,35,66,27,98]

p.plot(x,'b',label='result',linewidth=5)
p.plot(y,'g',label='numbers',linewidth=1)

p.title('Result Report')
p.xlabel('Result')
p.ylabel('Numbers')


p.legend()
p.grid(True,color='w')

p.show()
