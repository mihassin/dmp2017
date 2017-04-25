from matplotlib import cm
from matplotlib.colors import cnames
import matplotlib.pyplot as plt
import random

from preprocessor import col_distribution
from preprocessor import read_column


def plot_vechicle_classes():
	'''Reads vehicle class information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	vclasses = read_column(0)
	rdata = col_distribution(vclasses)
	data = {'Light': 0, 'Car': 0, 'Heavy': 0, 'Trailer': 0, 'Others': 0}
	keys = {'Light': ['L1', 'L1e', 'L2', 'L2e', 'L3', 'L3e', 'L4', 'L4e', 'L5', 'L5e', 'L6e', 'L7e', 'KNP'],
			'Car': ['M1', 'M1G'],
			'Trailer': ['O1', 'O2', 'O3', 'O4'],
			'Heavy': ['C1', 'C2', 'T', 'T1', 'T2', 'T3', 'T4', 'T5', 'LTR', 'M2', 'M2G', 'M3', 'N1', 'N1G', 'N2', 'N2G', 'N3', 'N3G'],
			'Others': ['MUU', 'MTK', 'MA']}
	for rkey, rvalue in rdata.items():
		for dkey, dvalue in keys.items():
			if rkey in dvalue:
				data[dkey] += rvalue  
	values = list(data.values())
	labels = list(data.keys())
	colors = ['yellowgreen', 'lightskyblue', 'red', 'orangered', 'gold']
	plot_pie(values, labels, colors, title = 'Customized Vehicle Classes')


def plot_init_reg_date():
	'''Reads initial registration date information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	date = read_column(1)
	rdata = col_distribution(date)
	rdata.pop('')
	data = {'1958 - 1979': 0, '1980 - 1989': 0, '1990 - 1999': 0, '2000 - 2009': 0, '2010 - 2016': 0}
	for k, v in rdata.items():
		year = k[:4]
		for interval in data.keys():
			lower = interval[:4]
			upper = interval[-4:]
			if year >= lower and year <= upper:
				data[interval] += v
				break
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, colors, title = 'Initial registration year', legend=1, sort=1)


def plot_usage():
	'''Reads usage information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	usages = read_column(3)
	keys = {'': 'Others', 'nul': 'Others', '01': 'Private', '02': 'Subject to permit', '03': 'School vechile', '04': 'Rental', '05': 'Sales storage'}
	data = col_distribution(usages)
	for old_key, new_key  in keys.items():
		if new_key not in data:
			data[new_key] = data.pop(old_key)
		else: 	
			data[new_key] += data.pop(old_key)
	data.pop('Others')
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Vehicle usage', legend=1, sort=1)


def plot_commencement_date():
	'''Reads commencement date information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	date = read_column(6)
	rdata = col_distribution(date)
	rdata.pop('')
	rdata.pop('00000000') # False date
	rdata.pop('00050812') # Year probably 2005, but theres only 1 such case
	data = {'1900 - 1989': 0, '1990 - 1999': 0, '2000 - 2004': 0, '2005 - 2009': 0, '2010 - 2017': 0}
	for k, v in rdata.items():
		year = k[:4]
		for interval in data.keys():
			lower = interval[:4]
			upper = interval[-4:]
			if year >= lower and year <= upper:
				data[interval] += v
				break
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, colors, title = 'Year of commencement', legend=1, sort=1)


