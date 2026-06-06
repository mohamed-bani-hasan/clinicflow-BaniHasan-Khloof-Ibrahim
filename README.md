# ClinicFlow - Smart Clinic Appointment Management System

## Senior Project Title

**Smart Clinic Appointment Management System (ClinicFlow)**

This project implements the scheduling and analytics engine for a smart clinic management system. It manages clinic departments, doctors, patient appointments, and appointment statistics using Python, JSON, CSV, and Matplotlib.

---

## Team Members

| Student Name                      | Student ID |
| --------------------------------- | ---------- |
| Mohammed Samih Ibrahim Bani Hasan | 202111409  |
| Qais Naser Ali Khloof             | 202111008  |
| Mustafa Sameh Mustafa Ibrahim     | 202110957  |

---

## Project Files

```text
clinicflow/
├── clinic_manager.py
├── appointment_manager.py
├── visualizer.py
├── main.py
├── create_sample_data.py
├── clinic.json
├── appointments.csv
├── requirements.txt
├── report.md
└── screenshots/
```

---

## Requirements

Install the required package:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install matplotlib
```

---

## How to Run

### Step 1: Generate Sample Data

```bash
python create_sample_data.py
```

This creates:

* clinic.json
* appointments.csv

### Step 2: Run the Application

```bash
python main.py
```

The application will:

1. Load clinic data.
2. Load appointment records.
3. Display departments and doctors.
4. Book a test appointment.
5. Save updated appointments.
6. Display appointment statistics charts.

---

## Technologies Used

* Python 3
* JSON
* CSV
* Matplotlib

---

## Expected Output

* Department and doctor information displayed in the terminal.
* New appointment successfully booked.
* Appointment data saved to CSV.
* Bar chart showing appointments per department.
* Pie chart showing appointment status distribution.
