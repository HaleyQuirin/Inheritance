import person as p

name = "Haley"
address = "1902 s 12th street"
phonenumber = "281-917-4734"
customer_number = 1234
on_list_flag = True

person1 = p.Person(name, address, phonenumber)

customer1 = p.Customer(name, address, phonenumber, customer_number, on_list_flag)

person1.print_person()

print()
print()
print()

customer1.print_person()
