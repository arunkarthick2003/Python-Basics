#code by Arunkarthick A K
#convert any image to black and white

from PIL import Image

def bw_image(input_image, output_image):
    img=Image.open(input_image)
    bw_img=img.convert('L')
    bw_img.save(output_image)

bw_image('demo.png', 'bw_demo.png')