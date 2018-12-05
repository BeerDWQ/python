#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 3:04 PM
# @Author  : Beer
# @Site    : 
# @File    : selection_sort.py
# @Software: PyCharm

from __future__ import print_function

def selection_sort(collection):
	length = len(collection)
	for i in range(length - 1):
		least = i
		for k in range(i+1,length):
			if collection[k] < collection[least]:
				least = k
		collection[least],collection[i] = (collection[i],collection[least])
	return collection

if __name__ == '__main__':
	try:
		raw_input
	except NameError:
		raw_input = input
	user_input = raw_input('Enter numbers separated by a comma:\n').strip()
	unsorted = [int(item) for item in user_input.split(',')]
	print(selection_sort(unsorted))