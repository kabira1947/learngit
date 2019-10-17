import os
#current working directory
current= os.getcwd()
print(current)


#create sub directory

#os.mkdir("filemanage1")

#os.mkdir("filemanage/book")
#os.makedirs("boook/college")

#os.chdir("filemanage/book")

#os.rmdir("filemanage/book")
#os.removedirs("filemanage")
#os.rename("filemanage","file manager")

for dirpath,dirnames,filenames in os.walk("."):
    print("current paths: ", dirpath)
    print("currnt directory: ",dirnames)
    print("files: ", filenames)
os.system("dir*.py")