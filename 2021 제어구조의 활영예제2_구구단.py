# 구구단1 세로로 출력하기
'''
for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
    print() #  단과 단사이 한줄 삽입
'''

# 구구단2 '구구단 출력 프로그램 꾸미기' 세로로 출력하기
'''
print('|------구구단 출력 프로그램------|')

for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
'''

# 구구단3 '구구단 출력 프로그램/단 꾸미기' 세로로 출력하기
'''
print('|------구구단 출력 프로그램------|')

for i in range(2,10):
    print("------",i,"단------")
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
'''
# 이스케이프 코드
이스케이프 코드란? 프로그래밍 할때 사용할 수 있도록 미리 정의해둔 '문자조합'
주로 출력물을 보기 좋게 정렬하는 용도로 사용
\n - 줄바꿈
\t - 문자열 사이에 탭 간격을 줄 때 사용
\\ - 문자 \를 그대로 표현하고자 할 때 사용
\' - 작은 따움표(')를 그대로 표현하고자 할 때 사용 
\" - 큰 따움표(")를 그대로 표현하고자 할 때 사용
\b - 백스페이스
# 구구단4 '구구단 출력 프로그램/단 꾸미기' 세로로 출력하기 (while문)
'''
print("┌──────┐") 
print("│ 구구단 출력│") 
print("└──────┘") 
i=2 ; j=1 
while i<10: 
    while j<10: 
        print("%d x %d = %d" %( i, j, j*i) ) 
        j+=1

    j=1; i+=1 
    print()
'''    

# 구구단5 '단을 입력받아  출력/단 꾸미기' 세로로 출력하기
'''
print('☞구구단 출력 프로그램☜')
i=int(input("몇단?"))
for j in range(1,10):
       print(i,"*",j,"=",i*j)
'''

'''
# 구구단 몇단 출력
print('|------구구단 출력 프로그램------|')
print('|                                              |')
print('|     몇단을 출력하시겠습니까?   |')
print('|                                |')
print('|--------------------------------|')
i=int(input("몇단?"))
if i<10:
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
        
else:
    print("다시 입력하세요")
'''

# 구구단7 '구구단 가로로 출력하기1
'''
for i in range(2,10):
    for j in range(1,10):
        print(i,"*",j,"=",i*j,end="\t")
'''
        
# 구구단7 '구구단 출력 프로그램/단 꾸미기' 가로로 출력하기2
'''
print('|------구구단 출력 프로그램------|')
for i in range(2,10):
    for j in range(1,10):                   #%d는 이스케이프 문자 중 하나로서 10진수와 매핑할 수 있다.
        print("%d*%d=%2d"%(i,j,i*j),end=' ') #2d의 의미 = >두자리를 사용
    print()
'''

# 구구단8 '구구단 출력 프로그램/단 꾸미기' 가로로 출력하기3
'''
for j in range(1,10):
    for i in range(2,10):
        print("%d*%d=%d"%(i,j,i*j),end='\t') # 이스케이프 코드  \t(tab)
    print("")
'''
'''
# 이스케이프 코드
이스케이프 코드란? 프로그래밍 할때 사용할 수 있도록 미리 정의해둔 '문자조합'
주로 출력물을 보기 좋게 정렬하는 용도로 사용
\n - 줄바꿈
\t - 문자열 사이에 탭 간격을 줄 때 사용
\\ - 문자 \를 그대로 표현하고자 할 때 사용
\' - 작은 따움표(')를 그대로 표현하고자 할 때 사용 
\" - 큰 따움표(")를 그대로 표현하고자 할 때 사용
\b - 백스페이스
'''


# [중요]구구단9 '구구단 출력 프로그램/단 꾸미기' 가로로 출력하기3
for l in range(1,9):#l은 구분선
    print("*****",end="\t")
print("")


for m in range(2,10):
    print(" %d단"%(m),end="\t")
print("")

for n in range(1,9):   #n은 구분선
    print("*****",end="\t")
print("")

for j in range(1,10):  
    for i in range(2,10):   # 범위만큼 단이 반복되어야 하므로 for문의 위치를 서로 바꿔주어야 함.
        print("%d*%d=%2d"%(i,j,i*j),end='\t')
    print("")


#팩토리얼 계산하기
# n! : 1부터 n까지의 정수를 모두 곱한것
#for문 사용
'''
fact=1
n=int(input("정수입력:"))
for i in range(1, n+1):
    fact=fact*i
print(n,"!=",fact)
'''
#while문 사용
'''
i=1
fact=1
n=int(input("정수입력:"))
while(i<=n):
    fact=fact*i
    i=i+1
print(n,"!=",fact)
'''

    
