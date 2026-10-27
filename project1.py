
"""
Hospital Patient Record System
"""

import json


class Patient:
    def __init__(self, name, age, temperature):
        self.name = name
        self.age = age
        self.temperature = temperature

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if 0 <= new_age <= 120:
            self.__age = new_age
        else:
            raise ValueError("Invalid age! Age must be between 0 and 120.")

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, new_temperature):
        if 30.0 <= new_temperature <= 45.0:
            self.__temperature = new_temperature
        else:
            raise ValueError(
                "Invalid temperature! Enter a value between 30 and 45."
            )

    def display_record(self):
        print("\n--- Patient Record ---")
        print("Patient's name:", self.name)
        print("Age:", self.age)
        print("Body temperature:", self.temperature)


name = input("Enter patient name: ").strip()

try:
    if not name:
        raise ValueError("Patient name cannot be empty.")

    age = int(input("Enter patient age: "))
    temperature = float(input("Enter body temperature: "))

    # Create patient object and validate details
    patient1 = Patient(name, age, temperature)

    # Display patient details
    patient1.display_record()

    # Load previous patient records
    try:
        with open("patients.json", "r") as file:
            patients = json.load(file)

        # Convert an old single dictionary into a list
        if isinstance(patients, dict):
            patients = [patients]

        # Check that the JSON contains a list
        if not isinstance(patients, list):
            raise ValueError("Patient file must contain a list of records.")

    except FileNotFoundError:
        patients = []

    except json.JSONDecodeError:
        raise ValueError(
            "patients.json contains invalid JSON. Please fix the file first."
        )

    # Create dictionary for the new patient
    patient = {
        "name": patient1.name,
        "age": patient1.age,
        "temperature": patient1.temperature
    }

    # Add new patient without removing old records
    patients.append(patient)

    # Save all patient records
    with open("patients.json", "w") as file:
        json.dump(patients, file, indent=4)

    print("\nPatient details saved successfully!")

except ValueError as error:
    print("Invalid input:", error)

except OSError as error:
    print("File error:", error)
