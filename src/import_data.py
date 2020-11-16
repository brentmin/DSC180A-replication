import os
import gzip
import shutil
import urllib.request


def import_data(dataset_name, output_path):

    # If folder isn't there, create it
    filename = output_path
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    for name in dataset_name:

        print('Getting '+name)
        
        if name == 'reviews':
            url = 'http://cseweb.ucsd.edu/~wckang/steam_reviews.json.gz'
            destination_path = output_path+'steam_reviews.json.gz'
            final_filepath = output_path+'steam_reviews.json'
        elif name == 'games':
            url = 'http://cseweb.ucsd.edu/~wckang/steam_games.json.gz'
            destination_path = output_path+'steam_games.json.gz'
            final_filepath = output_path+'steam_games.json'
        else:
            url = ''
            destination_path = ''
            final_filepath = ''

        urllib.request.urlretrieve(url, destination_path)

        with gzip.open(destination_path, 'rb') as f_in:
            with open(final_filepath, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

