class Person:
    def __init__(self, name, address, phonenumber):
        self.__name = name
        self.__address = address
        self.__phonenumber = phonenumber

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phonenumber(self):
        return self.__phonenumber

    def print_person(self):
        print("Name:", self.__name)
        print("Address:", self.__address)
        print("Phone Number:", self.__phonenumber)


class Customer(Person):
    def __init__(self, name, address, phonenumber, customer_number, on_list):
        Person.__init__(self, name, address, phonenumber)
        self.__customer_number = customer_number
        self.__on_list = on_list

    def print_person(self):
        Person.print_person(self)

        print(f"Customer Number: {self.__customer_number}")
        if self.__on_list:
            print("On Mailing List: YES")
        else:
            print("On Mailing List: NO")
