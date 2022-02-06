def duty_free(price, discount, holiday_cost):
    sale = price * (discount / 100)
    result = int(holiday_cost // sale)
    return result


#(duty_free(12, 50, 1000), 166)
#(duty_free(17, 10, 500), 294)

print(duty_free(17, 10, 500))