def plot_colors():
	'''Reads color information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	colors = read_column(7)
	data = {}
	keys = {'': '', '0': 'Black', '1': 'Brown', '2': 'Red', '3': 'Orange', '4': 'Yellow',
			'5': 'Green', '6': 'Blue', '7': 'Violet', '8': 'Grey', '9': 'White', 'X': 'Multi-colored',
			'Y': 'Silver', 'Z': 'Turquoise'}
	for color in colors:
		if keys[color] not in data:
			data[keys[color]] = 1
		else:
			data[keys[color]] += 1
	data.pop('') # Missing values
	data['Blue'] += data.pop('Turquoise')
	data['Others'] = 0
	data['Others'] = data.pop('Orange') + data.pop('Violet') + data.pop('Multi-colored') + data.pop('Yellow')
	values= list(data.values())
	labels=list(data.keys())
	colors = labels.copy()
	colors[colors.index('Others')] = 'Pink'
	colors[colors.index('Brown')] = 'Sienna'
	plot_pie(values, labels, colors, title='Colors', legend=1)


def plot_doors():
	'''Reads door information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	doors = read_column(8)
	rdata = col_distribution(doors)
	rdata.pop('')
	data = {'Less than 4': 0, '4': 0, '5': 0, 'More than 5': 0}
	for k, v in rdata.items():
		drs = int(k)
		if drs < 4:
			data['Less than 4'] += v
		if drs == 4:
			data['4'] += v
		if drs == 5:
			data['5'] += v
		if drs > 5:
			data['More than 5'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Number of doors', sort=1, legend=1)
 

def plot_seats():
	'''Reads seat information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	seats = read_column(11)
	data = col_distribution(seats)
	data.pop('') # Missing values
	data.pop('0') # Only 1 Vechile
	keys = [int(val) for val in data.keys()]
	data['More than 5'] = 0
	for key in keys:
		if key > 5:
			data['More than 5'] += data.pop(str(key))
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Number of Seats', legend=1, sort=1)


def plot_mass():
	'''Reads mass information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	mass = read_column(12)
	rdata = col_distribution(mass)
	rdata.pop('')
	data = {'0 - 1000 kg': 0, '1000 - 1500 kg': 0, '1500 - 2000 kg': 0, 'Greater': 0}
	for k, v in rdata.items():
		mss = int(k)
		if mss < 1000:
			data['0 - 1000 kg'] += v
		elif mss >= 1000 and mss < 1500:
			data['1000 - 1500 kg'] += v
		elif mss >= 1500 and mss < 2000:
			data['1500 - 2000 kg'] += v
		else:
			data['Greater'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Mass', sort=1)


def plot_length():
	'''Reads length information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	length = read_column(15)
	rdata = col_distribution(length)
	rdata.pop('')
	data = {'0 - 4300 mm': 0, '4300 - 4700 mm': 0, 'Longer than 4700 mm': 0}
	for k, v in rdata.items():
		lng = int(k)
		if lng < 4300:
			data['0 - 4300 mm'] += v
		elif lng >= 4300 and lng < 4700:
			data['4300 - 4700 mm'] += v
		else:
			data['Longer than 4700 mm'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Lenght', sort=1)


def plot_width():
	'''Reads width information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	width = read_column(16)
	rdata = col_distribution(width)
	rdata.pop('')
	data = {'0 - 1700 mm': 0, '1700 - 1800 mm': 0, '1800 - 1900 mm': 0, '1900 - 2000 mm': 0, 'Wider than 2000 mm': 0}
	for k, v in rdata.items():
		wdt = int(k)
		if wdt < 1700:
			data['0 - 1700 mm'] += v
		elif wdt >= 1700 and wdt < 1800:
			data['1700 - 1800 mm'] += v
		elif wdt >= 1800 and wdt < 1900:
			data['1800 - 1900 mm'] += v
		elif wdt >= 1900 and wdt < 2000:
			data['1900 - 2000 mm'] += v
		else:
			data['Wider than 2000 mm'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Width', sort=1)


def plot_height():
	'''Reads height information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	height = read_column(17)
	rdata = col_distribution(height)
	rdata.pop('')
	data = {'0 - 1450 mm': 0, '1450 - 1500 mm': 0, '1500 - 1550 mm': 0, 'Greater than 1550 mm': 0}
	for k, v in rdata.items():
		hgt = int(k)
		if hgt < 1450:
			data['0 - 1450 mm'] += v
		elif hgt >= 1450 and hgt < 1500:
			data['1450 - 1500 mm'] += v
		elif hgt >= 1500 and hgt < 1550:
			data['1500 - 1550 mm'] += v
		else:
			data['Greater than 1550 mm'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Height', sort=1)


def plot_fuel():
	'''Reads fuel type information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	fuel = read_column(18)
	rdata = col_distribution(fuel)
	rdata.pop('')
	data = {'Gasoline': 0, 'Diesel': 0, 'Others': 0}
	data['Gasoline'] += rdata.pop('01')
	data['Diesel'] += rdata.pop('02')
	data['Others'] += sum(rdata.values())
	values = data.values()
	labels = data.keys()
	plot_pie(values, labels, title='Fuels', legend=1)


def plot_displacement():
	'''Reads engine displacement information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	displacement = read_column(19)
	rdata = col_distribution(displacement)
	rdata.pop('')
	data = {'Small': 0, 'Large': 0, '1000 - 1499 cc': 0, '1500 - 1999 cc': 0 , '2000 - 2999 cc': 0}
	for k, v in rdata.items():
		disp = int(k)
		if disp < 1000:
			data['Small'] += v
		if disp >= 3000:
			data['Large'] += v
		if disp >= 1000 and disp < 1500:
			data['1000 - 1499 cc'] += v
		if disp >= 1500 and disp < 2000:
			data['1500 - 1999 cc'] += v
		if disp >= 2000 and disp < 3000:
			data['2000 - 2999 cc'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Engine displacement', sort=1)


def plot_power():
	'''Reads maximum net power information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	power = read_column(20)
	rdata = col_distribution(power)
	rdata.pop('')
	data = {'0 - 50 kW': 0, '50 - 75 kW': 0, '75 - 100 kW': 0, '100 - 150 kW': 0, '150 - 200 kW': 0, 'Greater': 0}
	for k, v in rdata.items():
		pwr = float(k)
		if pwr <= 50.0:
			data['0 - 50 kW'] += v
		elif pwr > 50.0 and pwr <=75.0:
			data['50 - 75 kW'] += v
		elif pwr > 75.0 and pwr <= 100.0:
			data['75 - 100 kW'] += v
		elif pwr > 100.0 and pwr <= 150.0:
			data['100 - 150 kW'] += v
		elif pwr > 150.0 and pwr <= 200.0:
			data['150 - 200 kW'] += v
		else:
			data['Greater'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Maximum net power', legend=1, sort=1)


def plot_cylinders():
	'''Reads cylider information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	cylinders = read_column(21)
	data = col_distribution(cylinders)
	data.pop('')
	keys = [int(val) for val in data.keys()]
	data['More than 4'] = 0
	data['Less than 4'] = 0
	for key in keys:
		if key < 4:
			data['Less than 4'] += data.pop(str(key))
		if key > 4:
			data['More than 4'] += data.pop(str(key))
	values = data.values()
	labels = data.keys()
	plot_pie(values, labels, title='Number of Cylinders', legend=1, sort=1)


def plot_co2():
	'''Reads co2 emission information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	co2 = read_column(33)
	rdata = col_distribution(co2)
	rdata.pop('')
	data = {'0 - 150 g': 0, '150 - 200 g': 0, 'More than 200 g': 0}
	for k, v in rdata.items():
		g = int(k)
		if g < 150:
			data['0 - 150 g'] += v
		elif g >= 150 and g < 200:
			data['150 - 200 g'] += v
		else:
			data['More than 200 g'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Carbon dioxide emissions')


def plot_km():
	'''Reads driven distance information from the data, re-organizes the data
	and then uses plot_pie to plot a pie chart.
	'''
	km = read_column(34)
	rdata = col_distribution(km)
	rdata.pop('')
	data = {'0 - 100000 km': 0, '100000 - 200000 km': 0, 'More than 200000 km': 0}
	for k, v in rdata.items():
		dist = int(k)
		if dist < 100000:
			data['0 - 100000 km'] += v
		elif dist >= 100000 and dist < 200000:
			data['100000 - 200000 km'] += v
		else:
			data['More than 200000 km'] += v
	values = list(data.values())
	labels = list(data.keys())
	plot_pie(values, labels, title='Driven distance', sort=1, legend=1)


def plot_pie(values, labels, colors=[], title="", legend=False, sort=False):
	'''Extended version of matplotlib.pyplot's pie chart.
	In addition to plt.pie's original functionality the function can create
	a randomized color scheme for the slices in the pie and customize a legend table.
	Also there's an option to sort the value/labels based on the values.

	Argument:
	values - counts for labels
	labels - labels or names of the pie slices
	colors - predetermined color scheme
	title - title of the chart
	legend - whether or not a legend should be added next to the chart
	sort - whether or not the value-labels should be sorted based on labels 
	'''
	if title:
		plt.title(title)
	if not colors:
		colors = random.sample(cnames.keys(), len(values))
	if sort:
		matrix = sorted(transpose([labels, values]))
		labels = transpose(matrix)[0]
		values = transpose(matrix)[1]
	if legend:
		patches, texts = plt.pie(values, colors=colors, shadow=True, startangle=140)
		percent = [100.*val/sum(values) for val in values]
		labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]
		plt.legend(patches, labels, loc='best', fontsize=10)
	else:
		plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
	plt.show()


def main():
	input_var = input('This script will display 17 pie chart.\n'
					+ 'The sciprt will most likely take alot of processing time.'
					+ 'Would you like to see the class pie charts? (Y/N)\n')
	if str.lower(input_var) == 'y'
		plot_vechicle_classes()
		plot_init_reg_date()
		plot_usage()
		plot_commencement_date()
		plot_colors()
		plot_doors()
		plot_seats()
		plot_mass()
		plot_length()
		plot_width()
		plot_height()
		plot_fuel()
		plot_displacement()
		plot_power()
		plot_cylinders()
		plot_co2()
		plot_km()

if __name__ == "__main__":
	main()

