from person import Person

class Client(Person):
    def __init__(self, first_name, last_name, adress, cell_phone, email, gender):
        super().__init__(first_name, last_name)
        self._adress = adress
        self._cell_phone = cell_phone
        self._email = email
        self._gender = gender