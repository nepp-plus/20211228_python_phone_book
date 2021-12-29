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
        
        # 범위를 벗어나는 위치 => 해당 위치의 연락처는 없습니다. 메뉴로 돌아가게.
        if position >=  len( contact_list ) or  position < 0 :
            print('해당 위치의 연락처는 없습니다.')
            # 연락처 삭제 기능 (함수 or 메쏘드) 강제 종료.
            return  # 이 함수의 결과가 여기서 나온다고 지정. => 밑의 코드들은 실행되지 않게 처리.
        
        # 특정 위치의 연락처만 다뤄보자.
        target_contact = contact_list[position].strip()  
        infos = target_contact.split(',')
        
    # 연락처 객체로 변환.
    remove_contact = ContactInfo( infos[0], infos[1], infos[2] )
    
    # 이 사람을 삭제하고싶은게 맞는지? 확인받아보자.
    confirm = input(f'정말 {remove_contact.name} 연락처를 삭제하겠습니까? (y/n) : ')
    
    # y로 실제 삭제만 코딩
    if confirm == 'y':
        
        # 지울 사람만 빼고, 나머지 인원들이 추가되도록 파일을 새로 작성.
        with open('phone_book.csv', 'w') as f:
            # 읽기 모드에서 가져온 연락처 정보 (이름,폰번,메모) str 을 불러내보자.
            for line  in contact_list:
                #  line - '이름,폰번,메모\n'  정보가 들어있을예정.
                #  remove_contact의 폰번을 => 불러낸 line이 포함하고 있는가? 맞으면 삭제 (추가 X)
                
                # 삭제할 대상이 아니어야 => 파일에 내용 추가
                if  remove_contact.phone_num  not in  line:
                    f.write(line)  # 가공이 끝난 상태의 str => 그대로 파일의 내용으로 기록.
                    
        # 삭제 완료 안내 2초간
        print('해당 연락처는 삭제되었습니다.')
        sleep(2)
        