# data validation creating objects of each row of csv file:- 

import csv
from generate_pdf import getData

workout_data=[]
i=0

# main class for content of certificate: 
class Workout:
    def __init__(self, name, course, sId, emailId, semester, date):
        self.name = name
        self.course = course
        self.sId = sId
        self.emailId = emailId
        self.semester = semester
        self.date = date 

# main logic of code: 
def processFile(csv_file_path):
    global workout_data
    Local_workout_data = []

    with open(csv_file_path, 'r') as file:
        csv_reader=csv.DictReader(file)
        
        for row in csv_reader:
            # removing Nan values from '0.0'
            name = str(row["Name"]) if row["Name"] else " "
            course = str(row["Course"]) if row["Course"] else " "
            sId = str(row["ID"]) if row["ID"] else " "
            emailId = str(row["email"]) if row["email"] else " "
            semester = str(row["Semester"]) if row["Semester"] else " "
            date = str(row["Date"]) if row["Date"] else " "

            # duration = float(row["Duration"]) if row["Duration"] else 0.0
            # pulse=float(row["Pulse"]) if row["Pulse"] else 0.0
            # maxpulse=float(row["Maxpulse"]) if row["Maxpulse"] else 0.0
            # calories=float(row["Calories"]) if row["Calories"] else 0.0

            workout_obj= Workout(name, course, sId, emailId, semester, date)
            Local_workout_data.append(workout_obj)
            
    workout_data = Local_workout_data
    return(workout_data)


# if __name__  ==  "__main__":
#     csvData = processFile("./Uploads/kpData3.csv")
#     for cvd in csvData:
#         print(f"\n==========\n\nData of Row{i}:-\n----------\na>. | Name of candidate: {cvd.name}\nb>. | Total number of calories burned during workout: {cvd.calories}\nc>. | Average Pulse-rate during workout: {cvd.pulse}\nd>. | Maximum pulse-rate achieved during workout: {cvd.maxpulse}\ne>. | Workout Duration: {cvd.duration}\nf>. | Course of student is: {cvd.course}\ng>. | student id is: {cvd.sId}")
