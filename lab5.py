import math

print("==================================================")
print("          ENGINEERING CALCULATION TOOL")
print("==================================================")
num = float(input("Enter a numerical value: "))
exp = float(input("Enter an exponent: "))
dec = float(input("Enter a decimal measurement: "))

power_val = math.pow(num, exp)
sqrt_val = math.sqrt(num)
ceil_val = math.ceil(dec)
floor_val = math.floor(dec)

print("")
print("--- Results ---")
print(f"  Value             : {num}")
print(f"  Exponent          : {exp}")
print(f"  Power (pow)       : {power_val}")
print(f"  Square Root (sqrt): {sqrt_val:.4f}")
print(f"  Decimal Value     : {dec}")
print(f"  Ceil Value        : {ceil_val}")
print(f"  Floor Value       : {floor_val}")
print("==================================================")
