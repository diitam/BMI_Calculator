# bmi_calculator.py

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI) using weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m) ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    print("Your BMI is:", bmi)

if __name__ == "__main__":
    main()
