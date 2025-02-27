import pandas as pd
import os

dir = os.listdir()

for file in dir[:len(dir) - 1]:
    df = pd.read_csv(file)

    df['DataType'] = df['Type'].apply(lambda x: 'float64' if len(x) == 1 else 'float32')

    df['Type'] = df['Type'].apply(lambda x: x[0])

    cols = df.columns.tolist()
    cols.insert(1, cols.pop(cols.index('DataType')))
    df = df[cols]

    df.to_csv('mod_' + str(file) + '.csv', index=False)