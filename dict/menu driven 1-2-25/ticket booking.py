movies = {}

while True:
    print("\nMovie Ticket Reservation System")
    print("1. Add Movie to Schedule")
    print("2. Book Tickets")
    print("3. Cancel Booking")
    print("4. View Movies")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter movie name: ")
        showtime = input("Enter movie showtime (HH:MM): ")
        seats = int(input("Enter available seats: "))
        movies[name] = {"showtime": showtime, "seats": seats}
        print(f"Movie '{name}' added to the schedule.")

    elif choice == "2":
        movie_name = input("Enter the movie name to book tickets: ")
        if movie_name in movies:
            num_tickets = int(input("Enter number of tickets to book: "))
            if num_tickets <= movies[movie_name]["seats"]:
                movies[movie_name]["seats"] -= num_tickets
                print(f"{num_tickets} tickets booked for {movie_name} at {movies[movie_name]['showtime']}.")
            else:
                print(f"Not enough seats available for {movie_name}.")
        else:
            print("Movie not found in the schedule.")

    elif choice == "3":
        movie_name = input("Enter the movie name to cancel booking: ")
        if movie_name in movies:
            num_tickets = int(input("Enter number of tickets to cancel: "))
            movies[movie_name]["seats"] += num_tickets
            print(f"{num_tickets} tickets cancelled for {movie_name} at {movies[movie_name]['showtime']}.")
        else:
            print("Movie not found in the schedule.")

    elif choice == "4":
        if not movies:
            print("No movies available.")
        else:
            print("\nMovies Schedule:")
            for movie_name, details in movies.items():
                print(f"Movie: {movie_name}, Showtime: {details['showtime']}, Available Seats: {details['seats']}")

    elif choice == "5":
        print("Exiting the movie ticket reservation system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
