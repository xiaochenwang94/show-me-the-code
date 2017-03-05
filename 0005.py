from PIL import Image

def size2Iphone5(img):
    x, y = img.size
    # 1136 * 640
    out = img.resize((1136,640),Image.ANTIALIAS)
    out.save('result.jpg','JPEG')

if __name__ == '__main__':
    filename = 'Harden.jpg'
    img = Image.open(filename)
    size2Iphone5(img)