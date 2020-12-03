# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:07:38 2020

@author: hariz
"""

import numpy as np
from skimage import filters
from skimage.measure import label, regionprops
from skimage import morphology
from skimage import draw
import matplotlib.pyplot as plt

def recognite(s):
    holes = count_holes(s)
    if holes == 2:
        hatches = count_hatch(s)
        if hatches == 1:
            return "B"
        else:
            return "8"
    elif holes == 1:
        ss = morphology.binary_closing(s)
        hatches = count_hatch(ss)
        if hatches == 2:
            return "A"
        elif hatches:
            if half_hole(s):
                return "P"
            else: 
                return "D"
        else:
            return "0"
    else:
        hatches = count_hatch(s)
        ratio = s.shape[0] / s.shape[1] 
        if (3 <= hatches <= 4 ):
            return "W"
        elif hatches == 2 and (0.9 < ratio < 1.1):
            return "*"
        elif hatches == 2:
            return "X"
        elif has_vline(s) and ratio > 1:
            return "1"
        elif (0.9 < ratio <= 1.1):
            return "*"
        elif (hatches == 1) and (1.9 < ratio < 2.16):
            return "/"
        elif (hatches == 1) and (ratio < 0.5):
            return "-"
    return ""


def count_holes(s):
    s = np.logical_not(s).astype('uint8')
    
    ss = np.ones((s.shape[0] + 2, s.shape[1] + 2))
    ss[1:-1, 1:-1] = s
    
    LBs = label(ss)
    LBs[LBs == 1] = 0
    
    return len(np.unique(LBs))-1

def half_hole(s):
    s = np.logical_not(s).astype('uint8')
    y = s.shape[0] // 3
    x = s.shape[1] // 3
    ss = s[y:-y, x:-x]
    if s[0, 0] in ss:
        return True
    else:
        return False

def count_hatch(s):
    up = s[0, :]
    upe = np.zeros(len(up) + 2)
    upe[1: -1] = up
    upe = np.abs(np.diff(upe))
    
    intervals = np.where(upe > 0)[0]
    points_up = []
    
    for p1, p2 in zip( intervals[::2], intervals[1::2]):
        points_up.append((p2+p1) // 2)
    
    down = s[-1, :]
    downe = np.zeros(len(down) + 2)
    downe[1: -1] = down
    downe = np.abs(np.diff(downe))
    
    intervals = np.where(downe > 0)[0]
    points_down = []
    
    for p1, p2 in zip( intervals[::2], intervals[1::2]):
        points_down.append((p2+p1) // 2)
    
    h = 0 
    for p1 in points_up:
        for p2 in points_down:
            line = draw.line(0, p1, s.shape[0] - 1, p2)
            if np.all(s[line] == 1):
                h += 1
    if (h == 0):
        h = has_vline(s)
    return h

def has_vline(s):
    line = np.sum(s, 0) // s.shape[0]
    return 1 in line
    



alphabet = plt.imread("symbols.png")

alphabet = np.mean(alphabet, 2)
thresh = filters.threshold_otsu(alphabet)

alphabet[alphabet < thresh] = 0
alphabet[alphabet >= thresh] = 1

b_alpha = np.zeros_like(alphabet)
b_alpha[alphabet < thresh] = 1
b_alpha[alphabet >= thresh] = 0

LB = label(alphabet)
props = regionprops(LB)

count_symbols = {}
symbols = {}
index = 0
indexes = []
for i in range(len(props)):
    s = props[index].image 
    sym = recognite(s)
    if count_symbols.get(sym):
        count_symbols[recognite(s)] = count_symbols[recognite(s)] + 1
    else:
        count_symbols[recognite(s)] = 1
    index += 1

recognized = 0
for key in count_symbols:
    recognized += count_symbols[key]
print("Распознаваемость:", recognized / index * 100)
