import json5
import sys
sys.path.append(".")
from utils import jsonDumps
from utils import updateConfig

def before(src, dst):
    key_list = ['version', 'desp']
    for key in src:
        if key in dst:
            if key in key_list:
                src[key] = dst[key]


config = json5.load(open(sys.argv[1], 'r', encoding='utf-8'))
oldconfig = json5.load(open(sys.argv[2], 'r', encoding='utf-8'))

before(oldconfig, config)

data = updateConfig(oldconfig, config)

with open(sys.argv[1], 'w', encoding='utf-8') as f:
    f.write(jsonDumps(data))
