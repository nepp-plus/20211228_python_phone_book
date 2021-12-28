class ContactInfo:
    def __init__(self, name, phone_num, memo):
        self.name = name
        self.phone_num = phone_num
        self.memo = memo
        
    def print_contact_info(self):
        print(f'{self.name} : {self.phone_num} - {self.memo}')