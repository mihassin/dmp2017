import urllib.request
import zipfile
import csv
import os

from helper import transpose
from codebook import CodeBook


class Preprocessor:
	'''Preprocessor class is responsible for 
	altering data into data mineable form.
	'''

	def __init__(self, path):
		if not os.path.exists(path):
			os.makedirs(path)
		self._path = path
		self._file_name = "Tieliikenne_AvoinData_4_8.zip"
		self._data_file = "vehicledata.csv"
		self._cb = CodeBook()
		self._file_location = ''
		self._data_location = self._path+self._data_file


	def fetch_data(self):
		'''Function that fetches the project data from hard-coded location.
		The zip file will be stored in ../target/
		'''
		if os.path.isfile(self._data_location):
			print('It seems that the data dile already exists!', self._data_location)
			return
		url = "http://trafiopendata.97.fi/opendata/" + self._file_name
		req = urllib.request.urlopen(url)
		meta = req.info()
		self._file_location = self._path + self._file_name
		file_size = int(meta.get("Content-Length"))
		print("Downloading: %s Bytes: %s" % (self._file_name, file_size))
		with open(self._file_location, 'wb') as f:
			file_size_dl = 0
			block_sz = 8192
			while True:
				buffer = req.read(block_sz)
				if not buffer: break
				file_size_dl += len(buffer)
				f.write(buffer)
				status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
				status = status + chr(8)*(len(status)+1)
				print(status)
			print()
			self._extract_data()


	def _extract_data(self):
		'''Extracts the data file.'''
		print('Initiating extraction')
		if not zipfile.is_zipfile(self._file_location):
			print("File in location " + self._file_location + " is not a zip file!\n"
			"Check the zip file or try re-fetching the file.")
			return
		zp = zipfile.ZipFile(self._file_location)
		data_file = zp.namelist()[0]
		zp.extract(data_file, self._path)
		zp.close()
		os.rename(self._path+data_file, self._data_location)
		print('Extraction complete!')


	def cleanse_and_transform(self):
		'''Removes columns, that are not suitable or interesting for data mining.
		Removes all rows containing null values. Transforms all values into categories,
		splits each category into their own binary attribute. Each of the binary attributes
		have integer label.
		'''
		data = []
		with open(self._data_location, encoding='latin_1') as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			next(reader)
			for row in reader:
				row = self._trim_features(row)
				if row.__contains__(''): continue
				data.append(row)
			data = self._cb.classify(data)
			data = self._cb.integerify(data)
		return data


	def _trim_features(self, row):
		'''Removes unsuitable columns from the row

		row -- a row in the data matrix
		''' 
		trimmed = row[0:2]
		trimmed.append(row[3])
		trimmed.extend(row[6:9])
		trimmed.extend(row[11:13])
		trimmed.extend(row[15:24])
		trimmed.extend(row[33:35])
		return trimmed


	def data_attributes(self):
		'''Reads the first row of data file.'''
		with open(self._data_location, encoding="latin_1") as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			attributes = next(reader)
		return attributes


	def col_distribution(self, column):
		'''Counts each distinct item in column
		and returns a dictionary, where keys are the
		column items and values their counts.

		column -- a list containing data column
		'''
		distr = {}
		col = self._read_column(column)
		for c in col:
			if c not in distr:
				distr[c] = 1
			else:
				distr[c] += 1
		return distr


	def _read_column(self, attribute = 0):
		'''Reads a column from the data file.
		Skips the headings.

		attribute -- index value of the desired column
		'''
		data = []
		with open(self._data_location, encoding="latin_1") as csvfile:
			reader = csv.reader(csvfile, delimiter=';')
			next(reader)
			for row in reader:
				data.append(row[attribute])
		return data


	def stringify(self, data, kind='frequent'):
		'''The Integer values of data are indexes of list cb._classes.
		It is important, that the same instant of cb does the stringification
		and integerization. Otherwise the ordering might vary and the results
		will be false. This function ensures the use of the correct cb instance.

		data -- either frequent itemsets or association rules
		kind -- string: either frequent or rules 
		'''
		if kind == 'frequent':
			return self._cb.stringify_itemsets(data)
		elif kind == 'rules':
			return self._cb.stringify_rules(data)
		else:
			return "Second parameter can be either 'frequent' or 'rules'!"

