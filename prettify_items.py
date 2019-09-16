import json
from glob import glob

files = glob('items/*.jsonld')

for f in files:
    with open(f, 'r') as fo:
        data = json.load(fo)

    with open(f, 'w') as fo:
        json.dump(data, fo, indent=4)
