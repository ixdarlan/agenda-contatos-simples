from control import add_contact, all_contact, delete_contact, see_contact

schedule = []

while True:
    print('\nwhat do you want?\n'
          '[ 1 ] - create new contact\n'
          '[ 2 ] - see contact \n'
          '[ 3 ] - delete contact \n'
          '[ 4 ] - all contacts  \n'
          '[ 5 ] - close \n')
    quest = str(input('Type here: '))

    if quest == '1':
        name = input('name: ').upper()
        number = int(input('number: '))
        email = input('email: ')
        schedule.append(add_contact(name, number, email))

    elif quest == '2':
        name = input('name: ').upper()
        see_contact(schedule, name)

    elif quest == '3':
        name = input('name: ').upper()
        delete_contact(schedule, name)

    elif quest == '4':
        all_contact(schedule)

    elif quest == '5':
        break

    else:
        print('error')
