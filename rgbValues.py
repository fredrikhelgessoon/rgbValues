import sys
from PIL import Image
import argparse

rot_value = 0 #Default value
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Filepath to image")
parser.add_argument("color", choices=["r", "g", "b", "all"], help="Choose RGB attribute to analyse, all not available with the --translate flag")
parser.add_argument("--show", "-s", help="List RGB-values for all pixels", action="store_true")
parser.add_argument("--rot", "-r", type=int, help="Declare a rot-conversion value")
parser.add_argument("--translate", "-t", help="Covert values to characters", action="store_true")
args = parser.parse_args()

#E.g RITSEC CTF 2018 required a rot_value of 13.
if(args.rot):
	rot_value = args.rot

#Open image
img = Image.open(args.file).convert('RGB')
#Determine imagesize
w, h = img.size
values = []
#Iterate through all pixels in image
for y in range(0, h):
    for x in range(0, w):
        red, green, blue = img.getpixel((x, y))
	if args.color== 'r':
		values.append(red)
	elif args.color == 'g':
		values.append(green)
	elif args.color == 'b':	
		values.append(blue)
	elif args.color == 'all':
		values.append(str(red) + "," + str(green) + ", " + str(blue))
#Assembly flag by converting all decimal RGB-values to characters
if(args.show):
	for decimal in values:
		print "[" + str(decimal) + "]"

if(args.translate and args.color != 'all'):
	flag = ''
	for decimal in values:
    		flag += chr(decimal - rot_value)
	print flag


