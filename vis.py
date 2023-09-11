from sklearn import neighbors, datasets, metrics
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

main =  pd.read_json('../data_deliverable/data/dob_violations.json')



counts = main['violation_type'].value_counts()

df = main['violation_type'].unique()#.groupby('violation_type').sum()
counts_df = pd.DataFrame({
    'category': df,
    'count': counts})
print(counts_df)
#print(df)
#values_to_keep = counts[counts >= 5].index
#df_filtered = main[main['violation_type'].isin(values_to_keep)]

plt.barh(counts.index, counts.values)

plt.show()