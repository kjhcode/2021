#화면에 사각형 그리기
from turtle import *
fd(50)
lt(90)
fd(50)
lt(90)
fd(50)
lt(90)
fd(50)
from turtle import *              
for i in range(4):
                fd(50)
                lt(90)                

                
#화면에 사각형 그리기_for 반복문
from turtle import *
for i in range(3):
                left(20)
                for j in range(4):    
                                fd(50)
                                lt(90)


#사각나선
from turtle import *
width(3)
for i in range(1,200,5):
                fd(i)
                lt(90)
#다각나선
from turtle import *
width(3)
for i in range(1,200,5):
                fd(i)
                lt(30)
#사각나선
from turtle import *
width(3)
for i in range(1,200,5):
                #stamp()
                fd(i)
                lt(91)

#화면에 거북이 그리기
from turtle import *
shape("turtle")
color("blue")
size=20
for i in range(30):
                stamp()
                size=size+3
                fd(size)
                rt(24)


#선으로 복잡한 무늬 그리기
from turtle import *
shape("turtle")
speed("fastest")
for i in range(300):  #300번 반복
                fd(i)        #i만큼 앞으로 이동, 반복할 때마다 선이 길어짐
                rt(91)    #오른쪽으로 91도 회전



#원을 반복해서 그리기
from turtle import *
n=60   #원을 60번 그림
shape("turtle")
speed("fastest")  # 거북이 속도를 가장 빠르게 설정  숫자:0(fastest),10(fast),6(normal),3(slow),1(slowtest)
for i in range(n):
                circle(120)  # 반지름이 120인 원을 그림
                rt(360/n)   #오른쪽으로 6도 회전


#별모양
from turtle import *
shape("turtle")
speed("fastest")
n=5
for i in range(5):
                fd(100)
                rt((360/n)*2)
                fd(100)
                lt(360/n)
#하트모양
begin_fill()
color("pink")
lt(50)
fd(200)
circle(73,221)
lt(180)
circle(73,221)
fd(200)
end_fill()












                
