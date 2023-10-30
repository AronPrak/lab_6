#Aron Prakash
def encoder(value):
    str_value = str(value)
    new_value = ''
    for i in str_value:
        new_value += str(int(i) + 3)
    return new_value
def decoder(encoded):
    str_number = str(encoded)
    new_number = ""
    for i in str_number:
        new_number += str(int(i) - 3)
    return new_number

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
                new_value = encoder(passcode)
        elif option == 2:
                decoded_passcode = decoder(new_value)
                print(f"The encoded password is {new_value}, and the original password is {decoded_passcode}.")
        elif option == 3:
            break








if __name__ == '__main__':
    main()
