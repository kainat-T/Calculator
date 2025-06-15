def BMI_cal(w, h):
    BMI = w/h**2
    return BMI

print("\nBMI Calculator")

try:
    w = float(input("Enter your weight(in kg):"))
    h = float(input("Enter your height(in m):"))
    BMI = BMI_cal(w, h)
    print(f"\nYour BMI is: {BMI}")
except ValueError:
    print("Invalid value. Try again!")

if BMI < 18.5:
    print("You are underweight!")
elif 18.5 <= BMI <= 24.9:
    print("You have normal weight!")
elif 25 <= BMI <= 29.9:
    print("You are overweight!")
else:
    print("You are obese!")

