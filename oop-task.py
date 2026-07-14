# 1️⃣

class Texnika:

    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}")



class Notebooks(Texnika):
    def __init__(self, brand, model, type, video_card, ram, display):
        super().__init__(brand, model, type)

        self.video_card = video_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type} VideoCard: {self.video_card}, Ram: {self.ram}, Display: {self.display}")


class Televisions(Texnika):
    def __init__(self, brand, model, type, size, display):
        super().__init__(brand, model, type)

        self.size = size
        self.display = display


    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Size: {self.size}, Display2: {self.display}")


class Smartphones(Texnika):

    def __init__(self,brand, model, type, size, sim_count):
        super().__init__(brand, model, type)

        self.size = size
        self.sim_count = sim_count

    def more_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Size: {self.size}, SimCount: {self.sim_count}")




# 2️⃣

class Transport:

    def __init__(self, brend, model, type):
        self.brend = brend
        self.model = model
        self.type = type

    def info(self):
        print(f"Brend - {self.brend} Model - {self.model} Type - {self.type}")

class Elektr_Cars(Transport):

    def __init__(self, brend, model, type, battery_life,charging_time):
        super().__init__(brend, model, type)

        self.battery_life = battery_life
        self.charging_time = charging_time

    def more_info(self):
        print(f"Brand - {self.brend} Model - {self.model} Type - {self.type} BatteryLife - {self.battery_life} Charging Time - {self.charging_time}")


class Super_Cars(Transport):
    def __init__(self, brend, model, type, motor, color ):
        super().__init__(brend, model, type)

        self.motor = motor
        self.color = color

    def more_info(self):
        print(f"Brand - {self.brend} Model - {self.model} Type - {self.type} Motor - {self.motor} Color - {self.color}")


class Truck(Transport):

    def __init__(self, brend, model, type, motor, height, long, wieght):
        super().__init__(brend, model, type)

        self.motor = motor
        self.height = height
        self.long = long
        self.wieght = wieght

    def more_info(self):
        print(f"Brand - {self.brend} Model - {self.model} Type - {self.type} Height - {self.height} Long - {self.long} WIeght - {self.wieght}")





# 3️⃣.1

class University:

    def __init__(self, university):
        self.university = university

    def info(self):
        print(f"University {self.university}")


class Staff(University):

    def __init__(self, university, first_name, last_name, age):
        super().__init__(university)

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def staff_info(self):
            print(f"University {self.university} FirstName {self.first_name} LastName {self.last_name} Age = {self.age}")



class Student(Staff):

    def __init__(self, university, first_name, last_name, age, group):
        super().__init__(university, first_name, last_name, age)

        self.group = group

    def more_info(self):
        print(f"University {self.university} FirstName {self.first_name} LastName {self.last_name} Age = {self.age} Group {self.group}")


class Teacher(Staff):

    def __init__(self, university, first_name, last_name, age, position, subject):
        super().__init__(university, first_name, last_name, age)

        self.position = position
        self.subject = subject

    def more_info(self):
        print(f"University {self.university} FirstName {self.first_name} LastName {self.last_name} Subject {self.subject} Position {self.position}")


class Other_Staff(Staff):

    def __init__(self, university, first_name, last_name, age, position):
        super().__init__(university, first_name, last_name, age)

        self.position = position

    def more_info(self):
        print(f"University {self.university} FirstName {self.first_name} LastName {self.last_name} Position {self.position}")




# # 3️⃣.2

class Object(University):

    def __init__(self, university,name):
        super().__init__(university)

        self.name = name

    def info(self):
        print(f"University {self.university}")

class Computer(Object):

    def __init__(self, university, name, soni,tizimi,holati):
        super().__init__(university, name)

        self.name = name
        self.soni = soni
        self.tizimi = tizimi
        self.holati = holati

    def object_more_info1(self):
        print(f"University - {self.university}  Nomi {self.name} Soni - {self.soni}, Tizimi - {self.tizimi} Holati {self.holati}")



class Mebel(Object):

    def __init__(self, university, name, soni, turi, holati):
        super().__init__(university, name)

        self.soni = soni
        self.turi = turi
        self.holati = holati

    def object_more_info2(self):
        print(f"University - {self.university} Name - {self.name} Soni {self.soni} Turi {self.turi}  Holati {self.holati} Name {self.name}")
