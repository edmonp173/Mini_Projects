class Student:
    def __init__(self, id, name):
        self.name = name
        self.__grades = []
        self.id = id
        

    def print_data(self):
        print(f"name: {self.name}, id: {self.id}, grades: {self.__grades}")
 
    def add_grade(self,grades):
        for i in grades:
          if int(i) <= 100:
             self.__grades.append(i)
          
   
    def avg_grades(self):
        mult = sum(self.__grades) / len(self.__grades)
        print(f"this is the sum:  {mult}")

per1 = Student("112", "avi")
grades = [80, 90, 100, 77]
per1.add_grade(grades)
per1.print_data()
per1.avg_grades()

