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

    def book(
        self,
        appointments: list,
        patient_name: str,
        patient_id: str,
        doctor_id: str,
        dept_id: str,
        date: str,
        time_slot: str
    ) -> list:

        # Check doctor availability
        for a in appointments:

            if (
                a["doctor_id"] == doctor_id
                and a["date"] == date
                and a["time_slot"] == time_slot
            ):

                raise ValueError(
                    f"Time slot {time_slot} is already booked for "
                    f"{doctor_id} on {date}"
                )

        # Check patient conflict
        for a in appointments:

            if (
                a["patient_id"] == patient_id
                and a["date"] == date
                and a["time_slot"] == time_slot
            ):

                raise ValueError(
                    "Patient already has an appointment at this time"
                )

        # Generate appointment ID
        new_id = f"APT{len(appointments) + 1:03d}"

        # Create appointment
        new_appointment = {
            "appt_id": new_id,
            "patient_name": patient_name,
            "patient_id": patient_id,
            "doctor_id": doctor_id,
            "dept_id": dept_id,
            "date": date,
            "time_slot": time_slot,
            "status": "Pending"
        }

        appointments.append(new_appointment)

        print(
            f"Appointment booked: {new_id} — "
            f"{patient_name} with {doctor_id} "
            f"on {date} at {time_slot}"
        )

        return appointments

    def cancel(self, appointments: list, appt_id: str) -> list:

        found = False
        updated = []

        for a in appointments:

            if a["appt_id"] == appt_id:

                a["status"] = "Cancelled"
                found = True

            updated.append(a)

        if not found:
            raise ValueError("Appointment not found")

        print(f"Appointment cancelled: {appt_id}")

        return updated

    def get_by_doctor(self, appointments: list, doctor_id: str) -> list:

        return [
            a for a in appointments
            if a["doctor_id"] == doctor_id
        ]