n=int(input('숫자를 입력하세요'))
#사용자가 숫자 입력하고 엔터 누르면
k2=55

if n>0:
    print('{0]은 양수입니다. {1}'.format(n,k2)) #n이 {0}에, k2가 {1}에 들어감
    #57은 양수입니다. 55...나와야 하는데 오류.
    #행변환에 엄격
if n<0:
    print('{}은 음수입니다.'.format(n))

if True:
    print('항상 실행')