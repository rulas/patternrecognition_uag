'''
Created on Jun 28, 2013

@author: lrvillan
'''
import numpy as np

def calculate_descriptor_1(array):
    """ this is the easiest descriptor but the longest
    
        it transforms a bidimiensinal array to a 1 dimension array.
    """
    return (array.flatten().astype(np.int32), 
            array.T.flatten().astype(np.int32))


def calculate_descriptor_2(array):
    """
        Another descriptor. 

        It sums the the black pixels in rows and columns and create a vector
        It also sums the white pixels in rows and columns and create another vector

        ie: columns=0, rows=1

        @return: an array containing both vectors in a 2 dimension array
    """
    sum_of_cols = array.sum(axis=0, dtype=np.int32)
    sum_of_rows = array.sum(axis=1, dtype=np.int32)

    return (sum_of_cols, sum_of_rows)


def calculate_descriptor_3(array):
    """

        Works as calculator_descriptor_2 but it also counts the number of white
        to each vector

        @return: an arrary containing both vectors in a 2 dimension array
    """
    # inverted array is needed to count white pixels
    inverted_array = (~array.astype(np.bool)).astype(int)

    # count black pixels
    sum_of_cols_black = array.sum(axis=0, dtype=np.int32)
    sum_of_rows_black = array.sum(axis=1, dtype=np.int32)
    # count white pixels
    sum_of_cols_white = inverted_array.sum(axis=0, dtype=np.int32)
    sum_of_rows_white = inverted_array.sum(axis=1, dtype=np.int32)

    # create a single array for cols
    sum_of_cols = np.concatenate([sum_of_cols_black, sum_of_cols_white])
    # create a single array for rows
    sum_of_rows = np.concatenate([sum_of_rows_black, sum_of_rows_white])

    return (sum_of_cols, sum_of_rows)

if __name__ == '__main__':
    pass