import datetime

import argparse #importing argparser

parser = argparse.ArgumentParser(description='my first program')
#defines a parser

#adding an argument that will just print the message
parser.add_argument("message", help="displays the string you use here")

#define the args
args = parser.parse_args()

#print message argument
print(args.message)

#whatever you write it will always take it as string

age = input("Tell me you age, if you don't mind ")
name = input("Tell me your name ")





def your_age_in_2050(age):
    birth_year = datetime.datetime.now().year - int(age)
    return (2050 - birth_year)

if __name__ == '__main__':
    print("Hello {} You will be {} 2050".format(name, your_age_in_2050(age)))
