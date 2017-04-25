from helper import transpose
from helper import flatten


class CodeBook:
	# REMEMBER TO REMOVE MISSING VALUES

	# Index 0
	# Light: Mopeds/Motocycles/Quads etc.
	# Heavy: Tractor/Buss/Van/Lorry
	# Others: Others/Public works vehicles/All-terrain vehicles
	__vclasses__ = {'Light': ['L1', 'L1e', 'L2', 'L2e', 'L3', 'L3e', 'L4', 'L4e', 'L5', 'L5e', 'L6e', 'L7e', 'KNP'],
					'Car': ['M1', 'M1G'],
					'Trailer': ['O1', 'O2', 'O3', 'O4'],
					'Heavy': ['C1', 'C2', 'T', 'T1', 'T2', 'T3', 'T4', 'T5', 'LTR', 'M2', 'M2G', 'M3', 'N1', 'N1G', 'N2', 'N2G', 'N3', 'N3G'],
					'Others': ['MUU', 'MTK', 'MA']}

	# Index 1
	__init_regis__ = ['1990 - 1999', '1958 - 1979', '1980 - 1989', '2010 - 2016', '2000 - 2009']

	# Index 3
	# Remove missing and nul values
	__usages__ = {'Private': ['01'], 'Subject to permit': ['02'], 'School vechile': ['03'], 'Rental': ['04'], 'Sales storage': ['05']}

	# Index 6
	# remove 00000000, remove 00050812
	__commencement__ = ['1900 - 1989', '1990 - 1999', '2000 - 2004', '2005 - 2009', '2010 - 2017']

	# Index 7
	__colors__ = {'Black': ['0'], 'Brown': ['1'], 'Red': ['2'], 'Green': ['5'],
 			  	  'Blue': ['6', 'Z'], 'Grey': ['8'], 'White': ['9'], 'Silver': ['Y'],
 			  	  'Others': ['3', '4', '7', 'X']}

 	# Index 8
	__doors__ = ['Less than 4', '4', '5' 'More than 5']

	# Index 11
	# Remove value 0 - occurs only once in data
	__seats__ = ['1', '2', '3', '4', '5', 'More than 5']

	# Index 12
	# min < val <= max
	__mass__ = {'0 - 1000 kg': {'max': 1000}, '1000 - 1500 kg': {'min': 1000, 'max': 1500}, '1500 - 2000 kg': {'min': 1500, 'max': 2000}, 'Greater': {'min': 2000}}

	# Index 15
	# min < val <= max
	__length__ = {'0 - 4300 mm': {'max': 4300}, '4300 - 4700 mm': {'min': 4300, 'max': 4700}, 'Longer than 4700 mm': {'min': 4700}}

	# Index 16
	# min < val <= max
	__width__ = {'0 - 1700 mm': {'max': 1700}, '1700 - 1800 mm': {'min': 1700, 'max': 1800}, '1800 - 1900 mm': {'min': 1800, 'max': 1900}, '1900 - 2000 mm': {'min': 1900, 'max': 2000}, 'Wider than 2000 mm': {'min': 2000}}

	# Index 17
	# min < val <= max
	__height__ = {'0 - 1450 mm': {'max': 1450}, '1450 - 1500 mm': {'min': 1450, 'max': 1500}, '1500 - 1550 mm': {'min': 1500, 'max': 1550}, 'Greater than 1550 mm': {'min': 1550}}

	# Index 18
	__fuels__ = {'Gasoline': ['01'], 'Diesel': ['02'],
			     'Others': ['33', '05', '53', '11', '13', '63', '48',
			 				'39', '61', '04', 'Y', '60', '37', '43',
			 				'59', '06', '40', '42', '58', '34', '44',
			 				'32', '38', '03', '31', '67', '47']}

	# Index 19
	# min < val <= max
	__displacement__ = {'Small': {'max': 1000}, 'Large': {'min': 2999}, '1000 - 1999 cc': {'min': 999, 'max': 2000}, '2000 - 2999 cc': {'min': 1999, 'max': 3000}}

	# Index 20
	# min < val <= max
	__power__ = {'0 - 50 kW': {'max': 50}, '50 - 75 kW': {'min': 50, 'max': 75}, '75 - 100 kW': {'min': 75, 'max': 100},
			 '100 - 150 kW': {'min': 100, 'max': 150}, '150 - 200 kW': {'min': 150, 'max': 200}, 'Greater': {'min': 200}}

	# Index 21
	__cylinders__ = ['Less than 4', '4', 'More than 4']
	
	# Index 22
	__supercharger__ = {'Supercharger': 'true', 'No supercharger': 'false'}

	# Index 23
	__hybrid__ = {'Hybrid': 'true', 'Not hybrid' :'false'}

	# Index 33
	# min < val <= max
	__co2__ = {'0 - 150 g': {'max': 150}, '150 - 200 g': {'min': 150, 'max': 200}, 'More than 200 g': {'min': 200}}
	
	# Index 34
	# min < val <= max
	__km__ = {'More than 200000 km':  {'min': 100000, 'max': 200000}, '0 - 100000 km': {'max': 100000}, '100000 - 200000 km':  {'min': 200000}}


	__classes__ = flatten(
				  			[__vclasses__.keys(), __init_regis__, __usages__.keys(), __commencement__,
				   			 __colors__.keys(), __doors__, __seats__, __mass__.keys(), __length__.keys(),
				   			 __length__.keys(), __width__.keys(), __height__.keys(), __fuels__.keys(),
				   			 __displacement__.keys(), __power__.keys(), __cylinders__, __supercharger__.keys(),
				   			 __hybrid__.keys(), __co2__.keys(), __km__.keys()]
				   		)


	def classify(data):
		return 


	def integerify(data):
		int_data = []
		for i in range(len(data)):
			row = data[i]
			int_data.append([])
			for j in range(len(row)):
				int_data[i].append(cb.__classes__.index(row[j]))
		return int_data


	def stringify(data):
		str_data = []
		for i in range(len(data)):
			row = data[i]
			str_data.append([])
			for j in range(len(row)):
				str_data[i].append(cb.__classes__[row[j]])
		return str_data
