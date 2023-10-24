#Aron Prakash
def encoder(value):
    str_value = str(value)
    new_value = ''
    for i in str_value:
        new_value += str(int(i) + 3)
    return new_value
def menu():
    print("Menu")
    print('-------------')
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")



def main():
    passcode = 0
    while True:
        menu()
        option  = int(input("Please enter an option: "))
        if option == 1:
                passcode = int(input("Please enter your password to encode:"))
                print("Your password has been encoded and stored!")
        elif option == 2:
                new_value = encoder(passcode)
                print(f"The encoded password is {new_value}, and the original password is {passcode}.")
        elif option == 3:
            break








if __name__ == '__main__':
    main()
