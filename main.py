from phone_book import print_menu, add_phone_num, show_all_phone_num

from time import sleep

while True:
    
    # 메뉴 출력 기능 -> 입력값이 뭔지 알려줌.
    # num에 담아두고 활용할 준비.
    num = print_menu()

    if num == 0:
        print('프로그램을 종료합니다.')
        break
    elif num == 1:
        add_phone_num()
    elif num == 2:
        show_all_phone_num()
    else:
        print('잘못된 입력입니다. 다시 입력해주세요.') 
        sleep(2)
        