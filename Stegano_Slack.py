# KAIS 2020 Competition
# fork KISA One-way Cyber Incident Response Training (Advanced) 
#

from optparse import OptionParser
from itertools import izip,cycle
import sys

parser = OptionParser()
parser.add_option('-K',dest='key_xor',help='(Optional) Cipher Key')
parser.add_option('-A',dest='adhoc',help='Output Image')
parser.add_option('-I',dest='input',help='Input Image')
parser.add_option('-S',dest='secret_text',help='Industrial Secret')
image,args = parser.parse_args(sys.argv)

if image.adhoc==None or image.input==None or image.secret_text==None:
        print parser.print_help()
        print ''
        sys.exit(2)
else:
    fi = open(image.input,'rb').read()
    if image.key_xor==None:
        x = ''.join(chr(ord(x)) for x in image.secret_text)
    else:
        x = ''.join(chr(ord(x)^ord(y)) \
                for (x,y) in izip(image.secret,cycle(image.key_xor)))
    fo = open(image.adhoc,'wb')
    fo.write(fi)
    fo.write(x)
    fo.close()
    print '\n         Path: {0}'.format(image.adhoc)
    print 'Steganography: {0}'.format(image.secret_text)
    print '       Offset: {0}\n'.format(hex(len(fi)))
