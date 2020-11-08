import numpy as np
import pandas as pd


# ------------------------------
# Numpy Crash Course
mylist = [1, 2, 3, 4]
np.array(mylist)

a = np.arange(0, 10, 2)

zeros = np.zeros((5, 5))
ones = np.ones((2, 10))

np.random.randint(0, 100, (2, 5))

test1 = np.linspace(0, 10, 2)  # 2 numbers with same liner space in [0, 10)
test2 = np.arange(0, 10, 2)  # space is 2

np.random.seed(100)
nums = np.random.randint(0, 100, 10)
nums.mean()
nums.max()
nums.argmax()
nums.argmin()
nums.reshape(2, 5)

mat = np.arange(0, 100).reshape(10, 10)

greater50 = mat[mat > 50]  # filter

# ------------------------------
# ------------------------------
# Pandas Crash Course
# df = pd.read_csv('salaries.csv')
# print(df)
#
# series_of_bool = df['Age'] > 30  # filter
# print(series_of_bool)
# older30 = df[series_of_bool]
# print(older30)
#
# older30_v2 = df[df['Age'] > 30]
#
#
# unique_values = df['Age'].unique()
# num_of_unique_values = df['Age'].nunique()
#
#
# print(df.info())
# print(df.describe())


mat2 = np.arange(0, 10).reshape(5, 2)
df2 = pd.DataFrame(data=mat2, columns=['A', 'B'])
print(df2)






