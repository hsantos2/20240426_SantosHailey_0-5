vehiclesList = open("data/vehicles.txt","r")
AllowedVehiclesList= vehiclesList.read()

# Menu and User input

print("********************************\nAutoCountry Vehicle Finder v0.1\n********************************")

response = input("Please Enter the following number below from the following menu:\n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. Exit\n")

# Print All Vehicles for loop
if (response == "1"):
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:\n"+ AllowedVehiclesList)

#Search
if (response == "2"):
  response = input("Please enter the full vehicle name.\n")
  if response in AllowedVehiclesList:
    print (response + " is an authorized vehicle.")
  else:
    print (response + " is not an authorized vehicle, if you received this in error please check the spelling and try again.")

# Append 
if (response == "3"):
  vehiclesList = open("data/vehicles.txt","a")
  response = input("Please enter the full vehicle name you would like to add:\n")
  vehiclesList.write("\n" + response)
  print("You have added " + response + " as an authorized vehicle.")
  
 

# Exit if statement
if (response == "4"):
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  vehiclesList.close()

exit()