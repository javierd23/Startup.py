import random
#This a program to choose meeting time randomly for different employees.

class MeetingTime:
    def __init__(self):
        self.meeting_time = ['8:00, 9:00', '9:00, 10:00', '10:00, 11:00', '11:00, 12:00',
                        '12:00, 13:00', '13:00, 14:00', '14:00, 15:00', '15:00, 16:00',
                        '16:00, 17:00', '17:00, 18:00', '18:00, 19:00', 'End'] #THIS END IS TO BE ABLE TO HAVE THE LAST CHOISE.
        self.emp_time = {}

    def meeting_assigment(self,  emp_name):
        if len(self.meeting_time) == 1:
            print('Just one more schedule available!')

        meeting = random.choice(self.meeting_time)
        self.emp_time[emp_name] = meeting
        self.meeting_time.remove(meeting)


    def show_schedule(self):
        print("Assigned Meeting Times")
        for names, times in self.emp_time.items():
            print(names, times)


scheduler = MeetingTime()

while True:
    name = input("Name: ")
    if name.lower() ==  'q': #once all the employees have been assigned, please exit with q
        break
    scheduler.meeting_assigment(name)
scheduler.show_schedule()






