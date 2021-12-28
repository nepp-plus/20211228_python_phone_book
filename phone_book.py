from time import sleep

# 실질적인 동작 관련 코드들을 함수로 갖고있는 파일. (모듈)

# 메뉴 출력하고 / 입력값을 돌려받는 기능.

def print_menu():
    print('===== 전화번호부 =====')
    print('1. 전화번호 등록')
    print('2. 전화번호 목록 조회')
    print('0. 프로그램 종료')
    print('=====================')
    input_num = int( input('메뉴 선택 : ') )
    
    # 입력한 결과를 함수의 결과로 return
    return input_num

# 이름/폰번/메모사항  세가지 데이터를 입력받아 => 파일에 추가 저장.
def add_phone_num():
    # 세가지 데이터 입력 : 세 항목 모두 str 으로 받자.
    name = input('이름 : ')
    phone_num = input('전화번호 : ')
    memo = input('특이사항 : ')
    
    # 전화번호부 파일에 한줄로 추가.  이름,폰번,메모  양식으로 추가해보자.
    # with 구문 => 파일 열고 / 닫기 자동.
    with open('phone_book.csv', 'a') as file:
        # .csv : 이름,폰번,메모  처럼 ,를 이용해서 칸 구분 => 엑셀에서 표 형태로 표현 가능.
        
        input_line = f'{name},{phone_num},{memo}\n'  # 3개의 데이터를 한줄로 ,로 붙여줌. + 다음줄로 내려주기
        file.write(input_line)
        
    # 안내 문구
    print('전화번호 등록이 완료되었습니다.') # 2초가량 대기 후 메뉴
    sleep(2)
        