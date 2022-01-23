import qrcode
import image
qr = qrcode.QRCode(
    version=15,  # 15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size=18,  # size of the box where qr code will be displayed
    border=5  # it is the white part of image -- border in all 4 side with white color
)
print('URL of which you want to make qr code :')
data = input()
print(' Name of the file')
rst = input()
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save(rst+".png")



