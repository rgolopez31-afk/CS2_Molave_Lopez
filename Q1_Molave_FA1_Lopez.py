import math

# Ask the user for the coordinates of the points
x1 = float(input("What is the x coordinate of the first point? "))
y1 = float(input("What is the y coordinate of the first point? "))
x2 = float(input("What is the x coordinate of the second point? "))
y2 = float(input("What is the y coordinate of the second point? "))

x_sub = x2 - x1
y_sub = y2 - y1

# Do the formula
ans = math.sqrt(pow(x_sub, 2) + pow(y_sub, 2))

# Print the answer
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {ans}")

#Using a library instead of writing code from scratch is useful for many reasons. First, libraries make code shorter. Would you rather write lines of code just to perform one function, or import the math module to keep your code concise? Second, libraries are more reliable. If you write code from scratch, there is a chance it will produce incorrect results, whereas imported libraries are highly accurate. In conclusion, importing a library is better than building code from scratch because it ensures your programs are both shorter and more precise.