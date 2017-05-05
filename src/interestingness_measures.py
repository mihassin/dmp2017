import math
from helper import transpose
from helper import powerset


def support_count(pattern, D):
    """Return the support count of pattern in dataset D.

    Arguments:
    pattern -- interesting pattern possibly appearing in the dataset
    D -- dataset
    """
    support_count = 0
    tmp_p = set(pattern)
    for transaction in D:
        if tmp_p <= set(transaction):
            support_count += 1
    return support_count
    

def contingency_table(X, Y, D):
	'''Returns the contingency table for X and Y in D.

	Arguments:
	X -- first variable
	Y -- second variable
	D -- dataset
	'''
	N = len(D)
	f11 = support_count(X.union(Y), D)
	f1_ = support_count(X, D) 
	f10 = f1_ - f11
	f_1 = support_count(Y, D)
	f01 = f_1 - f11
	f0_ = N - f1_
	f00 = f0_ - f01
	return [[f00, f01], [f10, f11]]


# Asymmetric objective interestingness measures
def confidence(X, Y, D):
	'''Calculates the confidence of rule X -> Y in D.

	Arguments:
	X -- left side of the rule
	Y -- right side of the rule
	D -- dataset
	'''
	return support_count(X.union(Y), D) / support_count(X, D)


def added_value(X, Y, D):
	'''Calculates the Added Value of rule X -> Y in D.

	Arguments:
	X -- first subset of the itemset
	Y -- second subset of the itemset
	D -- dataset
	'''
	f = contingency_table(X, Y, D)
	N = len(D)
	result = f[1][1] / sum(f[1])
	result -= sum(transpose(f)[1]) / N
	return result


def laplace(X, Y, D):
	'''Calculates the Laplace measure of rule X -> Y in D.
	The measure is also known as Laplace smoothing.
	Here the pseudocounts are 1 and 2, since 
	X and Y are binary.

	Arguments:
	X -- left side of the rule
	Y -- right side of the rule
	D -- dataset
	'''
	f = contingency_table(X, Y, D)
	return (f[1][1] + 1) / (sum(f[1]) + 2)


def conviction(X, Y, D):
	'''Calculates the lift of pattern of rule X -> Y in D.

	Arguments:
	X -- first subset of the itemset
	Y -- second subset of the itemset
	D -- dataset
	'''
	N = len(D)
	f = contingency_table(X, Y, D)
	f1_ = sum(f[1])
	f_0 = sum(transpose(f)[0])
	try:
		result = (f1_ * f_0) / (N * f[1][0])
	except ZeroDivisionError:
		result = None
	return result

# Symmetric objective interestingness measures
def lift(X, Y, D):
	'''Calculates the lift of pattern {X, Y} in D.

	Arguments:
	X -- first subset of the itemset
	Y -- second subset of the itemset
	D -- dataset
	'''
	N = len(D)
	return (N * support_count(X.union(Y), D)) / (support_count(X, D) * support_count(Y, D))


def correlation(X, Y, D):
	'''Calculates phi-coefficient as correlation,
	since X and Y are assumed to be binary variables.

	Arguments:
	X -- first variable
	Y -- second variable
	D -- dataset
	'''
	f = contingency_table(X, Y, D)
	numerator = f[1][1] * f[0][0] - f[0][1] * [1][0]
	f0_ = sum(f[0])
	f1_ = sum(f[1])
	f_0 = sum(transpose(f)[0])
	f_1 = sum(transpose(f)[1])
	denominator = math.sqrt(f0_ * f_0 * f1_ * f_1)
	try:
		result = numerator / denominator
	except ZeroDivisionError:
		result = None
	return result


def odds_ratio(X, Y, D):
	'''Calculates the odds ratio of pattern {X, Y} in D.

	Arguments:
	X -- first variable
	Y -- second variable
	D -- dataset
	'''
	f = contingency_table(X, Y, D)
	try:
		result = (f[0][0] * f[1][1]) / (f[0][1] * f[1][0])
	except ZeroDivisionError:
		result = None
	return result


def IS(X, Y, D):
	'''Calculates the IS measure of pattern {X, Y} in D.

	Arguments:
	X -- first variable
	Y -- second variable
	D -- dataset
	'''
	#return support_count(X + Y, D) / math.sqrt(support_count(X, D) * support_count(Y, D))
	return support_count(X.union(Y), D) / math.sqrt(support_count(X, D) * support_count(Y, D))


def generate_patterns(frequent, data, measure, minval = -1e30):
	'''Generates patterns from frequent itemsets with 
	different interestingness measures. Also ignores patterns
	below threshold value minval. Creates candidates based on
	the type of measure. For symmetric measures patterns
	rhs -> lhs and lhs -> rhs have equal value.

	frequent -- list of frequent itemsets
	data -- data set where frequent are gathered
	measure -- confidence, j_measure, laplace
	           conviction, lift, correlation, 
	           odds_ratio or IS
	minval -- threshold value
	'''
	rules = []
	for f in frequent:
		if is_symmetric(measure):
			candidates = symmetric_premises(f[0])
		else:
			candidates = powerset(f[0])
		candidates.remove(set())
		for c in candidates:
			value = measure(c, f[0] - c, data) 
			if value and value >= minval:
				rules.append([c, f[0] - c, f[1], value])
	return rules


def is_symmetric(measure):
	'''Checks if a measure is symmetric or not.
	
	measure -- function of this module
	'''
	symmetric = [lift, correlation, odds_ratio, IS]
	for s in symmetric:
		if measure == s:
			return True
	return False


def symmetric_premises(s = set()):
	'''Returns the powerset of s. Since doubly nested set
	is not allowed in python, the actual return value is a list
	of sets.

	s -- a set
	'''
	result = [[]]
	for element in s:
		result.extend([subset + [element] for subset in result if len(subset)+1 < len(s)/2 ])
	tmp = [[]]
	tmp_s = list(s)
	for e in tmp_s[1:]:
		tmp.extend([subset + [e] for subset in tmp if len(subset)+2 <= len(tmp_s)/2 ])
	tmp = [[tmp_s[0]] + subset for subset in tmp if len(subset) + 1 == len(tmp_s) / 2]
	result.extend(tmp)
	return [set(lst) for lst in result]


def measure_pattern(X, Y, data):
	'''Calculates all measures for pattern X -> Y

	X -- lhs
	Y -- rhs
	data -- transformed transaction data
	'''
	result = []
	result.append(['Confidence', confidence(X, Y, data)])
	result.append(['Added value', added_value(X, Y, data)])
	result.append(['Laplace', laplace(X, Y, data)])
	result.append(['Conviction', conviction(X, Y, data)])
	result.append(['Lift', lift(X, Y, data)])
	result.append(['Correlation', correlation(X, Y, data)])
	result.append(['Odds ratio', odds_ratio(X, Y, data)])
	result.append(['IS', IS(X, Y, data)])
	return result
