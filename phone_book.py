from time import sleep

from datas import ContactInfo

def print_menu():
    print('===== 전화번호부 =====')
    print('1. 전화번호 등록')
    print('2. 전화번호 목록 조회')
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