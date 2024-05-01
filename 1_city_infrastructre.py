# Task 1: Vehicle Registration System

class Vehicle():
    def __init__(self, reg_number, v_type, owner):
        self.reg_number = reg_number
        self.v_type = v_type
        self.owner = owner

    def get_info(self):
        print(f"\n{self.owner} is the current owner for {self.v_type} registration number: {self.reg_number}.")
    
    def update_owner(self, new_owner):
        print(f"\n{new_owner} is now the new vehicle owner for {self.v_type} registration number: {self.reg_number}")
        self.owner = new_owner

honda = Vehicle('V12345', 'SUV', 'John')
honda.get_info()

honda.update_owner('Joshua')
honda.get_info()

# Task 2: Event Management System Enhancement

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.current_guests = 0

        def get_participant_count(self):
            print(f"\n Current guests invited to the BBQ: {self.current_guests}")
            return self.current_guests

        def add_new_guest(self, guest_name):
            self.current_guests += 1
            print(f"\nNew total of guests invited to the BBQ: {self.current_guests}")
            

bbq = Event('Beach BBQ Day', '05/12/24')
bbq.get_participant_count()

bbq.add_new_guest('Cristina')
bbq.add_new_guest('Sean')
bbq.add_new_guest('Jaime')
bbq.add_new_guest('Crystal')
bbq.add_new_guest('Justin')

bbq.get_participant_count()