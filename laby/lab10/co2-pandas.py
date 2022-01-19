import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cd = pd.read_csv('owid-co2-data.csv')
cda = cd.fillna(0).groupby('country').agg(sum_co2=('co2',np.sum))
print('Parametry statystyczne emisji każdego kraju przez cały czas łącznie')
print(cda.describe())
eu = cd.loc[cd['country']=='Europe']
na = cd.loc[cd['country']=='North America']
az = cd.loc[cd['country']=='Asia']
eu = eu[['year','co2']].values
na = na[['year','co2']].values
az = az[['year','co2']].values
eu = np.array(eu).transpose()
na = np.array(na).transpose()
az = np.array(az).transpose()
plt.plot(eu[0],eu[1], label='Europa')
plt.plot(na[0],na[1], label='Ameryka Północna')
plt.plot(az[0],az[1], label='Azja')
plt.title('Emisja CO2 zależnie od roku')
plt.xlabel('rok')
plt.ylabel('emisja CO2')
plt.legend()
plt.show()


