#6. WAP to calculate total salary of employee based on basic, da=10% of basic, 
#ta=12% of basic, hra=15% of basic.

# Get basic salary from the user
basic_salary = float(input("Enter the basic salary of the employee: "))

# Calculate allowances
da = 0.10 * basic_salary  # 10% of basic
ta = 0.12 * basic_salary  # 12% of basic
hra = 0.15 * basic_salary # 15% of basic

# Calculate total salary
total_salary = basic_salary + da + ta + hra

# Display the results
print(f"\n--- Salary Details ---")
print(f"Basic Salary: Rs. {basic_salary:.2f}")
print(f"Dearness Allowance (DA): Rs. {da:.2f}")
print(f"Travel Allowance (TA): Rs. {ta:.2f}")
print(f"House Rent Allowance (HRA): Rs. {hra:.2f}")
print(f"----------------------")
print(f"Total Salary: Rs. {total_salary:.2f}") 
