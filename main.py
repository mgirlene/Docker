from IPython.display import display
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

covid = pd.read_csv('owid-covid-data.csv', sep=',') #lendo o arquivo
display(covid) #mostrando os dados

x = covid['date']
y = covid['new_cases']



sns.lineplot(x=x,y=y) #grafico com a data e os novos casos

covid.describe() #descrição do dataset

df_sum = covid.groupby('date').agg({'new_cases': 'sum'}).reset_index() #agrupando pela data e somando o total de novos casos

display(df_sum)

plt.stackplot(df_sum['date'], df_sum['new_cases'], labels=['Novos Casos']) #grafico do dataframe com a soma de novos casos
plt.legend(loc = 'upper left')