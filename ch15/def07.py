def merge_string(*text):
    result=''
    print('type(text)->',type(text)) #tuple
    for s in text:
        result=result+" "+s
    return result
#튜플에서 각 요소를 꺼내 문자열에 넣고 띄어쓰기 하고 반복해 문자열 리턴

print(merge_string('아버지가','방에','들어가신다'))