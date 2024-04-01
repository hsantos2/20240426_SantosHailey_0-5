AllowedVehiclesList = ["Ford F-150","Chevrolet Silverado","Tesla CyberTruck","Toyota Tundra","Nissan Titan"]

# Menu and User input

print("********************************\nAutoCountry Vehicle Finder v0.1\n********************************")

response = input("Please Enter the following number below from the following menu:\n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. Exit\n")

# Print All Vehicles for loop
if (response == "1"):
  for AllowedVehicles in AllowedVehiclesList:
    print(AllowedVehicles)

#Search
if (response == "2"):
  response = input("Please enter the full vehicle name.\n")
  if response in AllowedVehiclesList:
    print (response + " is an authorized vehicle.")
  else:
    print (response + " is not an authorized vehicle, if you received this in error please check the spelling and try again.")


# Exit if statement
if (response == "3"):
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

exit()