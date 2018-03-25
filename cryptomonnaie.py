#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from cryptocompy import coin
from cryptocompy import price
import os
import sys

def get_crypto_full_name(cryptomonnaie):

	list_names = []
	for key, value in cryptomonnaie.items():
		list_names.append(value.get('FullName'))
	return list_names

def get_crypto_name(cryptomonnaie):

	list_names = []
	for key, value in cryptomonnaie.items():
		list_names.append(value.get('CoinName'))
	return list_names

def find_key(d, value):

	for k,v in d.items():
		if isinstance(v, dict):
			p = find_key(v, value)
			if p:
				return [k] + p
		elif v == value:
			return [k]

def get_price(cryptocurrency, currency):
	prices_crypto = price.get_current_price(cryptocurrency, [currency], e='all', try_conversion=True, full=False, format='raw')
	return prices_crypto.get(cryptocurrency).get(currency)

def print_price(cryptocurrency, price, currency):
	print('\t1 ' + cryptocurrency + ' = ' + str(price) + symbols.get(currency))
	print('\n')

def print_list(list):

	if len(list) % 2 != 0:
		list.append(" ")

	split = int(len(list) / 2)
	l1 = list[0:split]
	l2 = list[split:]

	for key, value in zip(l1, l2):
		print("{0:<40s} {1}".format(key, value))

def clear():

	os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("\t*****************************")
print("\t*\tCRYPTOCURRENCY\t    *")
print("\t*****************************")

cryptocurrencies = coin.get_coin_list(coins='all')
cryptocurrencies_names = get_crypto_name(cryptocurrencies)
cryptocurrencies_acronym = cryptocurrencies.keys()
symbols = {'USD': '$', 'EUR': '€'}

while True:

	print("\n - Entrez le nom ou l'acronym de la cryptomonnaie que vous voulez")
	print("   (ex : 'BTC' or 'Bitcoin')")
	print(" - Enter 'list' to list cryptocurrency")
	print(" - Enter 'exit' to exit")

	input_cryptocurrency = input("> ")

	if input_cryptocurrency == 'list':
		cryptocurrencies_fullname = list(get_crypto_full_name(cryptocurrencies))
		print_list(cryptocurrencies_fullname)

	elif input_cryptocurrency == 'exit':
		sys.exit(0)

	else:

		if input_cryptocurrency.upper() in cryptocurrencies_acronym or input_cryptocurrency in cryptocurrencies_names:

			if input_cryptocurrency in cryptocurrencies_names:
				input_cryptocurrency = find_key(cryptocurrencies, input_cryptocurrency)[0]


			prix_dollar = get_price(input_cryptocurrency, 'USD')
			print_price(input_cryptocurrency, prix_dollar, 'USD')

		else:
			sys.stderr.write("Error : Undefined CryptoCurrency")
			sys.exit(1)
