# Pandas: Drop columns if Name contains a given String

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl'],
    'last_name': ['Smith', 'Hadz', 'Lemon'],
    'salary': [175.1, 180.2, 190.3],
    'experience': [5, 10, 15]
})

print(df)

print('-' * 50)

df.drop(list(df.filter(regex='name')), axis=1, inplace=True)

print(df)