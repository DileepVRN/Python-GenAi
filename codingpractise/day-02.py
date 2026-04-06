def is_palindrom_number(st:str)->bool:
    filtered=''.join( c.lower() for c in st  if c.isalnum())
    return filtered==filtered[::-1]
def is_palindrome_string(st:str)->bool:
    left=0
    right=len(st)-1
    while left<right:
        while left<right and not st[left].isalnum():
            left+=1
        while right>left and not st[right].isalnum():
            right-=1    
        if st[left].lower()!=st[right].lower():
            return False
        left+=1
        right-=1    
    return True


def main():
    print("Welcome to the Palindrome number checker")
    st=input("Enter a string :")
    print(f"{st} is a palindrome string : {is_palindrome_string(st)}")
    if is_palindrom_number(st):
        print(f"{st} is a palindrome number")
    else:
        print(f"{st} is not a palindrome number")
if __name__=='__main__':
    main()
