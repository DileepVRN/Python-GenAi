def tip_calculator(amount,tip_calculator,number_of_people)->float:
    if number_of_people == 0:
        return "Error: Number of people cannot be zero."
    try:
        return  float(amount+float(amount*float(tip_calculator/100)))/number_of_people
    except ZeroDivisionError:
        return "Error: Number of people cannot be zero."

def main():
    amount=float(input("Enter the total bill amount: "))
    tip=float(input("Enter the tip amount in percentage: "))
    number_of_people=int(input("Enter the number of people sharing the bill: "))
    result = float(tip_calculator(amount, tip, number_of_people))
    print(f"Each person should pay: ${result:.2f}")
    print("Number of letters in your name is", len(input("Enter your name: ")))
if __name__ == "__main__":
    main()