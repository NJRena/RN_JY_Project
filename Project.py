import pandas as pd
import matplotlib.pyplot as plt

countries = pd.read_excel('IMVA.xlsx')
print(countries)

country = countries['Periods'].str.split(expand = True)
countries = countries.assign(country_year=pd.to_numeric(country[0]))
countrylist = countries[(countries['country_year'] >= 1988) & (countries['country_year'] <= 1997)].iloc[:, 8:19]
out = countrylist.sum().sort_values(ascending=False)/1000
print("The top 3 countries are %s, %s and %s." %(out.index[0], out.index[1], out.index[2]))





ax=out.plot(kind='bar' , title = "Total Travellers from Asia in thousands (Period:1978 - 1987)", figsize=(10,10), legend=True, fontsize=12, label="Travellers")
plt.show()