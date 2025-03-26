#fahrenheit_to_celsius

def main():
    print("Fahrenheit to Celsius Converter")
    degrees_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"Temperature:{degrees_fahrenheit}°F = {degrees_celsius:.2f}°C")

if __name__ == '__main__':
    main()