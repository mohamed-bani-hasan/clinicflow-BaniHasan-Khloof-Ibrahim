import json
import csv


def create_clinic(filepath="clinic.json"):
    data = {
        "clinic": {
            "name": "AAUP Health Center",
            "departments": [
                {
                    "dept_id": "D01",
                    "name": "General Medicine",
                    "doctors": [
                        {
                            "doctor_id": "DR01",
                            "name": "Dr. Samira Haddad",
                            "slots_per_day": 20
                        },
                        {
                            "doctor_id": "DR02",
                            "name": "Dr. Omar Barakat",
                            "slots_per_day": 18
                        }
                    ]
                },
                {
                    "dept_id": "D02",
                    "name": "Dentistry",
                    "doctors": [
                        {
                            "doctor_id": "DR03",
                            "name": "Dr. Lina Nassar",
                            "slots_per_day": 12
                        }
                    ]
                },
                {
                    "dept_id": "D03",
                    "name": "Ophthalmology",
                    "doctors": [
                        {
                            "doctor_id": "DR04",
                            "name": "Dr. Faris Qasim",
                            "slots_per_day": 15
                        }
                    ]
                }
            ]
        }
    }

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Clinic saved: {filepath}")


def create_appointments(filepath="appointments.csv"):
    rows = [
        [
            "appt_id",
            "patient_name",
            "patient_id",
            "doctor_id",
            "dept_id",
            "date",
            "time_slot",
            "status"
        ],

        ["APT001", "Ahmad Saleh", "202200101", "DR01", "D01", "2026-05-15", "09:00", "Completed"],
        ["APT002", "Sara Younis", "202200102", "DR03", "D02", "2026-05-15", "10:00", "Completed"],
        ["APT003", "Nour Khalil", "202200103", "DR01", "D01", "2026-05-15", "09:30", "Cancelled"],
        ["APT004", "Yousef Awad", "202200104", "DR04", "D03", "2026-05-15", "11:00", "Completed"],
        ["APT005", "Rania Mahmoud", "202200105", "DR02", "D01", "2026-05-15", "10:30", "Pending"],
        ["APT006", "Khaled Nasser", "202200106", "DR03", "D02", "2026-05-15", "11:30", "Completed"],
        ["APT007", "Dina Abu Zaid", "202200107", "DR01", "D01", "2026-05-16", "09:00", "Pending"],
        ["APT008", "Lara Hijazi", "202200108", "DR04", "D03", "2026-05-16", "10:00", "Completed"],
        ["APT009", "Faris Barakat", "202200109", "DR02", "D01", "2026-05-16", "09:30", "Cancelled"],
        ["APT010", "Hana Odeh", "202200110", "DR03", "D02", "2026-05-16", "11:00", "Pending"]
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"Appointments saved: {filepath}")


if __name__ == "__main__":
    create_clinic()
    create_appointments()