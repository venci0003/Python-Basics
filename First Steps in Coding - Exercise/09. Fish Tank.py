lenght = float(input())

width = float(input())

height = float(input())

percentage = float(input())

volume = lenght * width * height

volumeInLiters = volume / 1000

busy = percentage / 100

liters = volumeInLiters * (1 - busy)

print(liters)
