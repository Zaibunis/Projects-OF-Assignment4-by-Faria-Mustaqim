def main():
    print("Mars Weight Calculator")
    earth_weight = float(input("Enter your weight on Earth: "))
    mars_weight = round(earth_weight * 0.38 , 2)
    print(f"Your equivalent weight on Mars: {mars_weight}kg")
   

if __name__ == "__main__":
    main()

def main():
    print("Planetary Weight Converter")
    earth_weight = float(input("Enter your weight on Earth: "))
    planet = input("Enter a planet: ").title()
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    gravity = gravity_factors[planet]
    planet_weight = round(earth_weight*gravity,2)
    print(f"The equivalent weight on {planet}: {planet_weight}")


if __name__ == "__main__":
    main()