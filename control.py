from contact import Contact


def add_contact(name, number, email):
    return Contact(name, number, email)


def see_contact(schedule, name):
    for num in schedule:
        if num.getName() == name:
            print(f"{num.getName()} | {num.getNumber()} | {num.getEmail()}")
            break
    else:
        print('name not found!')


def delete_contact(schedule, name):
    if len(schedule) != 0:
        cont = 0
        for num in schedule:
            if num.getName() == name:
                schedule.pop(cont)
                print(f'contact {num.getName} successfully removed!')
                break
            else:
                print('name not found!')
            cont += 1
    else:
        print('empty list')


def all_contact(agenda):
    for num in agenda:
        print(f'{num.getName()} | {num.getNumber()} | {num.getEmail()}')
