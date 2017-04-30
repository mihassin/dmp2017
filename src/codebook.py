from helper import transpose
from helper import flatten


class CodeBook:
	'''CodeBook includes all necessary information regarding the different
	categories used for the data attributes. Class has alot of hardcoding
	based on the analysis of the data done before the data mining. There are
	also few simple functions used for data transformation.
	'''


	def __init__(self):
	# REMEMBER TO REMOVE MISSING VALUES

	# Index 0
	# Light: Mopeds/Motocycles/Quads etc.
	# Heavy: Tractor/Buss/Van/Lorry
	# Others: Others/Public works vehicles/All-terrain vehicles
	 self._vclasses = {'Light': ['L1', 'L1e', 'L2', 'L2e', 'L3', 'L3e', 'L4', 'L4e', 'L5', 'L5e', 'L6e', 'L7e', 'KNP'],
					'Car': ['M1', 'M1G'],
					'Trailer': ['O1', 'O2', 'O3', 'O4'],
					'Heavy': ['C1', 'C2', 'T', 'T1', 'T2', 'T3', 'T4', 'T5', 'LTR', 'M2', 'M2G', 'M3', 'N1', 'N1G', 'N2', 'N2G', 'N3', 'N3G'],
					'Others': ['MUU', 'MTK', 'MA']}

	# Index 1
	 self._init_regis = ['ir 1990 - 1999', 'ir 1958 - 1979', 'ir 1980 - 1989', 'ir 2010 - 2016', 'ir 2000 - 2009']

	# Index 3
	# Remove missing and nul values
	 self._usages = {'Private': ['01'], 'Subject to permit': ['02'], 'School vechile': ['03'], 'Rental': ['04'], 'Sales storage': ['05']}

	# Index 6
	# remove 00000000, remove 00050812
	 self._commencement = ['cy 1900 - 1989', 'cy 1990 - 1999', 'cy 2000 - 2004', 'cy 2005 - 2009', 'cy 2010 - 2017']

	# Index 7
	 self._colors = {'Black': ['0'], 'Brown': ['1'], 'Red': ['2'], 'Green': ['5'],
 			  	  'Blue': ['6', 'Z'], 'Grey': ['8'], 'White': ['9'], 'Silver': ['Y'],
 			  	  'Other colors': ['3', '4', '7', 'X']}

 	# Index 8
	 self._doors = {'Less than 4 doors': {'max': 4}, '4 doors': {'eq': 4,  'min': 1e30, 'max': -1e30}, '5 doors': {'eq': 5, 'min': 1e30, 'max': -1e30}, 'More than 5 doors': {'min': 6}}

	# Index 11
	# Remove value 0 - occurs only once in data
	 self._seats = {'1 seat': {'eq': 1,  'min': 1e30, 'max': -1e30}, '2 seats': {'eq': 2,  'min': 1e30, 'max': -1e30}, '3 seats': {'eq': 3,  'min': 1e30, 'max': -1e30},
				 '4 seats': {'eq': 4,  'min': 1e30, 'max': -1e30}, '5 seats': {'eq': 5,  'min': 1e30, 'max': -1e30}, 'More than 5 seats': {'min': 6}}

	# Index 12
	# min < val <= max
	 self._mass = {'0 - 1000 kg': {'max': 1000}, '1000 - 1500 kg': {'min': 1000, 'max': 1500}, '1500 - 2000 kg': {'min': 1500, 'max': 2000}, 'Greater than 2000 kg': {'min': 2000}}

	# Index 15
	# min < val <= max
	 self._length = {'0 - 4300 mm': {'max': 4300}, '4300 - 4700 mm': {'min': 4300, 'max': 4700}, 'Longer than 4700 mm': {'min': 4700}}

	# Index 16
	# min < val <= max
	 self._width = {'0 - 1700 mm': {'max': 1700}, '1700 - 1800 mm': {'min': 1700, 'max': 1800}, '1800 - 1900 mm': {'min': 1800, 'max': 1900}, '1900 - 2000 mm': {'min': 1900, 'max': 2000}, 'Wider than 2000 mm': {'min': 2000}}

	# Index 17
	# min < val <= max
	 self._height = {'0 - 1450 mm': {'max': 1450}, '1450 - 1500 mm': {'min': 1450, 'max': 1500}, '1500 - 1550 mm': {'min': 1500, 'max': 1550}, 'Greater than 1550 mm': {'min': 1550}}

	# Index 18
	 self._fuels = {'Gasoline': ['01'], 'Diesel': ['02'],
			     'Other fuels': ['33', '05', '53', '11', '13', '63', '48',
			 				'39', '61', '04', 'Y', '60', '37', '43',
			 				'59', '06', '40', '42', '58', '34', '44',
			 				'32', '38', '03', '31', '67', '47']}

	# Index 19
	# min < val <= max
	 self._displacement = {'Small engine': {'max': 1000}, 'Large engine': {'min': 2999}, '1000 - 1999 cc': {'min': 999, 'max': 2000}, '2000 - 2999 cc': {'min': 1999, 'max': 3000}}

	# Index 20
	# min < val <= max
	 self._power = {'0 - 50 kW': {'max': 50}, '50 - 75 kW': {'min': 50, 'max': 75}, '75 - 100 kW': {'min': 75, 'max': 100},
			 '100 - 150 kW': {'min': 100, 'max': 150}, '150 - 200 kW': {'min': 150, 'max': 200}, 'Greater than 200 kW': {'min': 200}}

	# Index 21
	 self._cylinders = {'Less than 4 cylinders': {'max': 4}, '4 cylinders':{'eq': 4, 'min': 1e30, 'max': -1e30}, 'More than 4 cylinders': {'min': 5}}

	# Index 22
	 self._supercharger = {'Supercharger': 'true', 'No supercharger': 'false'}

	# Index 23
	 self._hybrid = {'Hybrid': 'true', 'Not hybrid' :'false'}

	# Index 33
	# min < val <= max
	 self._co2 = {'0 - 150 g': {'max': 150}, '150 - 200 g': {'min': 150, 'max': 200}, 'More than 200 g': {'min': 200}}

	# Index 34
	# min < val <= max
	 self._km = {'More than 200000 km':  {'min': 100000, 'max': 200000}, '0 - 100000 km': {'max': 100000}, '100000 - 200000 km':  {'min': 200000}}


	 self._classes = flatten(
				  		[self._vclasses.keys(), self._init_regis, self._usages.keys(), self._commencement,
				   		 self._colors.keys(), self._doors.keys(), self._seats.keys(), self._mass.keys(),
				   		 self._length.keys(), self._width.keys(), self._height.keys(), self._fuels.keys(),
				   		 self._displacement.keys(), self._power.keys(), self._cylinders.keys(),
				   		 self._supercharger.keys(), self._hybrid.keys(), self._co2.keys(), self._km.keys()]
				   		)

	def __handle_dict(self, value, codes):
		for k, v in codes.items():
			if value in v:
				return k

	def __handle_dict_interval(self, value, codes):
		val = float(value)
		for k, v in codes.items():
			try:
				eq = v['eq']
			except KeyError:
				eq = -1e30
			if val == eq:
				return k
			try:
				minv = v['min']
			except KeyError:
				minv = 0
			try:
				maxv = v['max']
			except KeyError:
				maxv = 1e30
			if val >= minv and val < maxv:
				return k 

	def __handle_date_interval(self, value, codes):
		year = value[:4]
		for interval in codes:
			tmp = interval[3:].split(' - ')
			minv = tmp[0]
			maxv = tmp[1]
			if year >= minv and year <= maxv:
				return interval


	def classify(self, data):
		'''Changes raw data values into
		selected item names.

		data -- preprocessed data matrix
		'''
		cl_data = []
		for row in data:
			classified = []
			classified.append(self.__handle_dict(row[0], self._vclasses))
			classified.append(self.__handle_date_interval(row[1], self._init_regis))
			classified.append(self.__handle_dict(row[2], self._usages))
			classified.append(self.__handle_date_interval(row[3], self._commencement))
			classified.append(self.__handle_dict(row[4], self._colors))
			classified.append(self.__handle_dict_interval(row[5], self._doors))
			classified.append(self.__handle_dict_interval(row[6], self._seats))
			classified.append(self.__handle_dict_interval(row[7], self._mass))
			classified.append(self.__handle_dict_interval(row[8], self._length))
			classified.append(self.__handle_dict_interval(row[9], self._width))
			classified.append(self.__handle_dict_interval(row[10], self._height))
			classified.append(self.__handle_dict(row[11], self._fuels))
			classified.append(self.__handle_dict_interval(row[12], self._displacement))
			classified.append(self.__handle_dict_interval(row[13], self._power))
			classified.append(self.__handle_dict_interval(row[14], self._cylinders))
			classified.append(self.__handle_dict(row[15], self._supercharger))
			classified.append(self.__handle_dict(row[16], self._hybrid))
			classified.append(self.__handle_dict_interval(row[17], self._co2))
			classified.append(self.__handle_dict_interval(row[18], self._km))
			cl_data.append(classified)
		return cl_data


	def integerify(self, data):
		'''Further simplifies item names into integers.

		data -- classified data matrix
		'''
		int_data = []
		for i in range(len(data)):
			row = data[i]
			int_data.append([])
			for j in range(len(row)):
				int_data[i].append(self._classes.index(row[j]))
		return int_data


	def _stringify(self, itemset):
		'''Turns integer sets into string sets.

		itemset -- set of index integers
		'''
		if itemset == set():
			return '{}'
		tmp = set()
		for item in itemset:
			tmp = tmp.union([self._classes[item]])
		return tmp


	def stringify_itemsets(self, frequent):
		'''Changes integers in frequent into strings. Frequent
		is doubly nested list, where frequent[i][0] is the
		itemset and frequent[i][1] is the support of the itemset.

		frequent -- doubly nested list
		'''
		str_freq = []
		for itemset in frequent:
			st = self._stringify(itemset[0])
			str_freq.append([st, itemset[1]])
		return str_freq


	def stringify_rules(self, rules):
		'''Turns items in rules into strings.
		Also generates a rule string. Here
		rules[i][0] is the premise
		rules[i][1] is the consequence and
		rules[i][2] is the measure value.

		rules -- doubly nested list
		'''
		str_rules = []
		for rule in rules:
			premise = str(self._stringify(rule[0]))
			consequence = str(self._stringify(rule[1]))
			st = premise + " => " + consequence
			str_rules.append([st, rule[2]])
		return str_rules

