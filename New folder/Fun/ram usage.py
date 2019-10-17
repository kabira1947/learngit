import psutil
"""print("CPU percentage")
a=psutil.cpu_percent()
print("a:{0:2f}".format(a))
print()
#print(b)
#print(c)
#print(d)
print("CPU Status")
b=dict(psutil.cpu_stats()._asdict())
for v,i in b.items():
    print(v,"=>",i//1024**3,"GB")
    if "percent" in v:
        print(i,"%")

print()
print("CPU Virtual Images")
c=dict(psutil.virtual_memory()._asdict())
for p,q in c.items():
    print(p,"=>",q//1024**3,"GB")
"""
d1=(psutil.disk_usage("/").total//1024**3)
d2=(psutil.disk_usage('/').free//1024**3)
d3=(psutil.disk_usage('/').used//1024**3)
d4=(psutil.disk_usage('/').percent)
print("Total Space={0} GBs\nFree space= {1} GBs\nUsed space= {2} GBs\n"
      "Percentage of used space= {3}".format(d1,d2,d3,d4))
#for g,h in d.items():
 #   print(h,"=>",g//1024**3,"GB")