class Contact:
    def __init__(self, name, number, email):
        self.__name = name
        self.__number = number
        self.__email = email

    def getName(self):
        return self.__name
    
    def getNumber(self):
        return self.__number

    def getEmail(self):
        return self.__email
    