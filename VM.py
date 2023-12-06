import csv

transportFile = open("www\PRA-III\VM.csv", "r")
reader = csv.DictReader(transportFile, delimiter=";")
transportList = list(reader)

maintenanceTime = 0
maintenanceCost = 0

for transport in transportList:
    maintenanceTime += int(transport['Onderhoud_mins'])

numTransport = len(transportList)
averageMaintenanceTime = round(maintenanceTime / numTransport)

print(f"Gemiddelde onderhoud tijd: \n{averageMaintenanceTime}")

transportTypeChoice = input("\nVoertuigtype van vervoer: ")

print(f"\nGemiddelde kostte: ")

for transport in transportList:
    if transportTypeChoice == transport['Voertuigtype']:
        maintenanceCost += float(transport['Onderhoud_Kosten'])