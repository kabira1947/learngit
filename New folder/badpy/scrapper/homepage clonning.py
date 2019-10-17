import urllib2
import sys
import io

def clone():
   url= input("Enter the url: ")
   response= urllib3.urlopen(url)
   resource= response.read()

   with io.FileIO('website-index.html','w')as file:
       file.write(resource)
