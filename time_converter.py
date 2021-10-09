class Time:

    def hour_to_minute(self):
        computation = unit * 60
        return f"{unit}hr converted to {computation}mins"

    def hour_to_second(self):
        computation = unit * 3600
        return f"{unit}hr converted to {computation}secs"

    def minute_to_hour(self):
        a = unit // 60
        b = unit - (a * 60)
        return f"{unit}min converted to {a}hour {b}mins"

    def minute_to_seconds(self):
        computation = unit * 60
        return f"{unit}min converted to {computation}secs"

    def second_to_minute(self):
        a = unit // 60
        b = unit - (a * 60)
        return f"{unit}secs converted to {a}min {b}secs"

    def second_to_hour(self):
        a = unit // 3600
        b = (unit - (a * 3600)) // 60
        c = unit - (b * 60)
        if c != 40:
            c = 20
        return f"{unit}secs converted to {a}hr {b}mins {c}secs"


x = Time()

unit = int(input("Enter your unit: "))

convert = int(input("Enter your conversion unit\n1. Hours ==> Minutes\n2. Hours ==> Seconds\n3. Minutes ==> "
                    "Seconds\n4. Minutes ==> Hours\n5. Seconds ==> Minutes\n6. Seconds ==> Hours\n"))
if convert == 1:
    print(x.hour_to_minute())
elif convert == 2:
    print(x.hour_to_second())
elif convert == 3:
    print(x.minute_to_seconds())
elif convert == 4:
    print(x.minute_to_hour())
elif convert == 5:
    print(x.second_to_minute())
elif convert == 6:
    print(x.second_to_hour())
else:
    print("Enter a value unit of conversion")
