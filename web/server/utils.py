import json
import pickle
import numpy as np

__model = None
__columns = None
__locations = None
__atributes = None

def get_location_names():
    load_model_meta_data()
    return __locations

def get_estimated_price(total_sqft, bath, balcony, size_in_bhk, location):

    try:
        loc_index = __columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = size_in_bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)

def load_model_meta_data():
    print("loading model start...")

    global __model, __columns, __locations, __atributes

    with open("./web/model/columns.json", "r") as f:
        __columns = json.load(f)["data_columns"]
        __locations = __columns[4:]
        __atributes = __columns[:4]

    with open("./web/model/bangalore_home_price_model.pickle", "rb") as f:
        __model = pickle.load(f)


    print("loading model end...")

    return


if __name__ == "__main__":
    print("utils.py")
    load_model_meta_data()
    # print(get_location_names())
    print(get_estimated_price(1000,3,3,3,'1st Phase JP Nagar'))