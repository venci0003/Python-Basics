square_meters_to_be_landscaped = float(input())

square_meter_price = square_meters_to_be_landscaped * 7.61

discount_result = square_meter_price * 0.18

print(f'The final price is: {square_meter_price - discount_result} lv.\nThe discount is: {discount_result} lv.')