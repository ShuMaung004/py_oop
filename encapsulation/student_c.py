class Student:
    def __init__(self,name):
        self.__name = name          #Private Attribute
        self.__grades = []
    
    def add_grades(self,grade):
        if 0 <= grade <= 100:
            self.__grades.append(grade)
            print(f"Grade {grade} added for {self.__name}")
        else:
            print("Invalid grade! Must be between 0 and 100")
    
    def get_average(self):
        if len(self.__grades) == 0:
            return 0
        else:
            return sum(self.__grades)/len(self.__grades)

    def display_info(self):
        print(f"Student :  {self.__name}")
        print(f"Grades  :  {self.__grades}")
        print(f"Average :  {self.get_average():.2f}")
    
    def change_name(self,new_name):
        if new_name.strip():
            self.__name = new_name
        else:
            print("Invalid name!")
    
    def __str__(self):
        return f"{self.__name}"
    
    def __len__(self):
        return len(self.__grades)
    
    @staticmethod
    def checking_static():  #static method don't need self parameter
        print("this is static method")


# student1 = Student("Kevin")
# student1.add_grades(30)
# student1.add_grades(40)
# print(len(student1))

# student1.display_info()
# print(student1)
# Student.checking_static()



# if " ":
#     print("haha")
