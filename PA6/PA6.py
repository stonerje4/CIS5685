"""
PA6
James Stoner 
"""

def conversion(imperial_unit, conversion_rate):
    return imperial_unit / conversion_rate

def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi


def main():
    LBS_PER_KG = 2.2046
    INCHES_PER_METER = 39.3701

    weight_lbs = float(input("Please enter weight (pounds): "))
    height_in = float(input("Please enter height (inches): "))

    new_weight = conversion(weight_lbs, LBS_PER_KG)
    new_height = conversion(height_in, INCHES_PER_METER)

    new_bmi = calculate_bmi(new_weight, new_height)
    print("BMI is ", new_bmi)


if __name__ == '__main__':
    main()