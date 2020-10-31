import sys
import json
import os
import pandas

cwd = os.getcwd()
baseline_path = os.path.join(cwd, 'src', 'baselines')
sys.path.append(baseline_path)

data_path = os.path.join(cwd, 'data', 'raw')
sys.path.append(data_path)

cwd = os.getcwd()

def main(targets):

    if 'data' in targets:
        with open('data/raw/steam_games.json') as steam:
            print('Load in dataset')
            #steam_str = steam.read()
            #steam_str = steam_str.replace("\'", "\"")
            df = json.load(steam)
            print('Done loading dataset')
        print('Do dataset stuff here')


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)