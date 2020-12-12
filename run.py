import os
from util import *
from tqdm import tqdm
from collections import Counter, defaultdict
from copy import deepcopy


class Partition(object):
    def __init__(self, data):
        self.users = set()
        self.items = set()
        self.train_UCM = set()
        self.valid_UCM = set()

        self.N = len(data)

        self.parseData(data)

    def parseData(self, data):
        # Shuffle the data
        random.shuffle(data)
        print('Creating User Set, Item Set')
        # Iterate and add users,items
        for u, i in tqdm(data):
            self.users.add(u)
            self.items.add(i)

        self.users = list(self.users)
        self.items = list(self.items)

        print('Creating Train Set for Positives')
        # Iterate and add train: games played by users
        for u, i in tqdm(data[:int(0.85 * self.N)]):
            self.train_UCM.add((u, i))

        print('Creating Validation Set for Positives')
        # Validation Set: Positives
        for u, i in tqdm(data[int(0.85 * self.N):]):
            self.valid_UCM.add(((u, i), 1))

        # print('Creating Validation Set for Negatives')
        # # Validation Set: Negatives
        # while len(self.valid_UCM) < int(self.N * .3):
        #     u, i = random.choice(self.users), random.choice(self.items)
        #     if (u, i) in self.train_UCM or ((u, i), 0) in self.valid_UCM:
        #         continue
        #     self.valid_UCM.add(((u, i), 0))


def topPopular(data):
    freqs = Counter()

    for _, item in data:
        freqs[item] += 1

    topFreqs = dict(sorted(freqs.items(), key=lambda item: -item[1]))
    topItems = list(topFreqs.keys())
    return topItems

def Jaccard(s1, s2):
    numer = len(s1.intersection(s2))
    denom = len(s1.union(s2))
    if denom > 0:
        return numer/denom
    return 0


# def jaccard_hr10(dataset):
#
#     valid_users = set()
#
#     for (u, _), _ in dataset.valid_UCM:
#         valid_users.add(u)
#
#     for (u, i), lbl in dataset.valid_UCM:


if __name__ == "__main__" :
    print(sys.argv[1])

    rawData = list()
    with open('data/Steam.txt') as fp:
        for item in fp.readlines():
            rawData.append(tuple(item.split()))

    data = Partition(rawData)
    if sys.argv[1] == 'all':

        interactions = defaultdict(set)
        topPop = topPopular(data.train_U2G)
        numFound = 0
        numUsers = len(data.users)

        for u, i in data.train_U2G:
            interactions[u].add(i)

        print('starting iteration')
        iteration = 0
        for user in data.users:
            iteration += 1
            if iteration % 1000 == 0: print(iteration)
            if len(interactions[user]) < 1:
                numUsers -= 1
                # print(len(interactions[user]), iteration)
                continue
            popped = random.sample(interactions[user], 1)[0]
            interactions[user].remove(popped)

            found = False
            search = 0
            _topPop = deepcopy(topPop)

            while search < 10 and len(_topPop) > 0:
                currItem = _topPop.pop(0)
                if currItem == popped:
                    found = True
                elif currItem in interactions[user]:
                    continue
                else:
                    search += 1

            if found:
                numFound += 1

        print('HR10 for Top Popular: ', numFound/numUsers)