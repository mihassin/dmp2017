def transpose(matrix):
    """Returns the transpose of matrix

    Key arguments:
    matrix -- matrix to be transposed
    """
    return [list(col) for col in zip(*matrix)]
