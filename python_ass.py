class Flight:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority     

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def sort_by_p_id(self):
        self.flights.sort(key=lambda flight: flight.p_id)

    def sort_by_start_time(self):
        self.flights.sort(key=lambda flight: flight.start_time)

    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        self.flights.sort(key=lambda flight: priority_order[flight.priority])

    def print_table(self):
        for flight in self.flights:
            print(f"P_ID: {flight.p_id}, Process: {flight.process}, Start Time: {flight.start_time}, Priority: {flight.priority}")

if __name__ == "__main__":
    flight_table = FlightTable()
    
    flight_table.add_flight(Flight("P1", "VSCode", 100, "MID"))
    flight_table.add_flight(Flight("P23", "Eclipse", 234, "MID"))
    flight_table.add_flight(Flight("P93", "Chrome", 189, "High"))
    flight_table.add_flight(Flight("P42", "JDK", 9, "High"))
    flight_table.add_flight(Flight("P9", "CMD", 7, "High"))
    flight_table.add_flight(Flight("P87", "NotePad", 23, "Low"))

    while True:
        print("\nE22CSEU1422_PARUCHURI CHAITANYA KRISHNA")
        print("\nChoose sorting parameter:")
        print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            flight_table.sort_by_p_id()
        elif choice == 2:
            flight_table.sort_by_start_time()
        elif choice == 3:
            flight_table.sort_by_priority()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")

        flight_table.print_table()