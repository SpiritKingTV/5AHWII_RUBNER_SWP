if __name__ == "__main__":
    class Person:
        def __init__(self, firstname, lastname, age, isMale):
            self.firstname = firstname
            self.lastname = lastname
            self.age = age
            self.isMale = isMale

    class Employee(Person):
        def __init__(self, firstname, lastname, age, gender, salary):
            super().__init__(firstname, lastname, age, gender)
            self.salray = salary

    class Leader(Employee):
        def __init__(self, firstname, lastname, age, gender, salary):
            super().__init__(firstname, lastname, age, gender, salary)

    class Department:
        def __init__(self, name):
            self.name = name

        leader = Leader("", "", 0, True, 0)
        employees = []

    class Company:
        departments = []


    l1 = Leader("Manuel", "Repetschnig", 18, True, 6600)

    e1 = Employee("Max", "Mustermann", 46, True, 1700)
    e2 = Employee("Maria", "Joseph", 2040, False, 10)
    e3 = Employee("Sophie", "Klostermann", 11, False, 1)

    d1 = Department("Manuels Pfuscherei")

    d1.leader = l1
    d1.employees.append([e1,e2, e3])
    c1 = Company()
    c1.departments.append([d1])

    def countDeps(com=Company()):
        return com.departments.count()

    def countEmp(com=Company()):
        count = 0
        for d in com.departments:
            for e in d:
                for a in e.employees:
                    count += len(a)
        return count

    def countLead(com=Company()):
        count = 0
        for d in com.departments:
            for e in d:
                if e.leader is not None:
                    count += 1
        return count

    def biggestDep(com=Company()):
        count = 0
        bigCount = 0
        dep = None
        for d in com.departments:
            for e in d:
                if e.leader is not None:
                    count += 1
                for a in e.employees:
                    count += len(a)
                if bigCount < count:
                    bigCount = count
                    dep = e
                count = 0
        return dep.name

    def howManyMen(com=Company()):
        ges = 0
        count = 0
        for d in com.departments:
            for e in d:
                if e.leader is not None:
                    if e.leader.isMale:
                        count += 1
                    ges += 1
                for a in e.employees:
                    for b in a:
                        if b.isMale:
                            count += 1
                        ges += 1

        return count / ges * 100

    print("Anzahl Mitarbeiter gesamt:",countEmp(c1)+countLead(c1))
    print("Davon Gruppenleiter:",countLead(c1))
    print("Größte Abteilung:",biggestDep(c1))
    print("Männerquote in Prozent:",howManyMen(c1), "%")