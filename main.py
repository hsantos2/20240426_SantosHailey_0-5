#vehicle.txt Open File

vehiclesList = open("data/vehicles.txt","r")
AllowedVehiclesList= vehiclesList.read()

#onLoad
onLoad = input("Please enter START to start the program.\n")
if onLoad == "START":
  # Menu and User input

  print("********************************\nAutoCountry Vehicle Finder v0.1\n********************************")

  response = input("Please Enter the following number below from the following menu:\n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit\n")

  # Print All Vehicles
  if (response == "1"):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n"+ AllowedVehiclesList)

  #Search
  elif (response == "2"):
    response = input("Please enter the full vehicle name.\n")
    if response in AllowedVehiclesList:
      print (response + " is an authorized vehicle.")
    else:
      print (response + " is not an authorized vehicle, if you received this in error please check the spelling and try again.")

  # Append 
  elif (response == "3"):
    vehiclesList = open("data/vehicles.txt","a")
    response = input("Please enter the full vehicle name you would like to add:\n")
    vehiclesList.write("\n" + response)
    print("You have added " + response + " as an authorized vehicle.")

  #Delete 
  elif (response == "4"):
    removeVehicle = input("Please enter the full vehicle name you would like to REMOVE:\n")
    with open("data/vehicles.txt", "r") as file:
      lines = file.readlines()
      lineStripped =[line.rstrip("\n") for line in lines]
      if removeVehicle in lineStripped:
        confirmation = input("Are you sure you want to remove " + removeVehicle + " from the Authorized Vehicle list?\n")
        if (confirmation == "yes"):
          lineStripped.remove(removeVehicle)
          with open("data/vehicles.txt", "w") as file:
             file.writelines('\n'.join(lineStripped))
          print("You have removed " + removeVehicle + " as an authorized vehicle.")

  # Exit if statement
  elif (response == "5"):
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    vehiclesList.close()

  exit()
  