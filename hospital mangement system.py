from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, person_id, name, age):
        self.person_id = person_id
        self.name = name
        self.age = age

    @abstractmethod
    def display_info(self):
        pass


# =========================
# Patient Class
# =========================
class Patient(Person):

    def __init__(self, person_id, name, age, disease):
        super().__init__(person_id, name, age)
        self.disease = disease
        self.__appointment_history = []  # Encapsulation

    def add_appointment(self, appointment):
        self.__appointment_history.append(appointment)

    def view_appointments(self):
        if not self.__appointment_history:
            print("No appointments found.")
        else:
            for appointment in self.__appointment_history:
                print(
                    f"Appointment ID: {appointment.appointment_id}, "
                    f"Doctor: {appointment.doctor_name}, "
                    f"Status: {appointment.status}"
                )

    def display_info(self):
        print(
            f"Patient ID: {self.person_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Disease: {self.disease}"
        )


# =========================
# Doctor Class
# =========================
class Doctor(Person):

    def __init__(self, person_id, name, age, specialization):
        super().__init__(person_id, name, age)
        self.specialization = specialization

    def accept_appointment(self, appointment):
        if appointment.status == "Pending":
            appointment.status = "Accepted"
            print("Appointment Accepted")

    def complete_appointment(self, appointment):
        if appointment.status == "Accepted":
            appointment.status = "Completed"
            print("Appointment Completed")

    def display_info(self):
        print(
            f"Doctor ID: {self.person_id}, "
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Specialization: {self.specialization}"
        )


# =========================
# Appointment Class
# =========================
class Appointment:

    def __init__(self, appointment_id, patient_name,
                 doctor_name, date):

        self.appointment_id = appointment_id
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date
        self.status = "Pending"

    def display_info(self):
        print(
            f"Appointment ID: {self.appointment_id}, "
            f"Patient: {self.patient_name}, "
            f"Doctor: {self.doctor_name}, "
            f"Date: {self.date}, "
            f"Status: {self.status}"
        )


# =========================
# Hospital Class
# =========================
class Hospital:

    def __init__(self):
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def book_appointment(self, patient, doctor, appointment):

        self.appointments.append(appointment)
        patient.add_appointment(appointment)

        print("Appointment Booked Successfully")

    def display_doctors(self):
        for doctor in self.doctors:
            doctor.display_info()

    def display_patients(self):
        for patient in self.patients:
            patient.display_info()

    def display_appointments(self):
        for appointment in self.appointments:
            appointment.display_info()


# =========================
# Main Program
# =========================
hospital = Hospital()

doctor1 = Doctor(1, "Dr. Smith", 45, "Cardiologist")
patient1 = Patient(101, "John", 25, "Fever")

hospital.add_doctor(doctor1)
hospital.add_patient(patient1)

appointment1 = Appointment(
    1001,
    patient1.name,
    doctor1.name,
    "25-06-2026"
)

hospital.book_appointment(
    patient1,
    doctor1,
    appointment1
)

doctor1.accept_appointment(appointment1)

doctor1.complete_appointment(appointment1)

print("\nDoctors:")
hospital.display_doctors()

print("\nPatients:")
hospital.display_patients()

print("\nAppointments:")
hospital.display_appointments()