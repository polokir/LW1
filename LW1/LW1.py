class Student:

    def __init__(self, studentType, neededCredits, money):
        self.credits = 0
        self.money = money
        self.neededCredits = neededCredits
        self.type = studentType
        self.state = "studying"

    def command(self, text):
        if not text:
            return False
        command = text[:31].strip()
        arg = int(text[32:].strip())
        if command == "obtain scholarship":
            return self.obtainScholarship(arg)
        elif command == "obtain help":
            return self.obtainHelp(arg)
        elif command == "pay hostel":
            return self.payHostel(arg)
        elif command == "pay canteen":
            return self.payCanteen(arg)
        elif command.split()[0] == "teach":
            return self.teach(arg)

    def obtainHelp(self, amount):
        self.money += amount
        return True

    def obtainScholarship(self, amount):
        self.money += amount
        return True

    def payCanteen(self, amount):
        if self.money < amount:
            return self.dropOut()
        else:
            self.money -= amount
        return True

    def payHostel(self, amount):
        if self.money < amount:
            return self.dropOut()
        else:
            self.money -= amount
        return True

    def teach(self, creditsTeached):
        self.credits += creditsTeached
        if self.credits >= self.neededCredits:
            return self.graduate()
        return True

    def dropOut(self):
        self.state = "dropped out"
        return False

    def graduate(self):
        self.state = "graduated"
        return False

if name == "__main__":
    with open("input01.txt", "r") as file:
        student = Student(studentType=file.readline().strip(), neededCredits=int(file.readline()), money=int(file.readline()))
        while student.command(file.readline()):
            pass
        print(student.state)
