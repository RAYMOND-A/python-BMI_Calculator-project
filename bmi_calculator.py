# Coding challenge an upgraded version of BMI calculator 2.0

bmi_height = float(input("Enter your height in m to know your BMI value? "))
bmi_weight = float(input("Enter your weight in kg to know your BMI value? "))

bmi_value = round(bmi_weight / bmi_height**2)
print(f"Your BMI value is {bmi_value}")

if bmi_value < 18.5:
    print(f"Your BMI is {bmi_value}, you are underweight")
elif bmi_value > 18.5 and bmi_value < 25:
    print(f"Your BMI is {bmi_value}, you have a normal weight")
elif bmi_value > 25 and bmi_value < 30:
    print(f"Your BMI is {bmi_value}, you are overweight")
elif bmi_value > 30 and bmi_value < 35:
    print(f"Your BMI is {bmi_value}, you are obese")
else:
    print(f"Your bmi_value {bmi_value}, you are clinically obese")

