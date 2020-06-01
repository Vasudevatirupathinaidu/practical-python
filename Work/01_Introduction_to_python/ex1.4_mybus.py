'''Exercise 1.4: Where is My Bus? -
Try something more advanced and type these statements to find out how long people waiting on the corner of Clark street and Balmoral in Chicago will have to wait for the next northbound CTA #22 bus:'''

# from urllib import request
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')

from xml.etree.ElementTree import parse
doc = parse(u)

for pt in doc.findall('.//pt'):
    print(pt.text)