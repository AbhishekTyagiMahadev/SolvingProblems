Celsius = float(input("Enter the temprature in °C:"))

def cal(Celsius):
    Fahrenheit  = (Celsius*9/5)+32
    return Fahrenheit

Fahrenheit = cal(Celsius)
print(f"{Celsius}°C = {Fahrenheit}°F")