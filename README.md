# rgbValues
This script is used to extract RBG-values of every pixel in an image with the functionality to translate them into characters. Useful tool in for example CTF challenges.

```bash
usage: rgbValues.py [-h] [--show] [--rot ROT] [--translate]
                    file {red,green,blue,all}

positional arguments:
  file                  Filepath to image
  {red,green,blue,all}  Choose RGB attribute to analyse, all not available
                        with the --translate flag

optional arguments:
  -h, --help            show this help message and exit
  --show, -s            List RGB-values for all pixels
  --rot ROT, -r ROT     Declare a rot-conversion value
  --translate, -t       Covert values to characters
```
# Examples:
* Show the blue RGB-attribute value of all pixels
```bash
python rgbValues.py CheckOutThisFilter.png b -s	
```
* Show all RGB-attribute values of all pixels
```bash
python rgbValues.py CheckOutThisFilter.png all -s
```
* Translate the blue RGB-attribute value of all pixels into characters
```bash
python rgbValues.py CheckOutThisFilter.png b -t
```
* Translate the blue RGB-attribute value of all pixels into characters with a ROT-value of 13
```bash
python rgbValues.py CheckOutThisFilter.png b -t -r 13
```
