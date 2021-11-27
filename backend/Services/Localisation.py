import math
from math import sqrt

import Repository

def locate_closest_producer(product,client_localisation):
    dataset=Repository.fetch_producer()
    dataset=product_mask(product,dataset)
    shortest_dist =math.inf
    closest_producer=dataset[0]
    for producer in dataset:
        temp_dist=compute_distance(producer['coord'],client_localisation)
        if temp_dist <shortest_dist:
            shortest_dist=temp_dist
            closest_producer=producer
    return closest_producer

# take 2 json in argument, compute the distance between then
# to compute the distance between 2 point a smart monkey would use the following formula :
# √(xB−xA)^2+(yB−yA)^2
def compute_distance(coord_client,coord_producer):
    Xa = coord_client['longitude']
    Xb = coord_producer['longitude']
    Ya = coord_client['lattitude']
    Yb = coord_producer['lattitude']
    result = sqrt(((Xb-Xa)**2)-((Yb-Ya)**2))
    return result

# function that return only the producer that has the wanted product
def product_mask(product,producers):
    array_result=[]
    for producer in producers :
        if producer[product]:
            array_result.append(producer)
    return array_result