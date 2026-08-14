# 3. Write a program to accept distance in km and convert it into meters and
# centimeters both.


d_km=float(int(input("enter the distance:")))


meter=d_km*1000
print(f"meter={meter}")

centimeter=d_km*100000
print(f"centimeter={centimeter}")


print(f"hence the distance in km is {d_km} and further converted in {meter} meter and {centimeter }centimeter")
