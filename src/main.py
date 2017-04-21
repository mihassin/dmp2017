import preprocessor


if __name__ == "__main__":
 input_var = input("Would you like to download the data? (Y/N)")
 if str.lower(input_var) == 'y' or str.lower(input_var) == 'yes':
  preprocessor.fetch_data()
  print('The zip file is stored in ../target/')
 input_var = input("Would you like to extract the zip file? (Y/N)")
 if str.lower(input_var) == 'y' or str.lower(input_var) == 'yes':
  preprocessor.extract_data()
  print('Extraction complete: ../target/'+preprocessor.__data_file__)
