def calculate_age(start_year, end_year):
    return end_year - start_year

start_year = int(input("Enter the year you were born: "))
end_year = int(input("Enter the current year: "))

age = calculate_age(start_year, end_year)

print(f"The age of the person is: {age} years.")