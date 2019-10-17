from zipfile import *

z=ZipFile('test.zip','w',ZIP_DEFLATED)
z.write('hello.txt')

z.extractall()
z.close()