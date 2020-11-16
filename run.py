import sys
import json
import os
import pandas

sys.path.insert(0, 'src')

from import_data import import_data
from process_data import process_data,parse

def main(targets):

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        import_data(**data_cfg)
    if 'process' in targets:
        with open('config/process-params.json') as fh:
            process_cfg = json.load(fh)
        process_data(**process_cfg)
        


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)