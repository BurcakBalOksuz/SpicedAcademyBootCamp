import datetime

name="Ada"
age="16"

def your_age_in_2050(age):
    birth_year=datetime.datetime.now().year-int(age)
    return(2050-birth_year)

if __name__=="__main__":#checks that this module is being run directly as the main python file and imported one
    print("Hello{} You will be {} in 2050".format(name,your_age_in_2050(age)))

    