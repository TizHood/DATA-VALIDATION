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

active = True
container = []

while active:
    details = get_details()

    password = gen_password(details)
    print('Your password is:' + str(password))

    password_like = input(str('Do you like the generated password. If yes, kindly enter Yes. If no, kindly enter No and provide new password '))

    password_loop = True
    while password_loop:
        if password_like == 'Yes' :
            details.append(password)

            container.append(details)

            password_loop = False
        else: 
            user_password = input(str('Enter password longer than or equal to 7 '))

            pass_len = True
            while pass_len:
                
                if len(user_password) >=7:
                    details.append(user_password)

                    container.append(details)

                    pass_len = False
                    password_loop = False


                else:
                    print ('Your entered password is less than the required minimum of 7')
                    user_password = input(str('Enter password longer than or equal to 7'))


    new_user = input(str('Would you like to enter a New user? Yes or No '))
    if (new_user == 'No'):
            
        active = False
        for item in container:
            print(item)

    else:
        active = True

