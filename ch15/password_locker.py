import pyperclip
#setting -> project src -> python interpreter -> + -> pyperclip 선택후 install package

PASSWORDS={'gmail':"1234", 'naver':'5678', 'daum':
           '9'}
def main():
    site=input('input your site:')
    password=PASSWORDS[site]
    #gmail 치면

    if password:
        pyperclip.copy(password)
        print('your password is copied')
        #pc의 버퍼에(메모리에) gamil의 비밀번호인 1234가 저장됨

    else:
        print('not valid site')

main()