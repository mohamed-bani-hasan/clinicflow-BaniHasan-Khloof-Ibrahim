from clinic_manager import ClinicManager
from appointment_manager import AppointmentManager
from visualizer import Visualizer


def main():

    CLINIC_FILE = "clinic.json"
    APPTS_FILE = "appointments.csv"

    cm = ClinicManager()
    am = AppointmentManager()
    viz = Visualizer()

    
    print("[1/4] Loading data...")

    clinic = cm.load_clinic(CLINIC_FILE)
    appointments = am.load_appointments(APPTS_FILE)

    print(f"      Clinic name         : {clinic['name']}")
    print(f"      Departments         : {len(clinic['departments'])}")
    print(f"      Appointments loaded : {len(appointments)}\n")


    print("[2/4] Clinic departments and doctors:")

    cm.display_departments(clinic)

    
    print("\n[3/4] Booking a test appointment...")

    try:

        appointments = am.book(
            appointments,
            patient_name="Mohamed Bani Hasan",
            patient_id="202111409",
            doctor_id="DR01",
            dept_id="D01",
            date="2026-05-17",
            time_slot="10:00"
        )

        am.save_appointments(appointments, APPTS_FILE)

    except ValueError as e:

        print(f"      Booking failed: {e}")

    
    print("\n[4/4] Displaying charts...")

    viz.dept_chart(appointments)
    viz.status_pie(appointments)

    print("\nDone!")


if __name__ == "__main__":
    main()