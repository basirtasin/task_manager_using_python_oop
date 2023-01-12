"""This Program Works with a Task manager Application.
Created by: Md. Samiul Basir
Email: turjotasin@gmail.com
"""
import string
from datetime import datetime
import random


charlist = [] #For unique id generation
charlist += string.ascii_letters #For unique id generation


#Function for print the Dictionary Values
def dic_print(item, cond = False): # Task No Will only print for case 5 & 6

    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if(cond==True):
        print(f"Task No - {item['id']}\n")
    print(f"ID - {item['id2']}\n"
          f"Task - {item['name']}\n"
          f"Created time - {item['created_time']}\n"
          f"Updated Time - {item['updated_time']}\n"
          f"Completed - {item['completed']}\n"
          f"Completed Time - {item['completed_time']}")
    print("----------------------------------------------------")
    print("\n\n\n")


class Task_Manager:

    def __init__(self):
        self.task_list = []

    def update_task(self, temp2, temp3):
        for item in self.task_list:
            if(item["id"]==int(temp2)):
                item["name"]=temp3
                item['updated_time']= datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def complete_task(self, id):
        for item in self.task_list:
            if(item["id"]==int(temp)):
                item["completed"]=True
                item['completed_time']= datetime.now().strftime("%d/%m/%Y %H:%M:%S")


all_task = Task_Manager() #Making a Class of Task Manager
id = 1; # This Will Work As the Task No
while(True):
    case = int(input('1. Add New Task \n'
                     '2. Show All Task \n'
                     '3. Show Incomplete Tasks\n'
                     '4. Show Completed Tasks\n'
                     '5. Update Task\n'
                     '6. Mark A Task Completed\n'
                     'Enter Option: '))

    if case ==1:
        new_task = input("Enter New Task ")
        #det_task Will Contain All the info of the task.
        det_task = {"name": new_task, "id":id, "id2":random.randint(100000, 10000000),
                    "created_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    "updated_time": "NA", "completed": False, "completed_time": "NA"}

        id= id+1

        all_task.task_list.append(det_task)

    elif case ==2:
        #This will print the every dictionary item from the list
        for item in all_task.task_list:
            dic_print(item)



    elif case ==3:
        for item in all_task.task_list:
            if(item['completed']==False):
                dic_print(item)



    elif case ==4:
        flag = 0;
        for item in all_task.task_list:
            if(item['completed']==True):
                flag =1
                dic_print(item)
        if flag ==0:
            print("No Completed Task!")


    elif case ==5:
        incompleted =0
        for item in all_task.task_list:
            if (item['completed'] == False):
                incompleted +=1

        if(incompleted>0):
            print("SELECT WHICH TASK TO UPDATE:")
            for item in all_task.task_list:
                if (item['completed'] == False):
                    dic_print(item, True)
            temp2 = input("Enter Task No: ")
            temp3 = input("Enter Updated Task Name: ")
            all_task.update_task(temp2, temp3)
        else:
            print("\n\nYou Dont have any Task for update!!!!!!\n\n")

    elif case ==6:
        incompleted =0
        for item in all_task.task_list:
            if (item['completed'] == False):
                incompleted +=1

        if(incompleted>0):
            print("SELECT WHICH TASK TO COMPLETE:")
            for item in all_task.task_list:
                if (item['completed'] == False):
                    dic_print(item, True)
            temp = input("Enter Task No: ")
            all_task.complete_task(temp)

        else:
            print("\n\n!!!YOU HAVE COMPLETED ALL TASK!!!\n\n")





"""
1
Tasin
1
Sleep
1
Tasin22


"""


