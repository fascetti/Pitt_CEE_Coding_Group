from PIL import Image, ImageDraw, ImageFont

def translate(i):
    #density = list('Ñ@#W$9876543210?!abc;:+=-,._ ')
    density = list('@%#*+=-:. ')
    n_char = len(density)
    return density[int(n_char/256*i)]

# my_text_file = open('ART.txt', 'w')

my_img = Image.open('Tsunami.jpeg').convert('RGB')
width, height = my_img.size
ratio = 0.1

my_img = my_img.resize((int(ratio*width),int(ratio*height)), Image.Resampling.LANCZOS)
width, height = my_img.size

my_ascii_art = Image.new(mode="RGB", size=(6*width, 6*height), color="white")
d1 = ImageDraw.Draw(my_ascii_art)

for i in range(height):
    for j in range(width):
        r, g, b = my_img.getpixel((j, i))
        # intensity = int((r + g + b)/3)
        intensity = int(0.299 * r + 0.587 * g + 0.114 * b)
        # my_img.putpixel((j, i), (intensity, intensity, intensity))
        #my_text_file.write(translate(intensity))
        myFont = ImageFont.truetype("Courier.ttc", 10)
        #bbox = myFont.getbbox("a")
        #print(bbox)
        d1.text((6*j, 6*i), translate(intensity), font=myFont, fill=(intensity, intensity, intensity))
    #my_text_file.write('\n')

my_ascii_art.save("my_ascii_art.png")