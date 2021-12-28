# 연락처 하나를 표현하는 클래스.

class ContactInfo:
    # 생성자로 변수들이 뭐뭐 있는지 표현.
    def __init__(self, name, phone_num, memo):
        self.name = name
        self.phone_num = phone_num
        self.memo = memo