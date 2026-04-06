def _band_name():
    city = input("Enter your city name :")
    pet=input("Enter your pet name :")
    print(f"your band name is {city}  {pet}")
def main():
    print("Welcome to the band name generator")
    _band_name()
if __name__=="__main__":
    main()