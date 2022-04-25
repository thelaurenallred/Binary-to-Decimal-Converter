import sys
from colorama import Fore, Style

"""
Usage: python converter.py <conversion_type> <number>
    conversion types:
        binary to decimal = btod
        two's compliment to decimal = ttod
        hex to decimal = htod

"""

def btod(binary,sign):
    decimal = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            decimal += 2**(i)
        elif binary[i] == '0':
            decimal += 0
        elif binary[i] != '0':
            if binary[i] != '1':
                print(Fore.RED + "Error: I can only convert binary numbers.")
                print(Style.RESET_ALL)
                quit()
    if sign == '-':
        decimal += 1
    print(Fore.GREEN + f'Decimal result is: {sign}{decimal}')
    print(Style.RESET_ALL)

def ttod(binary):
    for i in range(len(binary)):
        if binary[i] != '0':
            if binary[i] != '1':
                print(Fore.RED + "Error: I can only convert binary numbers.")
                print(Style.RESET_ALL)
                quit()
    for i in range(len(binary)):
        if binary[i] == '1':
            binary[i] = '0'
        elif binary[i] == '0':
            binary[i] = '1'
    sign = '-'
    btod(binary,sign)
    
def htod(user_in):
    data = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001',
            'A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
    out = []
    for i in range(len(user_in)):
        if user_in[i] in data:
            binary = list(data[user_in[i]])
            out += [*binary]
        else:
            print(Fore.RED + "Error: Make sure input is in hexadecimal.")
            print(Style.RESET_ALL)
            quit()
    h = (out[::-1])
    sign = ''
    btod(h, sign)


def main():
    if len(sys.argv) < 3:
        print(Fore.YELLOW + "Usage:")
        print("    $ python converter.py <conversion_type(btod, ttod, htod)> <number>")
        print(Style.RESET_ALL)
        quit()
    
    conv_type = sys.argv[1]
    user_in = sys.argv[2]

    if conv_type == "btod":
        print(Fore.CYAN + f'Converting {user_in} from binary to decimal...\n')
        print(Style.RESET_ALL)
        binary = list(user_in[::-1])
        sign = ''
        btod(binary, sign)
    elif conv_type == "ttod":
        print(Fore.CYAN + f"Converting {user_in} from two's complement to decimal...\n")
        print(Style.RESET_ALL)
        binary = list(user_in[::-1])
        index = len(binary)-1
        if binary[index] == '0':
            sign = ''
            btod(binary,sign)
        else:
            ttod(binary)
    elif conv_type == "htod":
        print(Fore.CYAN + f'Converting {user_in} from hex to decimal...\n')
        print(Style.RESET_ALL)
        htod(list(user_in))
    else:
        print(Fore.RED + "Error: I can only convert from binary, two's compliment, or hex.") 
        print(Style.RESET_ALL)
        quit()

if __name__ == "__main__":
    main()