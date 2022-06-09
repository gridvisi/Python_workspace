
#


List = []
class append_op():

    def __init__(self,init,next):
        self.init = init
        self.next = next
    @property
    def appends(self):
        return self.init + self.next


start = []
old = append_op([],[1,2,3])

old.init = []
old.next = [1,2,3]

ans = old.appends
print(ans)

# append-> print
class myClass:
    def __init__(self):
        self.x = []
        self.x.append(1)

    def print_x(self):
        print(self.x)


obj1 = myClass()
obj1.print_x()  # prints [1]
obj2 = myClass()
obj2.print_x()  # prints [1],  not "[ 1, 1]"

ans = []
obj3 = myClass()
for i in range(3):
    #ans += obj3.print_x()
    #ans.extend(obj3.print_x())
    #ans.append()
    temp = obj3.print_x()
    print("### print ###")
    ans.append(temp)    # print not return!!!
print(ans)



# append-> print
class myClass:
    def __init__(self):
        self.x = []
        self.x.append(1)

    def print_x(self):
        return self.x + [2]


obj1 = myClass()
obj1.print_x()  # prints [1]
obj2 = myClass()
obj2.print_x()  # prints [1],  not "[ 1, 1]"

ans = []
obj3 = myClass()
for i in range(3):
    #ans += obj3.print_x()
    ans.extend(obj3.print_x())
    #ans.append(obj3.print_x())
    #temp = obj3.print_x()
    print("*** return ***")
    #ans.append(temp)    # print not return!!!
print(ans)




#case 1st
class School:
    def student(self):

        print("Welcome to Havard")

havard = School()
havard.student()


class School:

    def student(self):
        self.name = "Pramod"  # instance attribute
        age = 19
        print("Welcome to Havard:", self.name)
        print("Are you {} years old?".format(age))

havard = School()
havard.student()


class School:

    def student(self):
        self.name = "Pramod"  # instance attribute
        age = 19
        print("Welcome to Havard:", self.name)
        print("Are you {} years old?".format(age))

    def student_form(self):
        print("Name:", self.name)
        print("Age:" '#age')


havard = School()
havard.student()
havard.student_form()


class School:

    def student(self):
        self.name = "Pramod"  # instance attribute
        age = 19
        print("Welcome to Havard:", self.name)
        print("Are you {} years old?".format(age))

    def student_form(self):
        print("Name:", self.name)
        print("Age:", '#age')


havard = School()
#havard.student_form()


class School:

    def __init__(self):
        self.name = "Pramod"  # instance attribute
        self.age = 19

    def student_form(self):
        print("Name:", self.name)
        print("Age:", self.age)


havard = School()
havard.student_form()


class School:

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age

    def student_form(self):
        print("Name:", self.name)
        print("Age:", self.age)


havard = School("Pramod", 19)
havard.student_form()

# second object which differs from any other objects created
berkley = School("Quora", 10)
berkley.student_form()