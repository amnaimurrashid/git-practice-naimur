import datetime
from utils import add, subtract, divide

print("Student Name: A M Naimur Rashid")
print("Today's Date:", datetime.date.today())

print("Addition (5 + 3):", add(5, 3))
print("Subtraction (10 - 4):", subtract(10, 4))
print("Division (10 / 2):", divide(10, 2))
print("Division by zero:", divide(10, 0))
print("--- Execution Completed---")