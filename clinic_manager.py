import json


class ClinicManager:

    def load_clinic(self, filepath: str) -> dict:
        try:
            with open(filepath, "r") as f:
                data = json.load(f)

            return data["clinic"]

        except FileNotFoundError:
            raise FileNotFoundError(
                f"Clinic file '{filepath}' was not found."
            )

    def get_department(self, clinic: dict, dept_id: str) -> dict:

        for dept in clinic["departments"]:

            if dept["dept_id"].upper() == dept_id.upper():
                return dept

        return None

    def get_doctor(self, clinic: dict, doctor_id: str) -> dict:

        for dept in clinic["departments"]:

            for doctor in dept["doctors"]:

                if doctor["doctor_id"].upper() == doctor_id.upper():
                    return doctor

        return None

    def display_departments(self, clinic: dict) -> None:

        print("Dept ID | Department        | Doctors")
        print("--------|-------------------|--------------------------------------------")

        for dept in clinic["departments"]:

            doctors = ", ".join(
                f"{d['name']} ({d['doctor_id']})"
                for d in dept["doctors"]
            )

            print(
                f"{dept['dept_id']:<8} | "
                f"{dept['name']:<17} | "
                f"{doctors}"
            )