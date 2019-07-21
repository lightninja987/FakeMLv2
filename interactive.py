#Imports necessary modules for the program to run
import pandas
from pandas import DataFrame
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.svm import LinearSVC
import tkinter.simpledialog
from graphics import graphics
from sklearn.calibration import CalibratedClassifierCV
import tkinter
from tkinter import *
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

tk = tkinter.Tk()
tk.withdraw()
#Reads the Comma Separated Value file into the dataframe
file = pandas.read_csv(r"C:\Users\rohan\Downloads\fake_or_real_news.csv")

"""
Sets y to the labels(FAKE or REAL) of the file and also drops the 
first row of the dataset since it is not necessary
"""
y = file.label
file.drop("label",axis = 1)

title = "TEST TITLE"
text = tkinter.simpledialog.askstring("Title","Enter a string:")

C = {' ': ['potatoman'],
        'Title': [title],
        'Text': [text],
        'Label': [''],
    }

df = pandas.DataFrame(C, columns= [' ', 'Title', 'Text', 'Label'])
export_csv = df.to_csv (r'C:\Users\rohan\Downloads\testingit.csv', index = None, header=True) # here you have to write path, where result file will be stored

tester = pandas.read_csv(r"C:\Users\rohan\Downloads\testingit.csv")


"""
Chooses random files in dataset to be training and testing data. test_size shows what portion of the data
will be test data. random_state is used for generating random numbers to help
"""

X_train = file['text']
X_test = tester['Text']
y_train = file['label']
y_test = tester['Label']

       

#Implemeents Hashing Vectorizer to save terms into numerical indexes

hash_vect = HashingVectorizer(stop_words='english', n_features = 2097152, binary = True, non_negative=True)


#fits the data to make a normal model
hash_train = hash_vect.fit_transform(X_train)
hash_test = hash_vect.transform(X_test)

#makes use of a SVC and a calibrated classifier



classifier = LinearSVC()

finalclassifier = CalibratedClassifierCV(classifier)
#fit classifier onto training data
finalclassifier.fit(hash_train,y_train)

#using 'learned' features from training data, predicts whether news is fake or real
prediction = finalclassifier.predict(hash_test)        


finalpred = str(prediction)
graphics(finalpred)
