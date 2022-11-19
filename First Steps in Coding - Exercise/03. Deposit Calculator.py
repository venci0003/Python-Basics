deposit_sum = float(input())

term_for_deposit = int(input())

percentage = float(input())

increase = deposit_sum * percentage / 100.0

increase_in_a_month = increase / 12

result = deposit_sum + term_for_deposit * increase_in_a_month

print(result)