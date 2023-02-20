class Person:
    def __init__(self, name, address, phonenumber):
        self.__name = name
        self.__address = address
        self.__phonenumber = phonenumber

    def print_person(self):
        print("Name: ", self.__name)
        print("Address: ", self.__address)
        print("Phone Number: ", self.__phonenumber)


class Customer(Person):
    def __init__(self, name, address, phonenumber, customer_number, boolean_data):
        self.__name = name
        self.__address = address
        self.__phonenumber = phonenumber
        self.__customer_number = customer_number
        self.__boolean_data_attribute = boolean_data

    def print_person(self):
        print("Name: ", self.__name)
        print("Address: ", self.__address)
        print("Phone Number: ", self.__phonenumber)
        print("Customer Number: ", self.__customer_number)
