from IPython.display import display
import pandas as pd

covid = pd.read_csv('owid-covid-data.csv', sep=',')
display(covid)