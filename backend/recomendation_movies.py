import pandas as pd
import os
from surprise import Dataset, KNNBasic, Reader, accuracy, get_dataset_dir
from surprise.model_selection import PredefinedKFold,cross_validate
import io
from collections import defaultdict


__all__ = ['get_movies', 'user_set', 'get_neighbors', 'get_rmse']



database = pd.read_csv('ml-100k/u1.base.csv')
user_set = set(database.user_id)
item_set = set(database.item_id)



files = os.path.expanduser('ml-100k/')


reader = Reader('ml-100k')


train_file = files + 'u1.base'
test_file = files + 'u1.test'


folds_files = [(train_file, test_file)]

data = Dataset.load_from_folds(folds_files, reader=reader)

pkf = PredefinedKFold()


algo = KNNBasic()


for trainset, testset in pkf.split(data):
    algo.fit(trainset)
    predictions = algo.test(testset)
 

def get_top_n(predictions, n=10):
    
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n


top_n = get_top_n(predictions, 5)



def read_item_names():
    file_name = 'ml-100k/u.item'
    rid_to_name = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = line[1]

    return rid_to_name


rid_to_item = read_item_names()


def get_movies(uid):
    lista = []
    valor = 0
    for i in top_n.get(unicode(uid)):
         valor +=1
         lista.append(str(valor)+" - "+str(rid_to_item[i[0]]))
    return lista

def read_user_info():
    file_name =  'ml-100k/u.user'
    rid_to_name = {}
    with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
        for line in f:
            line = line.split('|')
            rid_to_name[line[0]] = (line[1],line[2],line[3])

    return rid_to_name

rid_to_name = read_user_info()

def get_neighbors(uid):
    inner_uid = algo.trainset.to_inner_uid(uid)
    neighbors = algo.get_neighbors(inner_uid, k=3)
    lista = []
    for i in neighbors:
       	lista.append("id: "+ str(algo.trainset.to_raw_uid(i))+' Age: '+str(rid_to_name[unicode(i)][0])+' Gender: '+str(rid_to_name[unicode(i)][1])+' Occupation: '+ str(rid_to_name[unicode(i)][2]))
    return lista

def get_rmse():
    return str("%.3f" % accuracy.rmse(predictions, verbose=True))
       
	

