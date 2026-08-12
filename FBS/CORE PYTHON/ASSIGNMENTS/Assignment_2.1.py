# Convert the time entered in hh,min and sec into seconds.

hour = int(input("Enter HOURS: "))
minute = int(input("Enter MINUTES: "))
second = int(input("Enter SECONDS: "))

Total_Sec = hour * 3600 + minute * 60 + second

print("TOTAL SECONDS:", Total_Sec)


