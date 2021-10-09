class Temperature:

    def celsius_to_fahrenheit(self):
        celsius = float(input("Enter your unit in celsius: "))
        computation = 9 / 5 * celsius + 32
        computation = round(computation, 3)
        return f"{celsius}°C converted to {computation}°F"

    def fahrenheit_to_celsius(self):
        fahrenheit = float(input("Enter your unit in fahrenheit: "))
        computation = 5 / 9 * (fahrenheit - 32)
        computation = round(computation, 3)
        return f"{fahrenheit}°F converted to {computation}°C"

    def celsius_to_kelvin(self):
        celsius = float(input("Enter your unit in celsius: "))
        computation = celsius + 273
        computation = round(computation, 3)
        return f"{celsius}°C converted to {computation}°K"

    def kelvin_to_celsius(self):
        kelvin = float(input("Enter your unit in kelvin: "))
        computation = kelvin - 273
        computation = round(computation, 3)
        return f"{kelvin}°K converted to {computation}°C"

    def fahrenheit_to_kelvin(self):
        fahrenheit = float(input("Enter your unit in fahrenheit: "))
        computation = 5 / 9 * (fahrenheit - 32) + 273
        computation = round(computation, 3)
        return f"{fahrenheit}°F converted to {computation}°K"

    def kelvin_to_fahrenheit(self):
        kelvin = float(input("Enter your unit in kelvin: "))
        computation = 9 / 5 * (kelvin - 273) + 32
        computation = round(computation, 3)
        return f"{kelvin}°K converted to {computation}°F"


y = Temperature()
unit = int(input("Enter your conversion unit\n1. Celsius ==> Fahrenheit\n2. Fahrenheit ==> Celsius\n3. Celsius ==> "
                 "Kelvin\n4. Kelvin ==> Celsius\n5. Fahrenheit ==> Kelvin\n6. Kelvin ==> Fahrenheit\n"))

if unit == 1:
    print(y.celsius_to_fahrenheit())
elif unit == 2:
    print(y.fahrenheit_to_celsius())
elif unit == 3:
    print(y.celsius_to_kelvin())
elif unit == 4:
    print(y.kelvin_to_celsius())
elif unit == 5:
    print(y.fahrenheit_to_kelvin())
elif unit == 6:
    print(y.kelvin_to_fahrenheit())
else:
    print("Enter a value unit of conversion")
