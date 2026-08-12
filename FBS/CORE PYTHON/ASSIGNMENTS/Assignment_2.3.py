# Convert distant given in feet and inches into meter and centimeter.

Feet = float(input("ENTER FEET: "))
Inch = float(input("ENTER INCHES: "))

Total_Meter = (Feet * 0.3048) + (Inch * 0.0254)

print("TOTAL METER =", Total_Meter)

Total_Centimeter = Total_Meter * 100

print("TOTAL CENTIMETER =", Total_Centimeter)