def decorator(a):

    def wrapper(*args, **kwargs):

        animal = args[0]

        if animal.health == "H":
            print("Health Check: Passed")
            return a(*args, **kwargs)
            

        else:
            print("Health Check: Failed")
            print(animal.name, "cannot perform this activity")
            exit()

    return wrapper