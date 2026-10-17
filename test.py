from calc import calc_current,calc_voltage,calc_resistance,calc_power
assert calc_current(10, 2) ==5
print("current test passed")
assert calc_voltage(10, 0.5) ==5
print("voltage test passed")
assert calc_resistance (10, 2)==5
print("resistance test passed")
assert calc_power(10, 2) == 20
print("power test passed")

print("all tests passed")	
