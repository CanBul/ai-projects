from app import app
import pickle
import numpy as np

path = '/home/ai-projects/app'


def returnMovies(movieList):

    with open(path+"/contentBasedMovieList.p", "rb") as f:
        moviesWithRecommendation = pickle.load(f)
    
    returnList = []    

    length = len(movieList)
    

    for i, movie in enumerate(movieList):
        
        tempRecommendation = moviesWithRecommendation[movie][0:(54//(i+1))]
        
        
        for each in tempRecommendation:
            if each not in returnList and each not in movieList:
                returnList.append(each)

    np.random.shuffle(returnList)
    return returnList[:54]

def my_ids(pointtable):
    pointtable.sort(key = lambda x: x['rating'], reverse=True )

    mylist = []
    for each in pointtable:


        if each['id'] not in mylist:
            mylist.append(each['id'])

    return mylist



