import requests
CUR_HEAD = requests.get('https://cyine.xyz/ebsi/currenthead.json').json()
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
        inp = input("번호를 입력 : ")
        
        if inp == '1':
            print(f"자료 범위 : {r['kor'][0]['ym']} ~ {r['kor'][len(r['kor']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('kor', inp, r)
        elif inp == '2':
            print(f"자료 범위 : {r['eng'][0]['ym']} ~ {r['eng'][len(r['eng']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('eng', inp, r)
        elif inp == '3':
            print(f"자료 범위 : {r['math'][0]['ym']} ~ {r['math'][len(r['math']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('math', inp, r)
        elif inp == '4':
            print(f"자료 범위 : {r['his'][0]['ym']} ~ {r['his'][len(r['his']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('his', inp, r)
        elif inp == '5':
            print(f"자료 범위 : {r['st'][0]['ym']} ~ {r['st'][len(r['st']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('st', inp, r)
        elif inp == '6':
            print(f"자료 범위 : {r['sct'][0]['ym']} ~ {r['sct'][len(r['sct']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('sct', inp, r)

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

        if inp == '1':
            print(f"자료 범위 : {r['kor'][0]['ym']} ~ {r['kor'][len(r['kor']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('kor', inp, r)
        elif inp == '2':
            print(f"자료 범위 : {r['eng'][0]['ym']} ~ {r['eng'][len(r['eng']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('eng', inp, r)
        elif inp == '3':
            print(f"자료 범위 : {r['math'][0]['ym']} ~ {r['math'][len(r['math']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('math', inp, r)
        elif inp == '4':
            print(f"자료 범위 : {r['his'][0]['ym']} ~ {r['his'][len(r['his']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('his', inp, r)
        elif inp == '5':
            print(f"자료 범위 : {r['st'][0]['ym']} ~ {r['st'][len(r['st']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('st', inp, r)
        elif inp == '6':
            print(f"자료 범위 : {r['sct'][0]['ym']} ~ {r['sct'][len(r['sct']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('sct', inp, r)
        elif inp == '7':
            print(f"자료 범위 : {r['jt'][0]['ym']} ~ {r['jt'][len(r['jt']) - 1]['ym']}")
            inp = input("년월을 입력(YYYYMM) : ")
            st2('jt', inp, r)

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
