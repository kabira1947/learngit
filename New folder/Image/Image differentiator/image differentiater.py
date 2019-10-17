from PIL import Image,ImageChops
img1 = Image.open("1.jpg")
img2 = Image.open("2.jpg")
"""
differences= ImageChops.difference(img1,img2)
if differences.getbbox():
    differences.show()
"""
"""
screens=ImageChops.screen(img2,img1)
if screens.getbands():
    screens.show()
"""
"""
inverts= ImageChops.invert(img2)
inverts.show()
"""
"""
lighters= ImageChops.lighter(img1,img2)
lighters.show()

darkers= ImageChops.darker(img1,img2)
darkers.show()

adds=ImageChops.add(img1,img2)
adds.show()

substracts=ImageChops.subtract(img1,img2)
substracts.show()

blends= ImageChops.blend(img1,img2,4)
blends.show()
"""
