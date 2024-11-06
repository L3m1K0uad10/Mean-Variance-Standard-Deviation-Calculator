import numpy as np


def get_mean(num_array):
    """ 
    get mean along both axes and for the flattened matrix.
    """

    mean_x_axis = num_array.mean(axis = 0)
    mean_y_axis = num_array.mean(axis = 1) 
    flatten_ = num_array.mean()

    return [mean_x_axis.tolist(), mean_y_axis.tolist(), flatten_.item()]

def get_variance(num_array):
    """ 
    get variance along both axes and for the flattened matrix.
    """
    
    var_x_axis = num_array.var(axis = 0)
    var_y_axis = num_array.var(axis = 1) 
    flatten_ = num_array.var()

    return [var_x_axis.tolist(), var_y_axis.tolist(), flatten_.item()]

def get_standard_deviation(num_array):
    """ 
    get standard deviation along both axes and for the flattened matrix.
    """

    std_x_axis = num_array.std(axis = 0)
    std_y_axis = num_array.std(axis = 1) 
    flatten_ = num_array.std()

    return [std_x_axis.tolist(), std_y_axis.tolist(), flatten_.item()]

def get_max(num_array):
    """ 
    get max along both axes and for the flattened matrix.
    """

    max_x_axis = num_array.max(axis = 0)
    max_y_axis = num_array.max(axis = 1) 
    flatten_ = num_array.max()

    return [max_x_axis.tolist(), max_y_axis.tolist(), flatten_.item()]

def get_min(num_array):
    """ 
    get min along both axes and for the flattened matrix.
    """

    min_x_axis = num_array.min(axis = 0)
    min_y_axis = num_array.min(axis = 1) 
    flatten_ = num_array.min()

    return [min_x_axis.tolist(), min_y_axis.tolist(), flatten_.item()]

def get_sum(num_array):
    """ 
    get sum along both axes and for the flattened matrix.
    """

    sum_x_axis = num_array.sum(axis = 0)
    sum_y_axis = num_array.sum(axis = 1) 
    flatten_ = num_array.sum()

    return [sum_x_axis.tolist(), sum_y_axis.tolist(), flatten_.item()]



def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations = {
        'mean': None,
        'variance': None,
        'standard deviation': None,
        'max': None,
        'min': None,
        'sum': None
    }

    num_list = np.array(list)

    # converting list parameter into np.array 3 x 3
    num_list = num_list.reshape((3, 3))
        
    # initializing the values
    calculations["mean"] = get_mean(num_list)
    calculations["variance"] = get_variance(num_list)
    calculations["standard deviation"] = get_standard_deviation(num_list)
    calculations["max"] = get_max(num_list)
    calculations["min"] = get_min(num_list)
    calculations["sum"] = get_sum(num_list)

    print(type(calculations))

    return calculations