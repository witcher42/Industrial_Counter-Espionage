# KAIS 2020 Competition
# Usage:
#       pip install Pillow
#

from optparse import OptionParser
from PIL import Image
import sys

parser = OptionParser()
parser.add_option('-N',dest='neutral_image',help='Input Image')
parser.add_option('-I',dest='inject',help='(Optional) Dummy Image')
parser.add_option('-S',dest='skewed',help='XOR Image')
parser.add_option('-C',dest='coming_out',help='Output Image')
image,args = parser.parse_args(sys.argv)

if image.neutral_image==None or image.skewed==None \
        or image.coming_out==None:
    print parser.print_help()
    print ''
    sys.exit(2)

if image.inject==None:
    image.inject = image.neutral_image

def XOR (pic1, pic2):
    for y in range(pic1.size[1]):
        for x in range(pic1.size[0]):
            pixel1 = pic1.getpixel((x,y))
            pixel2 = pic2.getpixel((x,y))
            newpixel = []
            for p in range(len(pixel1[:3])):
                newpixel.append(pixel1[p] ^ pixel2[p])
            newpixel = tuple(newpixel)
            temp.putpixel((x,y),newpixel)

print '\nProcessing...'
pic1 = Image.open(image.neutral_image)
pic2 = Image.open(image.inject)
pic2 = pic2.resize(pic1.size)
temp = Image.new('RGB',pic1.size)
XOR(pic1, pic2)
temp.save(image.skewed)
print '\nXOR Image Created!\n{0}'.format(image.skewed)
print '\nOriginal Image Creating...'
pic3 = Image.open(image.skewed)
pic3 = pic3.resize(pic2.size)
temp = Image.new('RGB', pic2.size)
XOR(pic2, pic3)
temp.save(image.coming_out)
print '\nFinish...!\n{0}'.format(image.coming_out)
print ''
