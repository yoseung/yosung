#1차시

#open은 단순 파일열기고, reader는 파일을 파이썬에서 이용하겠다는 뜻
# for문의 핵심은 데이터에서 한줄씩 실행한거를 여러번해서 붙여놓아서 집합값처럼 보이는거지 걍 단일값을 여러개 붙여놓은거임.
import csv

f=open("D:/강효승/temp_3.csv")

data=csv.reader(f)

data_list=[]

for row in data:
    data_list.append(row)
 
    
 #닐찌만 출력하기
data_list_2 = data_list[12:100]

for sim in data_list_2:
    print( sim[2] )
    
 
#최고기온중에서 최댓값 구하기

data_list_2 = data_list[12:100]

max=-999

for row in data_list_2:
    if max<float(row[4]):
        max=float(row[4])
        
print(max)

# 착각하지 말아야 될게 sim[4]는 기온값들의 집합값이 아니고 단일 기온값으로 하나임. 그래서 sim[4]=12.5 처럼 단일값과 똑같이 여겨짐.
# 근데 프린트 했을때 집합값으로 보이는건 for문을 돌려서 데이터의 마지막행까지 명령을 실행하는 반복문이라 그럼. 
# 그리고 얘가 단일값으로 리스트가 될수 없으니까 타입 잘 확인할것
# for문의 핵심은 데이터에서 한줄씩 실행한거를 여러번해서 붙여놓아서 집합값처럼 보이는거지 걍 단일값을 여러개 붙여놓은거임.


#파이썬 코드를 위에서 부터 순차적으로 코드를 번역하는데 오류발생하면 거기서 멈추고 에러메세지 나옴. 뒤에 오류없다라도 앞에서 나오면 멈춤.
#트라이 익셉트문은 트라이문을 수행하되 트라이문 안에서 있는 부분에서 에러나면 멈추지 말고 그 트라이문 오류부분만 익셉트 쪽으로 빠지고 뒤에 에러 없으면 다시 수행.
A=""

try:
    float(A)
except:
    print("오류발생")
    
    
#최고기온에서 오류나는 행들은 몇번째 인가
data_list_2= data_list[12: ]
counter=0
max=-999

for row in data_list_2:
    counter=counter+1
    try:
        if max<float(row[4]):
           max=float(row[4])
    except:
        print(counter)


#오류나는 행들이 뭐가 문제인지 확인해 줄수 있음. 여러개의 오류나는 행들중 걍 골라서 보는게 아래식.  
data_list_2[15963]


#그래서 최종 전체 데이터에서 최고기온중 최댓값 찾기

data_list_2= data_list[12: ]
counter=0
max=-999

for row in data_list_2:
    counter=counter+1
    try:
        if max<float(row[4]):
           max=float(row[4])
    except:
        print(counter)

print(max)


#최저기온중 최소값 구하기

data_list_4=data_list[12:]

min=1000
counter=0

for row in data_list_4:
    counter=counter+1
    try: 
        if min > float(row[6]):
          min=float(row[6])
            
    except: 
        print(counter)
        
print(min)
        

#최저기온중에서 최솟값의 날짜 찾아보기

#정석풀이-1
min=1000
counter=0
for row in data_list_4:
    try:
        if min>float(row[6]):
            min=float(row[6])
            min_idx=counter
    except:
        print(counter)
    counter=counter+1
data_list_4[min_idx]
        
#정석풀이-2
min=1000
counter=0
for row in data_list_4:
    counter=counter+1
    try:
        if min>float(row[6]):
            min=float(row[6])
            min_idx=counter
    except:
        print(counter)
data_list_4[min_idx-1]
    
#내가 푼거- 얘는 if조건문에 해당할때만 세는 거잖아. 정석은 if조건 해당 안될때도 세준다고.
#대신 포문 돌아갈때마다 업데이트 되는게 아니고 if 만족하면 업데이트 해준다게 차이점임
min=1000
counter=0
c=9
for row in data_list_4:
    try:
        if min> float(row[6]):
            min=float(row[6])
            counter=counter+1
    except:
        print(c)
    
data_list_4[counter-1]

 
#데이터에서 맨뒤에서 20번째까지 출력해보기   
low_data_list=data_list_2[-20: ] 
print(data_list_2)   
    
    
for row in low_data_list:
    print(row)
    
#뒤에서 11번째 바로 앞에까지. 우리가 출력한거에서 11번째부터가 불필요한 데이터였으니까
for row in low_data_list[:-11]:
    print(row)

    
#에이라는 변수안에 아이라이크 파이썬 라는 문자열이 구성요소로서 포함되어있니? 라는 질문임 
A="i like python"     
if "python" in A:
    print("1")
        

#내 생일의 최고기온과 최저기온 구하기
for row in data_list_2:
    if "2001-05-12" in row:
        print(row)
        print(row[4])
        print(row[6])


#내 생일의 월과 일에만 해당하는 최고와 최저기온 구하기,ㅎㅎ
for row in data_list_2:
    if "05-12" in (row[2]):
           print(row[2],"최고기온: ",row[4], "최저기온: ", row[6])      
      
    
       
#set 특성상 중복된 데이터를 허용하지 않음. 중복된 애들은 지움, 합집차집합에서 많이 씀.

A=[1,2,3,3,3,4,5,5]
B=set(A)
print(B)
B=list(set(A))
print(B)


#데이터의 형태 바꾸기, 일별 데이터를 월별 데이터로 바꾸기
#이거는 1907로 나오는게 아니라 리스트안에 리스트를 넣어서 ['1'.'2','5']] 이렇게 나옴
C=[]
D=[]
for row in data_list_2:
    for low in row[2]:
        D.append(low)
        C.append(D[:-3])
print(C)
        

 
#데이터의 형태 바꾸기, 일별 데이터를 월별 데이터로 바꿔서 최고기온중 최댓값, 최소기온 최솟값, 평균기온의 평균값 찾기
data_list_3 = data_list_2[:-11]             
list_month=[]
for row in data_list_3:
    list_month.append(row[2][:-3])        
print(list_month)  

#중복값 제거하기, 근데 순서가 바뀌어 보임. 
set_month=list(set(list_month))
set_month.sort()
print(set_month)
           
#리스트안에 리스트 넣어서 보기 편하게 하기
temp=[]
for row0 in set_month:
    high=-999
    low=999
    avg=0
    A=[]
    for row1 in data_list_3:
        if row0 in row1[2]:
            try:
                if float(row1[4]) > high:
                    high=float(row1[4])
                    
                if float(row1[6]) <low:
                    low=float(row1[6])
                    
                avg=avg+float(row1[3])
            except:
                print("error")
    A.append(row0)            
    A.append(high)
    A.append(low)
    A.append(avg/30)
    temp.append(A)
    
#더 예쁘게 정리해주는거                
df_A=ad.DataFrame(A,columns=["날짜", "최고기온","최저기온", "평균기온"])           

            




temp=[]
for row0 in set_month:
    high=-999
    low=999
    avg=0
    for row1 in data_list_3:
        if row0 in row1[2]:
            try:
                if float(row[4])>high:
                high=float(row1[4])
        
            if float(row1[6])>low:
                low=float(row1[6])
            avg=avg+float(row1[3])
            if counter=30:
                print(avg)
                
            
                
                
            


















