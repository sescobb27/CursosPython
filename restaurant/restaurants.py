#!/usr/bin/env python3.3

# FULLPATH = '/home/simon/Documents/python/restaurants_small.txt'
FILENAME = "restaurants_small.txt"

def recomend(file, price, cuisines_list):
	name_to_rating, price_to_names, cuisines_to_names = read_restaurants(file)

	names_matching_price = price_to_names[price]

	names_final = filter_by_cuisine(names_matching_price, cuisines_to_names, cuisines_list)

	result = build_rating_list(name_to_rating, names_final)

	return result


def read_restaurants(file):
	name_to_rating = {}
	price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
	cuisines_to_names = {}
	text = open(file,'r')
	line = readline(text)
	while line != '':
		temp = readline(text)
		temp = temp[:len(temp)-1]
		name_to_rating[line] = int(temp)
		price_to_names[readline(text)].append(line)
		cuisines_list = read_cuisine(readline(text))
		for cuisine in cuisines_list:
			if cuisines_to_names.__contains__(cuisine):
				cuisines_to_names[cuisine].append(line)
			else:
				cuisines_to_names[cuisine] = [line]
		text.readline()
		line = readline(text)
	text.close()
	return(name_to_rating, price_to_names, cuisines_to_names)

def filter_by_cuisine(names_matching_price, cuisines_to_names, cuisines_list):
	names_cuisine_matches = []
	result = []
	for cuisine in cuisines_list:
		for cuisine_, name in cuisines_to_names.items():
			if cuisine_ == cuisine:
				for rest_name in name:
					names_cuisine_matches.append(rest_name)

	for name in names_matching_price:
		for name_ in names_cuisine_matches:
			if name == name_:
				result.append(name)
	return result

def build_rating_list(name_to_rating, names_final):
	result = []
	for name, rate in name_to_rating.items():
		for name_ in names_final:
			if name_ == name:
				temp = []
				temp.append(rate)
				temp.append(name)
				result.append(temp)
	result.sort(reverse=True)
	return result

def read_cuisine(str):
	return str.split(',')

def readline(text):
	return text.readline().rstrip()