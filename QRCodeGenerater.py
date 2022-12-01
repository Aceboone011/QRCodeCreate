# install pypng library
# install  pyqrcode

#import lib
import pyqrcode

# create qrcode method
def  qrcode():

#ask for user input ane create qr code  *string
    x = pyqrcode.create(input())

#save qrcode in a png file and scale or size the image.
    x.png('qrcode.png',  scale = 6)

    print('QR code  generated')

#initiate program and call method qrcode

if __name__  == '__main__' :
    qrcode( )
    
