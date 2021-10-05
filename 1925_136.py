
#movie9.txt  파일명
#f9 파일변수
f9=open("movie9.txt","w")
title=input("뭔영화볼래?")
fee=input("티켓비용?")
f9.write(title+"\n")
f9.write(fee)
f9.close()
f9=open("movie9.txt","r")
title=f9.readline()
fee=f9.readline()
print("영화제목:",title)
print("티켓비용:",fee)
f9.close()
name=input("예약할사람?")
date=input("언제볼겨?")
num=input("몇명?")
total=int(fee)*int(num)
f9=open("movie9.txt","a")
print("지불할 금액:",total,"원입니다.")
f9.write("예약자:"+name+"\n")
f9.write("예약일:"+date+"\n")
f9.write("예약인원:"+num+"\n")
f9.write("지불금액:"+str(total)+"\n")
f9.close()



















