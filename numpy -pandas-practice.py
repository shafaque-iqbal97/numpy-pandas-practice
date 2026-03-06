# NumPy & pandas Assignment 

#NumPy Assignment

import numpy as np
 
# Q1 Import NumPy and create a NumPy array from the following list:

data  = np.array([20,30,40,50,60])
print(data)

# Q2 Create a 3×3 NumPy array with numbers from 1 to 9.

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr)

# Q3 Find the following from the array in Q2:
# Shape
# Size
# Number of dimensions

print(np.shape(arr))
print(np.size(arr))
print(np.ndim(arr))

# Q4 Create a NumPy array containing numbers from 0 to 20 with step 2.

arr = np.arange(0,20,2)
print(arr)

# Q5 Generate a 4×4 matrix of random numbers between 0 and 1.

matrix = np.random.rand(4,4)
print(matrix)

# Q6 rom the array below: [5, 10, 15, 20, 25, 30]
# Find: Maximum value, Minimum value, Mean

arr = np.array([5,10,15,20,25,30])
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))

# Q7 Create two arrays: a = [1,2,3,4], b = [5,6,7,8]
# Perform: Addition, Multiplication, Dot product

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(np.add(a,b))
print(np.multiply(a,b))
print(np.dot(a,b))

# Q8 Reshape the array: [1,2,3,4,5,6,7,8] into a 2×4 matrix.

arr = np.array([1,2,3,4,5,6,7,8])
print(arr.reshape(2,4))

# Pandas Assignment

import pandas as pd

# Q1 Import pandas and create a Series from the list: [100, 200, 300, 400, 500]

series = pd.Series([100,200,300,400,500]) 
print(series) 

# Q2 Create a DataFrame using the dictionary: data = {
#     "Name": ["Ali", "Sara", "John", "David"],
#     "Age": [23, 25, 21, 24],
#     "Salary": [50000, 60000, 45000, 52000]
# }   Print the DataFrame.


data = {
    "Name" : ["Ali", "Sara", "John", "David"],
    "Age" : [23,25,21,24],
    "Salary" : [50000,60000,45000,52000]
}
df = pd.DataFrame(data)

print(df)

# Q3 Display: First 2 rows, Last 2 rows

print(data.head(2))      # First Two rows
print(data.tail(2))      # Last Two rows

# Q4 Find: Mean salary & Maximum salary

print(data["Salary"].mean())
print(data["Salary"].max())

# Q5 Select only the Name and Salary columns.

print(data[["Name","Salary"]])

# Q6 Filter the DataFrame to show employees with: Salary greater than 50,000.

print(data[data["Salary"] > 50000])

# Q7 Add a new column called: Bonus = Salary * 0.10

df["Bonus"] = df["Salary"] * 0.10
print(df)

# Q8 Sort the DataFrame by Salary in descending order.

sorted_data = data.sort_values(by = "Salary", ascending= False)
print(sorted_data)

# Q9 Check: Data types of columns & Summary statistics of the DataFrame

print(df.dtypes)
print(df.describe())

# Q10 Save the DataFrame as a CSV file named: employee_data.csv

df.to_csv("employee_data.csv", index=False)

# Q11 Load the CSV file using Pandas

df = pd.read_csv("employee_data.csv")
print(df)

# Q12 Display Number of Rows and Columns

print(df.shape)

















