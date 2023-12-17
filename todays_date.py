#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#from sklearn import model_selection
#from sklearn.linear_model import LogisticRegression
#from sklearn.model_selection import train_test_split
from datetime import datetime

class todays_date:
    today = datetime.today()
    date_in_format = today.strftime("%m-%d-%Y %H:%M:%S")
    date_in_format_2 = today.strftime("%A, %B %d, %Y %I:%M:%S")
    date_in_format_3 = today.strftime("%A, %B %d, %I:%M %p")
    print(date_in_format)
    print(date_in_format_2)
    print(date_in_format_3)

todays_date()

# just messing around/practicing