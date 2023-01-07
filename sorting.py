import pandas as pd

data = pd.DataFrame({
	"roll_no": [101, 103, 104, 102, 105],
	"name":    ["Alok", "Ramesh", "Suresh", "Mahesh", "Arunesh"],
	"grades":   ["A", "B", "A", "C", "D"],
        "marks":    [20, 18, 22, 15, 10]
        })
print(data)

# Sorting data based on grades
print(data.sort_values(by=['grades']))

# Sorting data frome based on roll numbers
print(data.sort_values(by=['roll_no']))

# Sorting based on more than one parameters
print(data.sort_values(by=["grades", "marks"], ascending=[True, False]))

# By above sorting, actual data frame hasn't changed yet
print(data)

# To make the sorting changes to take effect

data.sort_values(by=["grades", "marks"], ascending=[True, False], inplace=True)
print(data)

# resetting index
data.reset_index()
print(data)

# To drop the new created index row

data.reset_index(inplace=True, drop=True)
print(data)
