C = 299792458 

def main():
    print("Einstein's Mass-Energy Calculator")
    mass = float(input("Enter kilos of mass (in kg): "))
    energy:float = mass * C**2
    print("e = m * C^2...")
    print(f"m = {mass}")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!")

if __name__ == '__main__':
    main()