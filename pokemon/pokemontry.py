# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 08:39:57 2019

@author: Rhea Arora
"""

import pandas

csv = pandas.read_csv('C:\\Users\\Rhea Arora\\Documents\\python\\pokemon\\pokemon.csv', sep=',', skipinitialspace=True)

csv_grass = csv[csv['Type 1'] == 'Grass']
csv_water = csv[csv['Type 1'] == 'Water']

csv_grass.to_csv('grass.csv', index=False, sep=',',mode="a")
csv_water.to_csv('water.csv', index=False, sep=',',mode="a")
print("File stored")
print(type(csv_grass))