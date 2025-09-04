room_grid = [
    ['E', 'F', 'L', 'R'],
    ['E', 'F', 'L', 'R'],
    ['E', 'F', 'L', 'R'],
    ['E', 'F', 'L', 'R'],
    ['E', 'F', 'L', 'R']
]
def available_rooms():
    print("Number of floors: 5")
    print("Number of Rooms (Per floor): 4 of each category")
    print("Room Categories and Charges:")
    print("1. Royal       8000 per night (AC)")
    print("2. Luxury      7000 per night (AC)")
    print("3. First Class 5000 per night (NON AC)")
    print("4. Economical  3000 per night (NON AC)")
    print("------------------------------------------")
    print("Room Layout: (E = Economical, F = First Class, L = Luxury, R = Royal, 0 = Occupied)\n")

    for i in range(5):
        print(f"Floor {i+1}: [ ", end="")
        for j in range(4):
            print(room_grid[i][j], end=" ")
        print("]")


def mark_room_as_booked(category):
    for i in range(5):
        for j in range(4):
            if room_grid[i][j] == category:
                room_grid[i][j] = '0'
                print(f"Room booked on Floor {i+1}, Room {j+1}")
                return
    print("No available rooms of selected category.")


def checkin():
    num = int(input("Enter the category number to check in:\n1. Royal\n2. Luxury\n3. First Class\n4. Economical\n"))

    name = input("Enter guest name: ")
    phone = int(input("Enter the last 3 digits of your mobile number: "))
    nights = int(input("Enter the number of nights you want to stay: "))

    with open("guestdata.txt", "a") as fout:
        fout.write("Guest: " + name + "\n")
        fout.write(str(phone) + "\n")

        if num == 1:
            cat = 'R'
            fout.write("Room: Royal\n")
            fout.write("Charges: " + str(8000 * nights) + "\n")
        elif num == 2:
            cat = 'L'
            fout.write("Room: Luxury\n")
            fout.write("Charges: " + str(7000 * nights) + "\n")
        elif num == 3:
            cat = 'F'
            fout.write("Room: First Class\n")
            fout.write("Charges: " + str(5000 * nights) + "\n")
        elif num == 4:
            cat = 'E'
            fout.write("Room: Economical\n")
            fout.write("Charges: " + str(3000 * nights) + "\n")
        else:
            print("Invalid input.")
            return

        mark_room_as_booked(cat)
        fout.write("---------------------------\n")


def checkout():
    cnt = int(input("Enter the last 3 digits of the contact number of the guest to checkout: "))

    found = False
    with open("guestdata.txt", "r") as fin, open("checkout.txt", "a") as fout:
        fout.write("Here are the details of the checkout Guests:\n")

        lines = fin.readlines()
        i = 0
        while i < len(lines):
            name = lines[i].strip()
            num = int(lines[i + 1].strip())
            room = lines[i + 2].strip()
            chargeLine = lines[i + 3].strip()

            if cnt == num:
                print(name)
                print("Contact:", num)
                print(room)
                print(chargeLine)
                print("---------------------------")
                print("You have checked out")

                fout.write(name + "\n")
                fout.write("Contact: " + str(num) + "\n")
                fout.write(room + "\n")
                fout.write(chargeLine + "\n")
                fout.write("---------------------------\n")
                fout.write("You have checked out\n")

                found = True
            i += 5  # skip block

    if not found:
        print("Guest not found with this contact number.")


def peak_period():
    print("Number of floors: 5")
    print("Number of Rooms (Per floor): 4 of each category")
    print("Room Categories and Charges because of peak period:")
    print("1. Royal       10000 per night (AC)")
    print("2. Luxury      8000 per night (AC)")
    print("3. First Class 7000 per night (NON AC)")
    print("4. Economical  5000 per night (NON AC)")
    print("------------------------------------------")

    num = int(input("Enter the category number to check in: "))
    nights = int(input("Enter the number of nights you will be staying here: "))

    name = input("Enter guest name: ")
    phone = int(input("Enter the last 3 digits of your mobile number: "))

    with open("guestdata.txt", "a") as fout:
        fout.write("Guest: " + name + "\n")
        fout.write(str(phone) + "\n")

        if num == 1:
            cat = 'R'
            fout.write("Room: Royal\n")
            fout.write("Charges: " + str(10000 * nights) + "\n")
        elif num == 2:
            cat = 'L'
            fout.write("Room: Luxury\n")
            fout.write("Charges: " + str(8000 * nights) + "\n")
        elif num == 3:
            cat = 'F'
            fout.write("Room: First Class\n")
            fout.write("Charges: " + str(7000 * nights) + "\n")
        elif num == 4:
            cat = 'E'
            fout.write("Room: Economical\n")
            fout.write("Charges: " + str(5000 * nights) + "\n")
        else:
            print("Invalid input.")
            return

        mark_room_as_booked(cat)
        fout.write("---------------------------\n")


def couple_pack():
    print("Couple package")
    num = int(input("Enter the category number to check in:\n1. Royal\n2. Luxury\n3. First Class\n4. Economical\n"))
    nights = int(input("Enter the number of nights you will be staying here: "))

    name = input("Enter guest name: ")
    phone = int(input("Enter the last 3 digits of your mobile number: "))

    with open("guestdata.txt", "a") as fout:
        fout.write("Guest: " + name + "\n")
        fout.write(str(phone) + "\n")

        if num == 1:
            cat = 'R'
            fout.write("Room: Royal\n")
            fout.write("Charges: " + str(7000 * nights) + "\n")
        elif num == 2:
            cat = 'L'
            fout.write("Room: Luxury\n")
            fout.write("Charges: " + str(6000 * nights) + "\n")
        elif num == 3:
            cat = 'F'
            fout.write("Room: First Class\n")
            fout.write("Charges: " + str(5000 * nights) + "\n")
        elif num == 4:
            cat = 'E'
            fout.write("Room: Economical\n")
            fout.write("Charges: " + str(4000 * nights) + "\n")
        else:
            print("Invalid input.")
            return

        mark_room_as_booked(cat)
        fout.write("---------------------------\n")


def main():
    print("         Welcome to the Mountain Lodge Murree")
    print("         -------------------------------------")

    while True:
        print("\nMenu:")
        print("1. View Available Rooms")
        print("2. Check In")
        print("3. Checkout")
        print("4. Couple package for checkin")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            available_rooms()
        elif choice == 2:
            checkin()
            # peak_period()   # uncomment if needed
        elif choice == 3:
            checkout()
        elif choice == 4:
            couple_pack()
        elif choice == 5:
            print("Thank you for visiting Mountain Lodge Murree. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

        again = input("Do you want to continue? (yes/no): ")
        if again.lower() != "yes":
            break

    print("Thank you for using our service!")


main()
