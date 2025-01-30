from hmac import digest_size

import matplotlib.pyplot as plt
import pandas as pd
import sns
from visualuisation_eda import visualize_data

from func_for_check_DB import check_DB

df = pd.read_csv('synthetic_data.csv')

check_file = check_DB(df,'database_statistik.txt')
print(check_file)

#  Processes emissions in the specified numerical and categorical columns.

# categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
# numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
# #
# categorical_df = pd.DataFrame({'Categorical Columns': categorical_columns })
# numerical_df = pd.DataFrame({'Numerical Columns': numerical_columns})
# #
# categorical_file = 'categorical_col.csv'
# numerical_file = 'numerical_col.csv'
#
# categorical_df.to_csv(categorical_file, index = False)
# numerical_df.to_csv(numerical_file, index=False)

df_categorical = pd.read_csv('categorical_col.csv')['Categorical Columns'].dropna().tolist()
df_numerical = pd.read_csv('numerical_col.csv')['Numerical Columns'].dropna().tolist()


#visualisation

print(visualize_data(df))
