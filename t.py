import pandas as pd

# create two series
s1 = pd.Series([1, 2])
s2 = pd.Series([3, 4])
# append s2 to s1

s3 = s1._append(s2, ignore_index=True)

print(s3.mean())

print(s3)