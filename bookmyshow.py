def single_ton(cls):
    l=[]
    def inner():
        if len(l)==0:
            obj=cls()
            l.append(obj)
        return l[0]
    return inner

@single_ton
class salaar:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('enter no of tickects: '))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('tickets booked sucessfully')
        else:
            print('tickets not available')
@single_ton
class kalki:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('enter no of tickects: '))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('tickets booked sucessfully')
        else:
            print('tickets not available')
@single_ton           
class og:
    def __init__(self):
        self.tickets=300
    def booking(self):
        tickets=int(input('enter no of tickects: '))
        if self.tickets>=tickets:
            self.tickets-=tickets
            print('tickets booked sucessfully')
        else:
            print('tickets not available')
while True:
    print('1) salaar\n2) og\n3) kalki')
    option=int(input('choose an option: '))
    if option==1:
        s1=salaar()
        s1.booking()
        print('-'*30)
    elif option==2:
            o1=og()
            o1.booking()
            print('-'*30)
    elif option==3:
            k1=kalki()
            k1.booking()
            print('-'*30)
    else:
        print('choose valid option')
    
