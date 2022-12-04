# data
names = ['salman','Amal','sarah','malik','lamar','mohammed','praneeth','sivamani','Gautam Giri','vamshi','Hari','surendra']
numbrs = [7487689756,9125470875,6578749476,9745286380,7401235467,9468263407,7451983476,7013341668,6372174006,7346824543,6369314118,9571270392]
def enter_name():
    while True:
        try:
            name = (input('enter name:'))
        except ValueError:
            print('sorry enter only name')
            continue
        else:
            break
    try:
        va1 = names.index(name)
        print(names[va1], numbrs[va1])
    except ValueError:
        print('the name you entered is not found')
def save_number():
    print('save new number')
    new_name = input('add the name:')
    names.append(new_name)
    new_number = int(input('add the number:'))
    numbrs.append(new_number)
    print('the nunber that you saved is:','\n',new_name,new_number)
def chose():
    while True:
        ch1 = input('save new contact or search:')
        if ch1 == 'search':
            while True:
                    enter_name()
                    break
            else:
                print('enter only "name"')
        elif ch1 == 'save new contact':
            save_number()
            break
        else:
            print('type only "new" or "search"')

while True:
    chose()