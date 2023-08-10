#The urgency register.
class Urgency:
    def __init__(self):
        self.patientName = ""
        self.patientLastName = ""
        self.patientAge = ""
        self.patientTime = ""
        self.patientAssurance = ""
        
    def get_PatientName(self):
        self.patientName = input("Enter your first name: ")
        
    def get_PatientLastName(self):
        self.patientLastName = input("Enter your last name: ")
        
    def get_PatientAge(self):
        self.patientAge = input("Enter your age: ")
        
    def get_PatientTime(self):
        self.patientTime = input("Enter your arrival time: ")
        
    def get_PatientAssurance(self):
        self.patientAssurance = input("Enter your insurance provider: ")

#Atributes of the departments.
class Department:
    def __init__(self, name, description, head):
        self.name = name
        self.description = description
        self.head = head
        
    def display_info(self):
        print(f"Department: {self.name}")
        print(f"Description: {self.description}")
        print(f"Head: {self.head.name} ({self.head.role})\n")

#Atributes of the Hospital.
class Hospital:
    def __init__(self, name, postal_Code, address, telephone, hospital_Type, max_number_Patients,
                 rating, area_Size, rooms_Quantity, doctors_Quantity, nurses_Quantity,
                 drugs_Quantity, worktools_Quantity, devices_Quantity, areas_Quantity):
        self.name = name
        self.postal_Code = postal_Code
        self.address = address
        self.telephone = telephone
        self.hospital_Type = hospital_Type
        self.max_number_Patients = max_number_Patients
        self.rating = rating
        self.area_Size = area_Size
        self.rooms_Quantity = rooms_Quantity
        self.doctors_Quantity = doctors_Quantity
        self.nurses_Quantity = nurses_Quantity
        self.drugs_Quantity = drugs_Quantity
        self.worktools_Quantity = worktools_Quantity
        self.devices_Quantity = devices_Quantity
        self.areas_Quantity = areas_Quantity
        self.medical_departments = []
        self.surgical_departments = []
        self.diagnostic_departments = []

#Function to show all the information about the hospital, departments, staff, etc.   
    def display_info(self):
        print(f"Hospital Name: {self.name}")
        print(f"Postal Code: {self.postal_Code}")
        print(f"Address: {self.address}")
        print(f"Telephone: {self.telephone}")
        print(f"Hospital Type: {self.hospital_Type}")
        print(f"Max Number of Patients: {self.max_number_Patients}")
        print(f"Rating: {self.rating}")
        print(f"Area Size: {self.area_Size}")
        print(f"Rooms Quantity: {self.rooms_Quantity}")
        print(f"Doctors Quantity: {self.doctors_Quantity}")
        print(f"Nurses Quantity: {self.nurses_Quantity}")
        print(f"Drugs Quantity: {self.drugs_Quantity}")
        print(f"Worktools Quantity: {self.worktools_Quantity}")
        print(f"Devices Quantity: {self.devices_Quantity}")
        print(f"Areas Quantity: {self.areas_Quantity}")
        print("\nMedical Departments:")
        for department in self.medical_departments:
            department.display_info()
        print("\nSurgical Departments:")
        for department in self.surgical_departments:
            department.display_info()
        print("\nDiagnostic Departments:")
        for department in self.diagnostic_departments:
            department.display_info()

#Class for the staff like doctors and nurses that leads a department.
class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        
    def display_info(self):
        print(f"Name: {self.name}, Role: {self.role}")


#Instances of the Staff.
doctor1 = Staff("Dr. Jacob Escareño", "Doctor")
doctor2 = Staff("Dr. Jose Domínguez", "Doctor")
doctor3 = Staff("Dra. Sarahí Lopéz", "Doctor")
doctor4 = Staff("Dr. Erasmo Díaz", "Doctor")
doctor5 = Staff("Dr. Alberto Campos", "Doctor")
doctor6 = Staff("Dr. Emilio Romo", "Doctor")
nurse1 = Staff("Nurse María José", "Nurse")
nurse2 = Staff("Nurse Juan Carlos", "Nurse")

#Instances of the medical deparment.
medical_department1 = Department("Anesthesiology", "Branch of medicine dedicated\nto pain relief and total patient care before,\n during and after surgery.", doctor1)
medical_department2 = Department("Cardiology", "Branch of medicine that deals\nwith the study, diagnosis and treatment of\n diseases of the heart and circulatory system.", doctor2)
medical_department3 = Department("Intensive Care", "It is a special facility within\nthe hospital area that provides intensive medicine.", nurse1)
medical_department4 = Department("Gastroenterology", "Study of the normal function and\ndiseases of the esophagus, stomach, small intestine,\ncolon and rectum, pancreas, gallbladder, bile ducts, and liver.", doctor3)

#Instances of the surgical department.
surgical_department1 = Department("General Surgery", "It includes the diagnosis and\ntreatment of diseases that are resolved by\nsurgical or potentially surgical procedures,\nboth elective and urgent.", doctor4)
surgical_department2 = Department("Orthopedics and Traumatology", "Traumatology is the branch\nof medicine dedicated to the study of injuries\nto the musculoskeletal system.", doctor6)
surgical_department3 = Department("Dermatology", "It is a specialty of medicine\nthat deals with the knowledge and study of\nhuman skin and the diseases that affect it.", doctor3)
surgical_department4 = Department("Gynecology and Obstetrics", "This combined training makes\nthose who practice it experts in the health\ncare of the female reproductive organs and\nin the management of obstetric complications,\neven through surgical interventions.", doctor5)

#Instances of the diagnostic department.
diagnostic_department1 = Department("Clinical Laboratories", "The clinical laboratory brings\ntogether a multidisciplinary team that analyzes\nhuman biological samples to study,\nprevent disease and expand medical knowledge.", doctor2)
diagnostic_department2 = Department("Radiology", "Branch of medicine that uses\nimaging technology to diagnose and treat disease.", doctor5)
diagnostic_department3 = Department("Pharmacy", "Science that studies everything\nrelated to the preparation, preservation,\npromotion and dispensing of medicines.", nurse2)
diagnostic_department4 = Department("Preventive Medicine", "It focuses on preventing health\nproblems before they occur.", doctor4)

#Instance of the Hospital.
hospital = Hospital("Quarks Medic", "20126", "Monkeys St. 146", "616-348", "Private", 150, 9.3,
                    "26,200m", 200, 65, 120, 1050, 1300, 1250, 3)
hospital.medical_departments.extend([medical_department1, medical_department2, medical_department3, medical_department4])
hospital.surgical_departments.extend([surgical_department1, surgical_department2, surgical_department3, surgical_department4])
hospital.diagnostic_departments.extend([diagnostic_department1, diagnostic_department2, diagnostic_department3, diagnostic_department4])

#Here we show the info of the hospital.
hospital.display_info()

#Instance of the department of Urgency
urgency_department = Urgency()

#Ask if the user wants to use the register to the urgency department
use_urgency = input("Do you want to use the urgency register? (y/n):\n")

if use_urgency.lower() == "y":
    urgency_department.get_PatientName()
    urgency_department.get_PatientLastName()
    urgency_department.get_PatientAge()
    urgency_department.get_PatientTime()
    urgency_department.get_PatientAssurance()
else:
    print("Goodbye, go to know God.")
