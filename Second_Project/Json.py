# -*- coding: utf-8 -*-
import json
import Tokenizer
import io

# Define data
data = {'Original_Text': 'Tokenizer.data'}

# Write JSON file
with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ':'), ensure_ascii=False)
    outfile.write(str_)

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

#print(data_loaded)
#print(data == data_loaded)