# import modules
import qrcode
from PIL import Image

# taking the image which user wants in the QR code center
# Note that the image must be saved in the local directory, as apparently pillow image is only able open the images in the Local Drive
Logo_link = input("Enter the link to the image - ") 

logo = Image.open(Logo_link)

# taking base width, can be changed later on
basewidth = 100

# adjusting image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# taking url or text
url = input("Enter the link you want to generate the QR code of - ")

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

QRcolor = input("Enter the colour of the QR code that you want - ")
QRcolor = QRcolor.lower()

# adding color to the QR code
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')

# setting the size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# saving the QR code generated
QRimg.save('QR_Code.png')

print('QR code generated!')