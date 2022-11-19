nylon = int(input())

paint = int(input())

paintThinner = int(input())

workersHours = int(input())

nylonSum = float(nylon + 2) * 1.50

paintPercentage = float(paint * 0.10)

paintSum = float(paint + paintPercentage) * 14.50

paintThinnerSum = paintThinner * 5.00

everythingSum = nylonSum + paintSum + paintThinnerSum + 0.40

workersHoursSum = (everythingSum * 0.30) * workersHours

result = everythingSum + workersHoursSum

print(result)