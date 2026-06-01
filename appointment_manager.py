import csv


class AppointmentManager:

    def load_appointments(self, filepath: str) -> list:

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return list(reader)

        except FileNotFoundError:
            return []

    def save_appointments(self, appointments: list, filepath: str) -> None:

        fieldnames = [
            "appt_id",
            "patient_name",
            "patient_id",
            "doctor_id",
            "dept_id",
            "date",
            "time_slot",
            "status"
        ]

        with open(filepath, "w", newline="", encoding="utf-8") as f:

            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(appointments)

        print(f"Appointments saved: {filepath}")
