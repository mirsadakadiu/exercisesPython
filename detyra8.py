from datetime import datetime as dt

class Member:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.expireDate = dt.today + 365
        self.secretCode = ""

    def show_expiryDate(self):
        return f"{self.firstName} {self.lastName}'s account expires on: {self.expireDate}"


class Admin(Member):
    def __init__(self, firstName, lastName):
        super.__init__(self, firstName, lastName)


class User(Member):
    pass



first_user = Member("John", "Doe")

print(first_user.show_expiryDate())

second_user = Admin("Anna", "West")
print(second_user)

third_user = User("Jack" "East")
print(third_user)