def validate_password(password=''):
    if(len(password))<8:
        return False
    elif password.isalpha(): #대문자면
        return False
    elif password.isnumeric(): #숫자로만되면
        return False
    else:
        return True


def main():
    user_password=input('input your password:')
    if(validate_password(user_password)):
        print('유효한 password입니다')
    else:
        print('유효하지 않은 password입니다')

main()
'''input your password:afaf4646
유효한 password입니다'''