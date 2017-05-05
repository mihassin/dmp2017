import os

from preprocessor import Preprocessor
import eclat
import interestingness_measures as im

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_PATH = PROJECT_ROOT + '/target/'
pp = Preprocessor(TARGET_PATH)

if __name__ == "__main__":
	input_var = input("Would you like to download the data? (Y/N) ")
	if str.lower(input_var) == 'y' or str.lower(input_var) == 'yes':
		pp.fetch_data()
		print('Data file has been stored in ' + TARGET_PATH)
	input_var = input('Would you like to mine some data? (Y/N) ')
	if str.lower(input_var) == 'y' or str.lower(input_var) == 'yes':
		print('Cleaning and transforming data..')
		data = pp.cleanse_and_transform()
		while(True):
			min_sup = input('Select minimum support (0 - 1). Press Q to quit program. ')
			if str.lower(min_sup) == 'q':
				quit()
			try:
				min_sup = float(min_sup)
			except ValueError:
				print('Only numbers allowed!')
				continue
			if min_sup >= 0 and min_sup <= 1:
				break
			else:
				print('Minimum support has to be between 0 and 1!')
		print('Mining frequent itemsets..')
		frequent = eclat.eclat(data, minsup=min_sup)
		pp.store_frequent(frequent)
		while(True):
			meas = input('Select a measure: confidence, added value, laplace, conviction, lift, correlation, odds ratio or IS. Press Q to quit program. ')
			if str.lower(meas) == 'q':
				quit()
			if meas == 'confidence':
				measure = im.confidence
				break
			elif meas == 'added value':
				measure = im.added_value
				break
			elif meas == 'laplace':
				measure = im.laplace
				break
			elif meas == 'conviction':
				measure = im.conviction
				break
			elif meas == 'lift':
				measure = im.lift
				break
			elif meas == 'correlation':
				measure = im.correlation
				break
			elif meas == 'odds ratio':
				measure = im.odds_ratio
				break
			elif meas == 'IS':
				measure = im.IS
				break
			else:
				print('Options are: confidence, added value, laplace, conviction, lift, correlation, odds ratio or IS!')
		print('Mining rules..')
		rules = im.generate_patterns(frequent, data, measure)
		pp.store_rules(rules, meas)
		print('Thank you and good bye!')
