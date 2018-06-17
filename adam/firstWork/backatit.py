aliens = 2
password = "aliens"
print("Quickly! We are being invaded!")
print("We need the password for the global defence protocalls")
print("-------------")
print("EARTH DEFENCE")
print("-------------")

guess = input("Enter password: ").lower()

while guess != password:
    print()
    print("INCORRECT")
    print()
    aliens = aliens ** 2
    print("There are", aliens, "aliens on earth. Quick, try again for Earth!")
    if aliens > 76000000000:
        break
    print()
    print("Password hint: the things attacking us: ")
    print()
    guess = input("Enter password: ").lower()
if aliens > 76000000000:
    print("Noooo!The aliens have out numbered us. Goodbye.")
else:
    print("Hooooray!We won")
