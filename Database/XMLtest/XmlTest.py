import os
from xml.etree import ElementTree

f = open("xml_file.xml")

parsef = ElementTree.parse(f)

CDs = parsef.findall("CD")

for c in CDs:
    #CD = c.find("CD")
    title = c.find("TITLE").text
    artist = c.find("ARTIST").text
    print('Album title: \"{}\", by artist:  \"{}\" '.format( title, artist))