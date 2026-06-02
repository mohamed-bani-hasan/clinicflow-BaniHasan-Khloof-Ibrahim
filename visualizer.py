import matplotlib.pyplot as plt

class Visualizer:

    def dept_chart(self, appointments):

        counts = {}

        for a in appointments:
            if a["dept_id"] in counts:
                counts[a["dept_id"]] += 1
            else:
                counts[a["dept_id"]] = 1

        plt.figure(figsize=(8, 5))
        plt.bar(counts.keys(), counts.values())

        plt.title("Appointments by Department")
        plt.xlabel("Department ID")
        plt.ylabel("Number of Appointments")

        plt.show()

    def status_pie(self, appointments):

        counts = {}

        for a in appointments:
            if a["status"] in counts:
                counts[a["status"]] += 1
            else:
                counts[a["status"]] = 1

        plt.figure(figsize=(7, 7))

        plt.pie(
            counts.values(),
            labels=counts.keys(),
            autopct="%1.1f%%"
        )

        plt.title("Appointment Status Distribution")

        plt.show()
