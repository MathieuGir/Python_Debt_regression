
pip install pandas

import pandas as pd

chemin_fichier_excel = 'econ-gen-dette-trim-adm-pub-2.xlsx'

df = pd.read_excel(chemin_fichier_excel)

print(df.head())


