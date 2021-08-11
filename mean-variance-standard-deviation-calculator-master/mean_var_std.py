import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    convert_list = np.array(list).reshape(3, 3) #convert the list into a 3 x 3 Numpy array
    calculations = {
        i: [f(convert_list, axis = x).tolist() #numpy array to list
            for x in [0, 1, None]] #axis
            for (i, f) 
            in zip(["mean", "variance", "standard deviation", "max", "min", "sum"],
            [np.mean, np.var, np.std, np.max, np.min, np.sum])
        }

    return calculations
