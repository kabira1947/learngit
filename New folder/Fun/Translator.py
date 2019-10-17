import goslate

text=input("Enter the text: ")

gs=goslate.Goslate()
trans=gs.translate(text,'ru')

print(trans)