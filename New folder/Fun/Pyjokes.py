import pyjokes
import re
a = str(pyjokes.get_jokes())
re.split(r"[|]|;|}|\|{|,|", a)

#b= a.split("[]"),


#for i in b:
 #  print(i)
