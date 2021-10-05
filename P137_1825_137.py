f8=open("movie8.txt","w")
title=input("뭔영화 볼건디?")
fee=input("얼마야?")
f8.write(title+"\n")
f8.write(fee+"\n")
f8.close()
f8=open("movie8.txt","r")
title=f8.readline()
fee=f8.readline()
print("영화제목:",title)
print("영화비:",fee)
f8.close()
name=input("누가 예매해:")
date=input("언제 몇시에:")
num=input("몇명:")
total=int(fee)*int(num)
f8=open("movie8.txt","a")
print("지불금액은:",total,"원입니다.")
f8.write("예약자:"+name+"\n")
f8.write("예약일:"+date+"\n")
f8.write("예약인원:"+num+"\n")
f8.write("지불금액:"+str(total)+"\n")
f8.close()















