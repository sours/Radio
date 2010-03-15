#! /usr/bin/python

import Image,ImageDraw,ImageFont
import radiostats
import cStringIO
import sys

fill = '#00FF00' #"#e6d6ca"
print "Content-Type: image/png \n"
fontsize = 16
txtoffset = fontsize + 4
offsetx = 100
offsety = 50

image = Image.open("nncr.png")
font = ImageFont.truetype("GOTHIC.TTF",fontsize)
draw = ImageDraw.Draw(image)
text = ( "Now playing: " + radiostats.m.CurrentlyPlaying)
text1 =	("DJ: " + radiostats.m.Description)
text2 = (radiostats.m.CurrentListeners + " Listeners")
draw.text((offsetx,offsety),text,font=font,fill=fill )
draw.text((4,120),text1,font=font,fill=fill )
draw.text((offsetx,txtoffset+offsety),text2,font=font,fill=fill)

"""
text = "Radio Currently disabled"
draw.text((offsetx,offsety),text,font=font,fill=fill )
"""
output = cStringIO.StringIO()
image.save(output,"png")
sys.stdout.write(output.getvalue())



