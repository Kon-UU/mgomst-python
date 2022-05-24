import requests
CUR_HEAD = requests.get('https://cyine.xyz/ebsi/currenthead.json').json()
L = ['blnk', 'kor', 'eng', 'math', 'his', 'st', 'sct', 'jt']

print(CUR_HEAD)

def st1():

    print("1. 고1, 2. 고2")
    inp = input("번호를 입력 : ")

    if inp == '1':
        r = requests.get('https://cyine.xyz/ebsi/go1.json').json()

        print(f"1. 국어 - 자료 수 : {len(r['kor'])}개")       
        print(f"2. 영어 - 자료 수 : {len(r['eng'])}개") 
        print(f"3. 수학 - 자료 수 : {len(r['math'])}개") 
        print(f"4. 국사 - 자료 수 : {len(r['his'])}개") 
        print(f"5. 사탐 - 자료 수 : {len(r['st'])}개") 
        print(f"6. 과탐 - 자료 수 : {len(r['sct'])}개")
        inp = int(input("번호를 입력 : "))
        

        print(f"자료 범위 : {r[L[inp]][0]['ym']} ~ {r[L[inp]][len(r[L[inp]]) - 1]['ym']}")
        inp_2 = input("년월을 입력(YYYYMM) : ")
        st2(L[inp], inp_2, r)


    elif inp == '2':

        r = requests.get('https://cyine.xyz/ebsi/go2.json').json()
        print(f"1. 국어 - 자료 수 : {len(r['kor'])}개")       
        print(f"2. 영어 - 자료 수 : {len(r['eng'])}개") 
        print(f"3. 수학 - 자료 수 : {len(r['math'])}개") 
        print(f"4. 국사 - 자료 수 : {len(r['his'])}개") 
        print(f"5. 사탐 - 자료 수 : {len(r['st'])}개") 
        print(f"6. 과탐 - 자료 수 : {len(r['sct'])}개")
        print(f"7. 과탐 - 자료 수 : {len(r['jt'])}개")
        inp = input("번호를 입력 : ")

        print(f"자료 범위 : {r[L[inp]][0]['ym']} ~ {r[L[inp]][len(r[L[inp]]) - 1]['ym']}")
        inp_2 = input("년월을 입력(YYYYMM) : ")
        st2(L[inp], inp_2, r)

def st2(sub, yyyymm, data):

    for i in range(len(data[sub])):
        if data[sub][i]['ym'] == yyyymm:
            print(f"{data[sub][i]['fullname']}\n문제지 링크 : {CUR_HEAD + data[sub][i]['munlink']}\n해설지 링크 : {CUR_HEAD + data[sub][i]['hsjlink']}\n")
            input("Enter 를 눌러서 처음으로.")
            st1()
    print("해당 학습지를 찾지 못했습니다.")
    input("Enter 를 눌러서 처음으로.")
    st1()

#Start 
st1()
