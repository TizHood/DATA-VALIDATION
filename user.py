import string, random

def get_details():
    first_name = input('Enter your first name: ')
    second_name = input('Enter your second name: ')
    user_email = input('Enter your email address: ')

    details = [first_name, second_name,user_email]

    return details

def gen_password(details):
    password = ''
    length = 5
    characters = string.printable
    for n in range(length):
        x = random.choice(characters)
        random_password = ''.join(random.choice(characters) for i in range(length))

        password = str(details[0][0:2] + details[1][-2:] + random_password)

    return password

details = get_details()
password = gen_password(details)
print ("this is your " + str(password))