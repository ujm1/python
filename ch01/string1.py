pin="881120-1068234"

#없으면 처음부터 : 6 미만의 문자열
yyyymmdd=pin[:6] #0-5까지 쪼갬
num=pin[7:] #7부터
print(yyyymmdd) #881120
print(num) #1068234

split1=pin[4:10] #4~9 : 20-106
print(split1)