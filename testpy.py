
# -*- coding: utf-8 -*-
import json

# Make it work for Python 2+3 and with Unicode
import io, codecs, string
from pprint import pprint

# Define data
data = {'a list': [1, 42, 3.141, 1337, 'help', 'hhh'],
        'a string': 'bla',
        'another dict': {'foo': 'bar',
                         'key': 'value',
                         'the answer': 42}}
'''with open('test.json') as data_file:
	print('hieeee.....')
	print(data_file)
	d = json.load(data_file)'''
enc = codecs.encode('STMzMDAzMzpTdW1hbkAxNjc=', 'rot_13')
print(enc)
print(codecs.decode(enc, 'rot13'))

				 
# Write JSON file
'''with io.open('test.json', 'a+', encoding='utf8') as outfile:
	#d = json.load(outfile)
	str_ = json.dumps(data,indent=4,sort_keys=True,separators=(',', ': '),ensure_ascii=False);
	#d.append(str_)
	outfile.write(str_)

# Read JSON file
with open('test.json') as data_file:
	#data_loaded = {}
	
	data_loaded = data_file.read();
	#data_loaded.append(data);
	
print(data == data_loaded)
print(data_loaded)'''