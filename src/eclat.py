from interestingness_measures import support_count


def _one_item_sets(D):
    '''Finds all 1-itemsets of the data D

    D -- list of transactions
    '''
    I = set()
    for transaction in D:
        I = I.union(transaction)
    return I


def _eclat(F, X, I, D, minsup = 0, maxlen = None):
    """Implementation of Eclat algorithm.
    Searches for frequent itemsets in D with
    minimum support count minsupcount and 
    stores found sets in F.

    Arguments:
    F -- storage for frequent itemsets
    X -- (k-1) previous items (prefix pattern)
    I -- all 1-itemsets of D
    D -- data set
    minsup -- minimum support
    """
    N = len(D)
    minsupcount = int(minsup*N)
    if I == set():
        return set()
    frequent = []
    for item in I:
        candidate = X.union([item])
        sc = support_count(candidate, D)
        if(sc >= minsupcount and len(candidate) <= maxlen):
            frequent.append((candidate, item, sc))
    for new_X, item, sc  in frequent:
        F.append([new_X, 1.*sc/N])
        I = I - {item}
        _eclat(F, new_X, I, D, minsup, maxlen)


def eclat(data, minsup = 0, maxlen = None):
    '''Layer between user and actual eclat algorithm.
    Initializes all necessary arguments and includes
    user given arguments to eclat procedure.
    Returns the frequent itemsets of data with minimum support
    minsup, where each itemset has maximum size of maxlen

    Arguments:
    data -- doubly nested list()
    minsup -- minimum support
    maxlen -- maximum size of each itemset
    '''
    frequent_itemsets = []
    I = _one_item_sets(data)
    if not maxlen: maxlen = 1e30
    _eclat(frequent_itemsets, set(), I, data, minsup, maxlen)
    return frequent_itemsets


def main(): 
    # D = ['abc', 'acdef', 'abc', 'de']
    # D = [['aa', 'ab', 'ac'], ['aa', 'ac', 'ad', 'ae', 'af'], ['aa', 'ab', 'ac'], ['ad', 'ae']]
    D = [[1, 2, 3], [1, 3, 4, 5, 6], [1, 2, 3], [4, 5]]
    print("Transaction data:")
    print(D, "\n")
    frequent_itemsets = eclat(D, minsup = 0.5)
    print("Found frequent itemsets with minimum support of 50%:")
    print(frequent_itemsets)

if __name__ == "__main__":
    main()

