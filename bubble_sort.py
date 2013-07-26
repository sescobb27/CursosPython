#!/usr/bin/env python3.3
def bubble_sort(list):
	end = len(list)-1
	while end != 0:
		for i in range(end):
			if list[i] > list[i+1]:
				list[i],list[i+1] = list[i+1],list[i]
		end = end - 1

def selection_sort(list):
	end = len(list)
	for i in range(end):
		smaller_index = i
		for j in range(i+1,end):
			if list[j] < list[smaller_index]:
				smaller_index = j
		list[smaller_index],list[i] = list[i],list[smaller_index]

def insertion_sort(list):
	end = len(list)
	for i in range(end):
		value = list[i]
		j = i
		while j != 0 and list[j-1] > value:
			list[j] = list[j-1]
			j = j -1
		list[j] = value


if __name__ == '__main__':
	import doctest
	doctest.testmod()