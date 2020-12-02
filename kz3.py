# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 14:50:14 2020

@author: Юрий
"""

import numpy as np

image = np.load("ps.npy.txt").astype("uint8")

struct_1 = np.array([[1,1,0,0,1,1],
                     [1,1,0,0,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1]])

struct_2 = np.rot90(struct_1)
struct_3 = np.rot90(struct_2)
struct_4 = np.rot90(struct_3)

struct_5 = np.array([[1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1],
                     [1,1,1,1,1,1]])

struct_6 = np.rot90(struct_5)

def count_arrs(image, structs):
    counts = [0]*len(structs)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for i, struct in enumerate(structs):
                w = struct.shape[0]
                h = struct.shape[1]
                if ((y + w <= image.shape[0]) and (x + h <= image.shape[1])):
                    if (image[y:y+w, x:x+h] == struct).all():
                        counts[i] += 1
    return counts       

structs = [struct_1, struct_2, struct_3, struct_4, struct_5, struct_6]
counts = count_arrs(image, structs)

print("Объекта тип 1: "+str(counts[0]))
print("Объекта тип 2: "+str(counts[1]))
print("Объекта тип 3: "+str(counts[2]))
print("Объекта тип 4: "+str(counts[3]))
print("Объекта тип 5: "+str(counts[4]))
print("Объекта тип 6: "+str(counts[5]))
