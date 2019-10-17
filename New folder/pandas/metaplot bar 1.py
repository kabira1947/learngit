from matplotlib import pyplot as p,style as s

#s.use('ggplot')

p.bar([23,45,34,56,45,34,22,49],[32,34,24,56,4,6,4,56],label='book',color='g')
p.bar([1,2,3,4,5,6,8,9], [34,54,5,3,63,67,35,54],label='Students',color='m')

p.title('Result Report')
p.xlabel('Result')
p.ylabel('Numbers')


p.legend()
p.grid(True,color='w')

p.show()