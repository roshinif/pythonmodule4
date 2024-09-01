# Module3 - Conditional structure
# Question 1
size_limit_of_a_zander = 42
length = float(input("Enter the length of the zander in centimeters:"))
if length >= size_limit_of_a_zander:
    print("Zander meets the size")
else:
    print("Zander does not meet the size")
    print("Release the fish back into the lake")
below_limit = size_limit_of_a_zander - length


# Question 2
cabin_class = input("Enter the cabin class (LUX, A , B , C):")
if cabin_class == "LUX":
    print("Upper deck cabin with a balcony")

elif cabin_class == "A":
    print("Above the car deck, equipped with a window")

elif cabin_class == "B":
    print("Windowless cabin above the car deck")

elif cabin_class == "C":
    print("Windowless cabin below the car deck")

else:
    print("Invalid cabin class")


# Question 3
gender = input("Enter your biological gender (male/female):")
hemoglobinValue = float(input("Enter your hemoglobin value:"))

if gender == "female":
    if hemoglobinValue < 117:
        print("The hemoglobin value is low")
    elif hemoglobinValue > 155:
        print("The hemoglobin value is high")
    else:
        print("The hemoglobin value is normal")

elif gender == "male":
    if hemoglobinValue < 134:
        print("The hemoglobin value is low")
    elif hemoglobinValue > 167:
        print("The hemoglobin value is high")
    else:
        print("The hemoglobin value is normal")


# Question 4
year = int (input("Enter the year:"))
if (year % 4 == 0 and year % 100  == 0  and year % 400 == 0):
    print("This is a leap year")

else:
    print("This is not a leap year")

