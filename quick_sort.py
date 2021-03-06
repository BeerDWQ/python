
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 5:03 PM
# @Author  : Beer
# @Site    : 
# @File    : quick_sort.py
# @Software: PyCharm

from __future__ import print_function

def quick_sort(ARRAY):
	ARRAY_LENGTH = len(ARRAY)
	if(ARRAY_LENGTH <= 1):
		return ARRAY
	else:
		PIVOT = ARRAY[0]
		GREATER = [element for element in ARRAY[1:] if element > PIVOT]
		LESSER = [element for element in ARRAY[1:] if element <= PIVOT]
		return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)

if __name__ == '__main__':
	try:
		raw_input
	except NameError:
		raw_input = input
	user_input = raw_input('Enter numbers separated by a comma:\n').strip()
	unstord = [int(item) for item in user_input.split(',')]
	print( quick_sort(unstord) )