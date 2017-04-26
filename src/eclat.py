from interestingness_measures import support_count


def one_item_sets(D):
    I = set()
    for transaction in D:
        I = I.union(transaction)
    return I


def eclat(F, X, I, D, minsupcount):
    """Implementation of Eclat algorithm.
    Searches for frequent itemsets in D with
    minimum support count minsupcount and 
    stores found sets in F.

    Arguments:
    F -- storage for frequent itemsets
    X -- (k-1) previous items (prefix pattern)
    I -- all 1-itemsets of D
    D -- data set
    minsupcount -- minimum support count
    """
    if I == set():
        return set()
    frequent = []
    for item in I:
        candidate = X.union([item])
        sc = support_count(candidate, D)
        if(sc >= minsupcount):
            frequent.append((candidate, item, sc))
    for new_X, item, sc  in frequent:
        F.append(new_X)
        I = I - {item}
        eclat(F, new_X, I, D, minsupcount)


def main(): 
    # D = ['abc', 'acdef', 'abc', 'de']
    # D = [['aa', 'ab', 'ac'], ['aa', 'ac', 'ad', 'ae', 'af'], ['aa', 'ab', 'ac'], ['ad', 'ae']]
    D = [[1, 2, 3], [1, 3, 4, 5, 6], [1, 2, 3], [4, 5]]
    print("Transaction data:")
    print(D, "\n")
    I = one_item_sets(D)
    frequent_itemsets = []
    eclat(frequent_itemsets, set(), I, D, 2)
    print("Found frequent itemsets with frequency of 2:")
    print(frequent_itemsets)

if __name__ == "__main__":
    main()
