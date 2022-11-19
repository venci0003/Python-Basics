count_of_pens = int(input()) * 5.80

count_of_markers= int(input()) * 7.20

count_of_cleaners = int(input()) * 1.20

percentage = float(input())

sum_of_all_products = count_of_markers + count_of_cleaners + count_of_pens

result = sum_of_all_products - (sum_of_all_products * percentage / 100)

print(result)

