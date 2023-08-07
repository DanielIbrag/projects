import pyqrcode 
from pyqrcode import QRCode 
  
# String which represent the QR code 
s = "https://danielibrag.github.io/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the png file naming "myqr.png" 
url.svg("mywebsite.svg", scale = 8) 