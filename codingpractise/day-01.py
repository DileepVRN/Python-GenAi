import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

reversed_String= lambda s: s[::-1]
def reverse_string_manually(s:str):
    if len(s)<2:
        return s
    logging.info(f"entered into reverse string {s} ")
    reversed =""
    for char in s:
        reversed=char+reversed
    return reversed
def sum_of_numbers(arr):
    sum=0
    for a in arr:
        sum+=a
    return sum

def main():
    s= "Hello, World!"
    numbers= [1, 2, 3, 4, 5]
    print(reversed_String(s))
    print(reverse_string_manually(s))
    print(sum_of_numbers(numbers))
    print(sum(numbers))
    name=''
    age=0
    try:
        name= input ("Enter your name:")
        age= int(input("Enter your age:"))
    except ValueError as e:
         print("An error occurred:", e)
    print(f"Your name is {name} and you are {age} years old.")

if __name__ == "__main__":
    main()