import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


data = 'Don\'t subscribe'

img = qrcode.make(data)

img.save('myqrcode.png')

img = Image.open('/Users/gareth/Documents/PyCharm/QRCode/myqrcode.png')

result = decode(img)

print(result)