#!/usr/bin/env python2
from astropy.io import fits
import numpy as np
import focasifu as fi
import os

file = fi.filibdir+'dustposition1_2x2.fits'
if os.path.exists(file):
    print('Do you want to overwrite %s? :[y/n]'%file)
    key = raw_input()
    if key == 'y' or key =='Y':
        print('Removing')
        os.remove(file)

badpix1 = np.array([
[603, 129],
[603, 130],
[604, 129],
[605, 129],
[605, 128],
[517, 222],
[517, 223],
[518, 223],
[518, 222],
[519, 222],
[519, 223],
[520, 223],
[520, 222],
[521, 223],
[521, 224],
[522, 224],
[522, 223],
[523, 224],
[523, 225],
[524, 225],
[525, 225],
[525, 226],
[524, 226],
[524, 227],
[525, 227],
[523, 228],
[523, 229],
[523, 230],
[522, 230],
[522, 229],
[521, 229],
[521, 230],
[520, 230],
[524, 232],
[524, 233],
[524, 234],
[524, 235],
[524, 236],
[519, 270],
[520, 270],
[198, 224],
[198, 225],
[199, 225],
[119, 284],
[734, 312],
[734, 313],
[805, 423],
[806, 423],
[807, 423],
[808, 423],
[808, 424],
[807, 424],
[806, 424],
[805, 424],
[804, 424],
[837, 480],
[837, 481],
[837, 497],
[837, 498],
[838, 497],
[385, 411],
[374, 456],
[457, 561],
[458, 561],
[458, 562],
[264, 574],
[265, 574],
[270, 565],
[238, 909],
[238, 910],
[239, 910],
[239, 909],
[239, 908],
[240, 909],
[240, 910],
[241, 910],
[242, 910],
[242, 911],
[243, 911],
[243, 912],
[244, 912],
[244, 913],
[243, 913],
[242, 913],
[242, 914],
[242, 915],
[241, 914],
[240, 914],
[175, 934],
[174, 934],
[173, 934],
[173, 935],
[174, 935],
[175, 935],
[172, 935],
[397, 1190],
[397, 1191],
[397, 1192],
[397, 1193],
[471, 1209],
[470, 1209],
[267, 1344],
[268, 1344],
[269, 1344],
[269, 1343],
[268, 1343],
[267, 1343],
[195, 1449],
[196, 1449],
[196, 1448],
[195, 1448],
[246, 1486],
[735, 1573],
[736, 1573],
[737, 1573],
[737, 1572],
[736, 1572]
])

baddata = np.zeros((4210, 1024))
for i in range(badpix1.shape[0]):
    baddata[badpix1[i,1]-1, badpix1[i,0]-1] = 1

# Creating HDU data
outhdu = fits.PrimaryHDU(data=baddata)
outhdl = fits.HDUList([outhdu])
outhdl.writeto(file)
outhdl.close()

file = fi.filibdir+'dastposition2_2x2.fits'
if os.path.exists(file):
    print('Do you want to overwrite %s? :[y/n]'%file)
    key = raw_input()
    if key == 'y' or key =='Y':
        os.remove(file)

badpix2 = np.array([
[359, 140],
[360, 139],
[361, 138],
[361, 139],
[360, 138],
[360, 140],
[952, 413],
[952, 414],
[953, 414],
[953, 413],
[954, 413],
[954, 414],
[954, 415],
[955, 415],
[955, 414],
[956, 415],
[956, 416],
[721, 612],
[722, 611],
[722, 610],
[723, 609],
[723, 610],
[724, 610],
[725, 611],
[725, 610],
[726, 611],
[726, 612],
[727, 612],
[727, 611],
[757, 791],
[756, 791],
[984, 797],
[297, 851],
[297, 852],
[298, 850],
[298, 851],
[298, 852],
[298, 853],
[337, 934],
[337, 935],
[338, 934],
[338, 935],
[338, 936],
[338, 933],
[339, 934],
[339, 935],
[714, 1442],
[715, 1442],
[585, 1554],
[586, 1554],
[586, 1555],
[585, 1555],
[586, 1553],
[476, 1557],
[476, 1558],
[475, 1558],
[181, 1442],
[182, 1442],
[182, 1441],
[181, 1441],
[587, 1282],
[587, 1283],
[588, 1282],
[588, 1283],
[589, 1283],
[589, 1282],
[589, 1281],
[590, 1282],
[590, 1283],
[591, 1282],
[592, 1282],
[585, 1555],
[585, 1554],
[586, 1554],
[586, 1555],
[586, 1553],
[476, 1558],
[475, 1558],
[715, 1442],
[714, 1442],
[181, 1442],
[182, 1442],
[182, 1441],
[181, 1441]
])

baddata = np.zeros((4210, 1024))
for i in range(badpix2.shape[0]):
    baddata[badpix2[i,1]-1, badpix2[i,0]-1] = 1

# Creating HDU data
outhdu = fits.PrimaryHDU(data=baddata)
outhdl = fits.HDUList([outhdu])
outhdl.writeto(file)
outhdl.close()
