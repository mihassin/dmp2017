from matplotlib import cm
from matplotlib.colors import cnames
import matplotlib.pyplot as plt
import random

from preprocessor import col_distribution
from preprocessor import read_column


def plot_vechicle_classes(vclasses):
	'''Data variable contains different vechicle classes and their support counts in data.
	The Classes are not the ones described in by Trafi, but they represent collections of
	the original classes. For example class 'Car' = {'M1', 'M1G'}.

	This function draws a pie chart of the vechicle classes.
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

def plot_usage():
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


def plot_colors():
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


def plot_seats():
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


def plot_pie(values, labels, colors=[], title="", legend=False, sort=False):
	if title:
		plt.title(title)
	if not colors:
		colors = random.sample(cnames.keys(), len(values))
	if legend:
		if sort:
			matrix = sorted(transpose([labels, values]))
			labels = transpose(matrix)[0]
			values = transpose(matrix)[1]
		patches, texts = plt.pie(values, colors=colors, shadow=True, startangle=140)
		percent = [100.*val/sum(values) for val in values]
		labels = ['{0} - {1:1.1f} %'.format(i,j) for i,j in zip(labels, percent)]
		plt.legend(patches, labels, loc='best', fontsize=10)
	else:
		plt.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
	plt.show()


def main():
	plot_vechicle_classes()
	plot_usage()
	plot_colors()
	plot_seats()

if __name__ == "__main__":
	main()
