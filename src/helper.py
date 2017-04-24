def transpose(matrix):
    """Returns the transpose of matrix

    Argument:
    matrix -- matrix to be transposed
    """
    return [list(col) for col in zip(*matrix)]


def class_support(row_distr, min_v, max_v):
    '''Method for calculating support of
    real valued data features. Class is 
    discribed as interval between [min, max).

    Arguments:
    row_distr -- a dictionary, where dict.keys are
                 values appearing in data and dict.values
                 are counts for data values
    min -- lower bound of class interval
    max -- upper bound of class interval
    '''
    N = sum(row_distr.values())
    support_count = 0
    for k, v in row_distr.items():
        cmp = int(k)
        if cmp >= min and cmp < max:
           support_count += v
    return 100. * support_count / N
