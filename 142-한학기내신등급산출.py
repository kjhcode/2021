print("[내신 등급 계산 프로그램]")
myGrade = 0
totUnit = 0
totGrade = 0
subjectCount = int(input("과목 수: "))
for i in range(subjectCount):
    print(i+1, end=" ")
    unit = int(input("과목 단위 수: "))
    grade = int(input("석차 등급: "))
    totUnit += unit                            #-> 단위수합=단위수합+단위수
    totGrade += grade*unit            #-> totGrade=등급*단위수
myGrade = totGrade/totUnit
print("내신 등급은", myGrade, "입니다.")
if myGrade <= 3:
    myLevel = "상위권"
elif myGrade <= 6:
    myLevel = "중위권"
else:
    myLevel = "하위권"
print("수준은",myLevel,"입니다.")






