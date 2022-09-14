# Electricity Unit Price
electricity_slice_one_unit_price = 5
electricity_slice_two_unit_price = 10
electricity_max_unit_price = 15

electricity_slice_one_upper_bound = 100
electricity_slice_two_upper_bound = 1000

# Water Unit Price
water_slice_one_unit_price = 50
water_slice_two_unit_price = 60
water_max_unit_price = 70

water_slice_one_upper_bound = 500
water_slice_two_upper_bound = 2500

# Implementation
mode = input("Enter the type of bill you want to calculate: \n 1)Electricity \n 2)Water \n Your Choice: ")
meter_reading = input("Enter your meter reading - KwH for Electricity & m^3 for water: ")

if not meter_reading.isnumeric():
    print("Please enter a numerical meter reading")
    exit(0)

if int(mode) != 1 and int(mode) != 2:
    print(f"Usage: mode should be a number within the list")
    exit(0)

mode = int(mode)
meter_reading = int(meter_reading)
bill_amount = 0

if int(mode) == 1:
    print(f"Calculating Electricity bill")

    if int(meter_reading) <= electricity_slice_one_upper_bound:
        bill_amount = meter_reading * electricity_slice_one_unit_price
    elif electricity_slice_two_upper_bound > int(meter_reading) > electricity_slice_one_upper_bound:
        bill_amount = meter_reading * electricity_slice_two_unit_price
    elif int(meter_reading) > electricity_slice_two_upper_bound:
        bill_amount = meter_reading * electricity_max_unit_price
    else:
        print("Not a proper reading")

    print(f"Your bill is {bill_amount}")

elif mode == 2:
    print(f"Calculating Water bill")

    if int(meter_reading) <= water_slice_one_upper_bound:
        bill_amount = meter_reading * water_slice_one_unit_price
    elif water_slice_two_upper_bound > int(meter_reading) > water_slice_one_upper_bound:
        bill_amount = meter_reading * water_slice_two_unit_price
    elif int(meter_reading) > water_slice_two_upper_bound:
        bill_amount = meter_reading * water_max_unit_price
    else:
        print("Not a proper reading")

    print(f"Your bill is {bill_amount}")

else:
    print(f"Mode {mode} is not supported, please choose a value from the list")
