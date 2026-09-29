# Vacuum Cleaner Agent - 2 Rooms

room_A = input("Enter status of Room A (Clean/Dirty): ").capitalize()
room_B = input("Enter status of Room B (Clean/Dirty): ").capitalize()

print("\nInitial State:")
print("Room A:", room_A)
print("Room B:", room_B)


print("\nVacuum is in Room A")

if room_A == "Dirty":
    print("Room A is Dirty -> Cleaning Room A")
    room_A = "Clean"
else:
    print("Room A is already Clean")


print("\nVacuum moves to Room B")

if room_B == "Dirty":
    print("Room B is Dirty -> Cleaning Room B")
    room_B = "Clean"
else:
    print("Room B is already Clean")


print("\nFinal State:")
print("Room A:", room_A)
print("Room B:", room_B)
