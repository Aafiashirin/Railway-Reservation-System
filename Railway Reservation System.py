from collections import deque


# Passenger class
class Passenger:
    def __init__(self, passenger_id, name):
        self.passenger_id = passenger_id
        self.name = name

    def __str__(self):
        return f"{self.passenger_id} - {self.name}"


# Train class
class Train:
    def __init__(self, train_no, train_name, source,
                 destination, departure_time, seats):

        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.available_seats = seats

        # Queue for waiting list
        self.waiting_list = deque()

        # Passengers who got tickets
        self.booked_passengers = []


    # Book ticket
    def book_ticket(self, passenger):

        if self.available_seats > 0:

            self.available_seats -= 1
            self.booked_passengers.append(passenger)

            print(f"\nTicket booked successfully!")
            print(f"Passenger: {passenger.name}")
            print(f"Train: {self.train_name}")

        else:

            self.waiting_list.append(passenger)

            print("\nNo seats available.")
            print(f"{passenger.name} added to waiting list.")


    # Cancel ticket
    def cancel_ticket(self, passenger):

        if passenger in self.booked_passengers:

            self.booked_passengers.remove(passenger)
            self.available_seats += 1

            print(f"\nTicket cancelled for {passenger.name}")

            # Give seat to first waiting passenger
            if self.waiting_list:

                next_passenger = self.waiting_list.popleft()

                self.available_seats -= 1
                self.booked_passengers.append(next_passenger)

                print(
                    f"{next_passenger.name} "
                    f"got the cancelled seat."
                )

        else:
            print("\nPassenger does not have a ticket.")


    # Display train
    def display(self):

        print(
            f"{self.train_no} | "
            f"{self.train_name} | "
            f"{self.source} -> {self.destination} | "
            f"Departure: {self.departure_time} | "
            f"Seats: {self.available_seats}"
        )


# Search trains
def search_trains(trains, source, destination):

    print("\n--- Search Results ---")

    found = False

    for train in trains:

        if (train.source.lower() == source.lower()
                and train.destination.lower() == destination.lower()):

            train.display()
            found = True

    if not found:
        print("No trains found.")


# Sort trains
def sort_trains(trains):

    sorted_trains = sorted(
        trains,
        key=lambda train: train.departure_time
    )

    print("\n--- Trains Sorted by Departure Time ---")

    for train in sorted_trains:
        train.display()


# Main program
def main():

    # Create trains
    trains = [

        Train(
            101,
            "Bangalore Express",
            "Bangalore",
            "Chennai",
            "08:00",
            2
        ),

        Train(
            102,
            "Superfast Express",
            "Bangalore",
            "Chennai",
            "06:30",
            1
        ),

        Train(
            103,
            "Intercity Express",
            "Bangalore",
            "Hyderabad",
            "09:30",
            3
        )
    ]


    # Create passengers
    passengers = [

        Passenger(1, "Mehek"),
        Passenger(2, "Saniya"),
        Passenger(3, "Samreen")
    ]


    while True:

        print("\n==============================")
        print("  RAILWAY RESERVATION SYSTEM")
        print("==============================")

        print("1. Display Trains")
        print("2. Search Train")
        print("3. Sort Trains")
        print("4. Book Ticket")
        print("5. Cancel Ticket")
        print("6. Display Waiting List")
        print("7. Exit")

        choice = input("\nEnter your choice: ")


        # Display trains
        if choice == "1":

            print("\n--- Available Trains ---")

            for train in trains:
                train.display()


        # Search
        elif choice == "2":

            source = input("Enter source: ")
            destination = input("Enter destination: ")

            search_trains(
                trains,
                source,
                destination
            )


        # Sort
        elif choice == "3":

            sort_trains(trains)


        # Book
        elif choice == "4":

            print("\nPassengers:")

            for passenger in passengers:
                print(passenger)

            passenger_id = int(
                input("Enter passenger ID: ")
            )

            train_no = int(
                input("Enter train number: ")
            )

            selected_passenger = None
            selected_train = None


            for passenger in passengers:

                if passenger.passenger_id == passenger_id:
                    selected_passenger = passenger


            for train in trains:

                if train.train_no == train_no:
                    selected_train = train


            if selected_passenger and selected_train:

                selected_train.book_ticket(
                    selected_passenger
                )

            else:

                print("Invalid passenger or train.")


        # Cancel
        elif choice == "5":

            passenger_id = int(
                input("Enter passenger ID: ")
            )

            train_no = int(
                input("Enter train number: ")
            )

            selected_passenger = None
            selected_train = None


            for passenger in passengers:

                if passenger.passenger_id == passenger_id:
                    selected_passenger = passenger


            for train in trains:

                if train.train_no == train_no:
                    selected_train = train


            if selected_passenger and selected_train:

                selected_train.cancel_ticket(
                    selected_passenger
                )

            else:

                print("Invalid passenger or train.")


        # Waiting list
        elif choice == "6":

            train_no = int(
                input("Enter train number: ")
            )

            selected_train = None

            for train in trains:

                if train.train_no == train_no:
                    selected_train = train


            if selected_train:

                print("\n--- Waiting List ---")

                if selected_train.waiting_list:

                    for passenger in selected_train.waiting_list:
                        print(passenger)

                else:
                    print("Waiting list is empty.")

            else:
                print("Train not found.")


        # Exit
        elif choice == "7":

            print("\nThank you for using Railway Reservation System!")
            break


        else:

            print("Invalid choice. Try again.")


# Start program
if __name__ == "__main__":
    main()