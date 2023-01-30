class User:
    def __init__(self, uid, name, surname, email, password, certificate):
        self.uid = uid
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.certificate = certificate

    def __str__(self):
        return f'Hi! my name {self.name} and the my surname is {self.surname} A.K.A {self.uid}'
