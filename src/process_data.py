#This was derived form the original processing script in references/SASRec/data/DataProcessing.py
import os
import gzip
from collections import defaultdict
from datetime import datetime

def parse(path):
    g = gzip.open(path, 'r')
    for l in g:
        yield eval(l)

def process_data(dataset_name, dataset_path, userId_column, productId_column, rating_column, date_column, temp_output_path, output_path):

    os.makedirs(os.path.dirname(temp_output_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    countU = defaultdict(lambda: 0)
    countP = defaultdict(lambda: 0)
    line = 0

    f = open(temp_output_path + 'reviews_' + dataset_name + '.txt', 'w')
    for l in parse(dataset_path):
        line += 1
        try:
            f.write(" ".join([l[userId_column], l[productId_column], str(l[rating_column]), str(datetime.strptime(l[date_column], '%Y-%m-%d').date())]) + ' \n')
        except:
            continue
        asin = l[productId_column]
        rev = l[userId_column]
        time = datetime.strptime(l[date_column], '%Y-%m-%d').date()
        countU[rev] += 1
        countP[asin] += 1

    f.close()

    usermap = dict()
    usernum = 0
    itemmap = dict()
    itemnum = 0
    User = dict()
    for l in parse(dataset_path):
        line += 1
        asin = l[productId_column]
        rev = l[userId_column]
        time = datetime.strptime(l[date_column], '%Y-%m-%d').date()
        if countU[rev] < 5 or countP[asin] < 5:
            continue

        if rev in usermap:
            userid = usermap[rev]
        else:
            usernum += 1
            userid = usernum
            usermap[rev] = userid
            User[userid] = []
        if asin in itemmap:
            itemid = itemmap[asin]
        else:
            itemnum += 1
            itemid = itemnum
            itemmap[asin] = itemid
        User[userid].append([time, itemid])
    # sort reviews in User according to time

    for userid in User.keys():
        User[userid].sort(key=lambda x: x[0])

    f = open(output_path+dataset_name+'.txt', 'w')
    for user in User.keys():
        for i in User[user]:
            f.write('%d %d\n' % (user, i[1]))
    f.close()
