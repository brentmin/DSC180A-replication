
import gzip
import shutil
import urllib.request


def import_data(dataset_name):
    for name in dataset_name:
        print('Getting '+name)
        if name == 'reviews':
            url = 'http://cseweb.ucsd.edu/~wckang/steam_reviews.json.gz'
            destination_path = 'data/raw/steam_reviews.json.gz'
            final_filepath = 'data/raw/steam_reviews.json'
        elif name == 'games':
            url = 'http://cseweb.ucsd.edu/~wckang/steam_games.json.gz'
            destination_path = 'data/raw/steam_games.json.gz'
            final_filepath = 'data/raw/steam_games.json'
        else:
            url = ''
            destination_path = ''
            final_filepath = ''
        urllib.request.urlretrieve(url, destination_path)

        with gzip.open(destination_path, 'rb') as f_in:
            with open(final_filepath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

