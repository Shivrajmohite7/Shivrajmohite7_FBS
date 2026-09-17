
class Toll:

    def toll(self,person):
        pass


class TWO_W(Toll):

    def toll(self, person):
        amount = 20
        if person > 2:
            amount = amount + (person - 2) * 10
        return amount

class THREE_W(Toll):

    def toll(self, person):
        amount = 30
        if person > 3:
            amount = amount + (person - 3) * 20
        return amount


class FOUR_W(Toll):

    def toll(self, person):
        amount = 40
        if person > 4:
            amount = amount + (person - 4) * 40
        return amount


class HEAVY_W(Toll):

    def toll(self, person):
        amount = 60
        if person > 6:
            amount = amount + (person - 6) * 100
        return amount



print("1. Two_W")
print("2. Three_W")
print("3. Four_W")
print("4. Heavy_V")

choice = int(input("Enter choice : "))
person = int(input("Enter number of persons : "))

if choice == 1:
    vehicle = TWO_W()

elif choice == 2:
    vehicle = THREE_W()

elif choice == 3:
    vehicle = FOUR_W()

elif choice == 4:
    vehicle = HEAVY_W()

else:
    print("CHECK AGAIN")
    exit()

print("OVERALL TOLL :", vehicle.toll(person))
    







input("enter")