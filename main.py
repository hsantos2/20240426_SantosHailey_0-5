AllowedVehiclesList = ["Ford F-150","Chevrolet Silverado","Tesla CyberTruck","Toyota Tundra","Nissan Titan"]

# Menu and User input
print("********************************\nAutoCountry Vehicle Finder v0.1\n********************************")
response = input("Please Enter the following number below from the following menu:\n1. PRINT all Authorized Vehicles\n2. Exit\n")

# Print All Vehicles for loop
if (response == "1"):
  for AllowedVehicles in AllowedVehiclesList:
    print(AllowedVehicles)

# Exit if statement
if (response == "2"):
  print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")

exit()