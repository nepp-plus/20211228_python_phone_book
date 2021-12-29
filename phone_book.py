from time import sleep

from datas import ContactInfo

def print_menu():
    print('===== 전화번호부 =====')
    print('1. 전화번호 등록')
    print('2. 전화번호 목록 조회')
    print('3. 모든 연락처 삭제')
    print('4. 연락처 상세 조회')
    print('5. 특정 연락처 삭제')
    print('0. 프로그램 종료')
    print('=====================')
    input_num = int( input('메뉴 선택 : ') )
    
    return input_num

def add_phone_num():
    name = input('이름 : ')
    phone_num = input('전화번호 : ')
    memo = input('특이사항 : ')
    
    with open('phone_book.csv', 'a') as file:
        input_line = f'{name},{phone_num},{memo}\n'
        file.write(input_line)
        
    print('전화번호 등록이 완료되었습니다.')
    sleep(2)
        

def show_all_phone_num():
    with open('phone_book.csv', 'r') as file:
        line_list = file.readlines()
        
        for line  in  line_list:
            
            line = line.strip()
            info_list = line.split(',')
            contact = ContactInfo(info_list[0], info_list[1], info_list[2])
            contact.print_contact_info()
            
        sleep(2)
        
def remove_all():
    with open('phone_book.csv', 'w') as f:
        pass
 
    print('모든 연락처가 삭제되었습니다.')
    sleep(2)
    
def search_and_view_contact():
    print('------ 사용자 검색 ------')
    search_name = input('조회할 사용자 이름 : ')
    
    with open('phone_book.csv', 'r') as file:
        line_list = file.readlines()
        
        for line in line_list:
            line = line.strip()
            if f'{search_name},' in line:
                infos = line.split(',')
                contact = ContactInfo(infos[0], infos[1], infos[2])
                contact.print_contact_info_detail()
                sleep(2)
                
                
# 몇번째 연락처를 지울건지 -> 그 위치의 연락처 삭제.
def remove_contact_by_position():
    # 지우고 싶은 위치를 입력받자.
    position = int( input('몇번째 연락처를 삭제하겠습니까? (1부터 시작) : ') )
    # 그 위치의 연락처가 누구인지? 이름 => 확인 받자.
    
    # 파일의 목록에서는 0번째부터 시작.
    position -= 1  # 입력값 보정
    
    with open('phone_book.csv', 'r') as f:
        # readlines 활용 => 한줄씩 목록으로.
        contact_list = f.readlines()
        # 특정 위치의 연락처만 다뤄보자.
        target_contact = contact_list[position]
        
        print(target_contact)