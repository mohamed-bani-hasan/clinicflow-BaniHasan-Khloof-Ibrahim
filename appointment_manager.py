import csv


class AppointmentManager:

    def load_appointments(self, filepath: str) -> list:

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                return list(reader)

        except FileNotFoundError:
            return []
