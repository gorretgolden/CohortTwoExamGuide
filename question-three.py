#3(c)
class Gradebook:
    #constructor
    def __init__(self):
      self.gradebook = {} #empty dictionary
      self.user_tasks = ""


    #ask user for next task
    def ask_user_task(self):
   
     new_task = input("What would you like to do?: ").lower()
     self.user_tasks = new_task  

     
    def user_grades(self):
        name = input("Enter student name: ").lower()


        if name not in self.gradebook:
            print("A new student! Adding them to the gradebook...")
            self.gradebook[name] = []
        grades = input("Enter student grade(s): ").split(",")
            #storing user grades
        new_grades = [float(grade) for grade in grades]
        for grade in new_grades:
          self.gradebook[name].append(grade) 
        print("New entry complete!") 
        self.ask_user_task()

    def view_gradebook(self):#function to print the grade dictonary values
  
     print(self.gradebook)
     self.ask_user_task()

    def student_average(self):
    # """Prints the average value of each student's grade list."""
      for student, grade in self.gradebook.items():
       print(f"{student}: {(sum(self.gradebook[student]) / len(self.gradebook[student])):.2f}")
       self.ask_user_task()



#function to end the program  when the user quits      
def run():


 
  student_grades =Gradebook() #new gradebook instance
  student_grades.ask_user_task()
  
  while student_grades.user_tasks != "quit":
    
    # Checking for invalid task entry
    if student_grades.user_tasks not in ['add student', 'add grades', 'view gradebook', 'calculate averages']:
      print("Invalid entry, try a different task!")
      student_grades.ask_user_task()

    if student_grades.user_tasks in ["add student", "add grades"]:
      student_grades.user_grades() 

    if student_grades.user_tasks == "view gradebook":
      student_grades.view_gradebook()

    if student_grades.user_tasks == "calculate averages":
      student_grades.student_average()

  print("End of program")
  

run()  