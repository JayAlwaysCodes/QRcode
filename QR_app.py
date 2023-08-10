import qrcode
from PIL import Image

data = "https://github.com/JayAlwaysCodes?tab=repositories"

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

Image = qr.make_image(fill="black", back_color="white")

Image.save("qr_code1.png")
Image.open("qr_code1.png")

print('QR code has been generated.')