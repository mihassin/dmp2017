import urllib.request
import zipfile
import csv
import os

from helper import transpose

# Globally accessable file_name and data_file
__file_name__ = "Tieliikenne_AvoinData_4_8.zip"
__data_file__ = "vechicledata.csv"


def fetch_data():
    """Function that fetches the project data from hardcoded location.
    The zip file will be stored in ../target/
    """
    url = "http://trafiopendata.97.fi/opendata/" + __file_name__
    req = urllib.request.urlopen(url)
    meta = req.info()
    storing_location = "../target/" + __file_name__
    file_size = int(meta.get("Content-Length"))
    print("Downloading: %s Bytes: %s" % (__file_name__, file_size))
    with open(storing_location, 'wb') as f:
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


def extract_data():
    """Extracts the data file.
    """
    path = '../target/'
    file_location = path + __file_name__
    if not zipfile.is_zipfile(file_location):
        print("File in location " + file_location + " is not a zip file!\n"
              "Check the zip file or try re-fetching the file.")
        return
    zp = zipfile.ZipFile(file_location)
    data_file = zp.namelist()[0]
    zp.extract(data_file, path)
    zp.close()
    os.rename(path+data_file, path+__data_file__)


def read_column(attribute = 0):
    """Reads a column from the data file.
    Skips the headings.

    Key arguments:
    attribute -- index value of the desired column
    """
    data = [] 
    with open('../target/' + __data_file__, encoding="latin_1") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            data.append(row[attribute])
    return data


def col_distribution(col):
    '''Counts each distinct item in col
    and returns a dictionary, where keys are the
    col items and values their counts.

    Argument:
    col -- a list containing data column
    '''
    distr = {}
    for c in col:
        if c not in distr:
            distr[c] = 1
        else:
            distr[c] += 1
    return distr


def data_attributes():
    '''Reads the first row of data file.
    '''
    with open('../target/' + __data_file__, encoding="latin_1") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        attributes = next(reader)
    return attributes
