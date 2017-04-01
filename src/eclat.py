def support_count(pattern, D):
    """Return the support count of 
    pattern in dataset D.

    Key arguments:
    pattern -- interesting pattern possibly
               appearing in the dataset
    D -- dataset
    """
    support_count = 0
    tmp_p = set(pattern)
    for transaction in D:
        if tmp_p <= set(transaction):
            support_count += 1
    return support_count


def eclat(F, X, I, D, minsupcount):
    if I == set():
        return set()
    frequent = []
    for item in I:
        candidate = X.union(item)
        sc = support_count(candidate, D)
        if(sc >= minsupcount):
            frequent.append((candidate, item, sc))
    for new_X, item, sc  in frequent:
        F.append(new_X)
        I = I - {item}
        eclat(F, new_X, I, D, minsupcount)


def main(): 
    D = ['abc', 'acdef', 'abc', 'de']
    print("Transaction data:")
    print(D, "\n")
    I = set()
    for transaction in D:
        I = I.union(transaction)
    frequent_itemsets = []
    eclat(frequent_itemsets, set(), I, D, 2)
    print("Frequent itemsets with support count threshold of 2:")
    print(frequent_itemsets)

if __name__ == "__main__":
    main()
