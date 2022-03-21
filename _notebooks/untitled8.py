# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 15:07:00 2022

@author: HS
"""
# int는 정수로 소수점 없음 % d, float은 실수로 소수점 있음 %f. str은 문자(열)로 "" 해줌 %s

#A=[1,2,3,4,5,6,7,8,9,19]만들기 예제 포문과 에펜드 이용
A=[1,2,3,4,5]
B=[6,7,8,9,10]


for var in B:
    A.append(var)
    print(A)
    

#밑이 정답임 차이를 보여주기 위해 넣어놓음. 포문에서 A값은 한줄실행시마다 업데이트 되는거임.

A=[1,2,3,4,5]
B=[6,7,8,9,10]

for var in B:
    A.append(var)
    
print(A)
 
#위에꺼는 하면 []까지 포함되서 나옴. 두 풀이의 차이점은 여기서 나옴.
B=[6,7,8,9,10]
print(B)

for var in B:
    print(var)   
    
    

#인덱싱은 리스트의 요소에서 각각의 번호표를 부여하는 것이고 슬라이싱은 [~:~]해서 잘라내는거임. 0번째부터 시작하고 그 전까지 표시하라는거임.
#print A( [-3: -1]) 이거는 맨뒤에서 세번째 부터 맨뒤에꺼 전까지
#print A([ :-1]) 이면 맨앞에서 맨뒤에꺼 전까지임.



#최댓값을 구하는 방법
A=[3,20, 7,9,1]

maximum=-999
for row in A:
    if maximum < row:
        maximum=row
        
 print(maximum)
 
 
#Q의 타입확인기 print(type(A)) 또는 Q=type(A) 하고 print(Q)하기
 
#파이썬 코드를 위에서 부터 순차적으로 코드를 번역하는데 오류발생하면 거기서 멈추고 에러메세지 나옴. 뒤에 오류없다라도 앞에서 나오면 멈춤.
#트라이 익셉트문은 트라이문을 수행하되 트라이문 안에서 있는 부분에서 에러나면 멈추지 말고 그 트라이문 오류부분만 익셉트 쪽으로 빠지고 뒤에 에러 없으면 다시 수행.
A=""

try:
    float(A)
except:
    print("오류발생")
 
# 역슬래쉬와 n은 엔터역할
 
 #함수len은 데이터의 구성요소를 세주는 역할함. b=[1,3,"가나"."초"]에서 len(b) 하면 4나옴.
 #문자열은 문자들이 구성요소임. a="pyhin"
 #중괄호 안에잇는게 변수다?
 # int는 정수로 % d, float은 실수로 %f. str은 문자(열)로 "" 해줌 %s
 for row in range(10):
     A=f"i eat {row} appples"
     print(A)
     
  for row in range(10):
     A="i eat %d appples" %row
     print(A)


#여기서 b가 몇개있냐    
 a="hobby"
 print(a.count("b"))
 #인덱스위치로 o문자 제일 먼저있는 인덱스 값 찾아줌
  print(a.find("o"))
 
  
 #슬라이싱과 파인드 이용해 공백위치의 인덱스값 찾기 , "you love java"
 #result = a.find(" ") 이게 맞지 result = print(a.find(" ")) 일케 하면 안됨. 프린트문의 목적은 콘솔창에 나타내기 위한것임.
a="i like python"

print(a.find(" "))
result = a.find(" ")
print( a[result+1: ].find(" ") + result +1 )


#어떤 문자열이 와도 그 공간의 공백수 찾아주기
#풀이-1
a="i like python"
temp=0
counter=0
for row in range(len(a)):
    idx_1=  a.find(" ")
    counter=counter+1
    if idx_1==-1:
        break
    else:
        a = a[idx_1+1 : ]
        temp=idx_1 +temp
        if counter == 1:
            print(temp)
        else:
            print(temp+1)

#플이-2:: 공백대신 i 찾기
a="i like python"
temp=[]
for row in range(len(a)):
    idx_1=  a.find("i")
    if idx_1==-1:
        break
    else:
        if len(temp)==0:
            temp.append(idx_1)
        else:
            temp.append(idx_1+temp[len(temp)-1]+1)
        a = a[idx_1+1 : ]
print(temp)
        
 

 #해당 문자열에서 없는거 찾으라하면 -1이 나옴. a.find("q")하면 -1 리턴됨. 공백 찾으라는데 공백이 없으면 -1 나옴.

var = "p y c"
result = var.find(" ")
print(result)

#리스트와 문자열 사이에서 구성요소의 차이 

#조인은 각 구성요소 사이에 해당 그 문자를 넣어줌

#스트립 특징이 특정문자를 다지우는게 아니고 지우다가 특정문자가 아닌게 나오면 멈춤.
#왼쪽부터 오면서 혹시 공백있으면 지워달라는게 lstrip, 오른쪽이 rstrip, 양쪽에서 오면서 공백지우느게 strip
#기본이 공백이고(아무것도 안써줬을때가) 특정 지우고 싶은거 있으면 써주면 됨.

#스플릿과 리플레이스

#팝: 뒤에있는걸 빼서 리턴해줌,신기하게 a가 줄어듬:난 a는 안변할거라 생각해서
a=[1,2,3]
b=a.pop()
print(a)
print(b)

#append는 통쩨로 요소 하나로서 추가되고, extend는 인풋값의 요소들을 요소로서 추가되는거임. 

#튜플은 단일값이 아니고 대괄호아닌 소괄호로 묶음, 튜플은 값을 삭제하거나 수정불가, 추가만 가능

#오더와 언오더 차이는 인덱스, 딕셔너리는 언오더로 키값과 벨류값을 가짐. 키값과 벨류값이 짝꿍으로 그게 하나의 구성요소임. 
#딕셔너리는 벨류값에 접근하려면 그 벨류값의 키값으로 접근해야함. 인덱스가 중복될수 없는것처럼 키값도 중복안되는 고유값임.

#리스트[], 튜플(), 집합{}, 딕셔너리{}//집합과 딕셔너리 구분시 쌍여부로 구분하기
{1:3,4:5}

#어떤 문자열이 와도 그 공간의 공백수 찾아주기
#풀이-1
a="i like python"

print=a.find((" "))


#자료형의 참과 거짓 어떤 조건이 나오지 않고 단일변수 하나만 나오면 참과 거짓의 판단여부는 자료형에 따라 달라짐
#문자열안에 어떤 문자가 하나라도 있으면 참임. " ", []이거는 거짓임.
#정수면 0나오면 거짓이고 0아니면 참임.
a=[]
if a:
    print("1")

 
#리스트안에 소분화로 리스트 넣기; randge는 1부터 9까지. 첫번째부터가 아니라 1이라는 값을 넣어준다는 거임
result=[]
temp=[]
for row in range(1,10):  
    temp.append(row)
    if row % 3 == 0:
        result.append(temp)
        temp=[] 
 
 
#우리가 생각한것과 다른 코딩의 흐름: b=a, b=a.copy()의 차이점
a=[1,2,3]
b=a
a[1]=10
print(a)
print(b)

a=[1,2,3]
b=a.copy()
a[1]=10
print(a)
print(b)


#
a='a:b:c:d'
b=a.replace(":","#")
print(b)


 #솔트는 원본 데이터를 바꿔주는 거지 다른변수로 리턴해주는게 아님. //원본 데이터와 원본 데이터 리턴이 다른게 많으..리턴값과 원본 데이터 바꾸기
 a=[1,2,5,4,3]
 a.sort()
 a.reverse()
 print

#조인함수: 지정 문자를 요소들 사이에 넣어줌; input의 요소 사이에 넣어줌
a=" "
input=['life', 'is', 'too', 'short']
print(a.join(input))


#b=(4)라고 하면 인트로 정수로 받아들임 b=(4,)라고 써줘야 튜플로 인식
#솔트하고 리스트로 다시 왜 묶어줌?














 
 
 
 
 
 
 
