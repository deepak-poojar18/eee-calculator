

def get_positive_float(prompt,allow_zero= False):
    while True:
        raw_val = input(prompt).strip()
        try:
            val = float(raw_val)
            if val < 0 or (val ==0 and not allow_zero):
                print("Error: Value must be strictly greater or than 0.")
                continue
            return val
        except ValueError:
            print(f"Error: '{raw_val}' is not a valid number. Try again.")

def calc_voltage(current, resistance):
	return current*resistance

def calc_resistance(voltage, current):
	return voltage/current

def calc_current(voltage,resistance):
	return voltage/resistance

def calc_power(voltage, current):
	return voltage*current



def main():
    #program starts now

    print("EEE CALCULATOR")
    print("==============")

    while True:
        print("\n1. Calculate voltage")
        print("2. Calculate resistance")
        print("3. Calculate current")
        print("4. Calculate power")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            current =get_positive_float("Current (A): ",allow_zero=True)
            resistance = get_positive_float("Resistance (ohms): ",allow_zero=True)


            voltage= calc_voltage(current, resistance)

            print(f"Voltage = {voltage} V")

        elif choice == "2":
            voltage = get_positive_float("Voltage (V): ",allow_zero=True)
            current = get_positive_float("Current (A): ")

            resistance = calc_resistance(voltage,current)

            print(f"resistance = {resistance} Ω")

        elif choice =="3":
            voltage = get_positive_float("Voltage (V): ",allow_zero=True)
            resistance = get_positive_float("resistance (o): ")

            current = calc_current(voltage,resistance)

            print(f"current = {current} amps")

        elif choice =="4":
            voltage = get_positive_float("Voltage (V):",allow_zero=True)
            current = get_positive_float("Current (A)",allow_zero=True)

            power = calc_power(voltage,current)

            print(f"power = {power} watts")

        elif choice == "5":
            print("Calculator closed.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
