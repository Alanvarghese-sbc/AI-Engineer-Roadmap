def get_integer(prompt, min_value=None, default=None):
    while True:
        val = input(prompt).strip()

        if not val:
            return default
        try:
            val = int(val)
            if min_value is not None and val < min_value:
                print(f"Enter a value greater than or equal to {min_value}.")
                continue
            return val
        except ValueError:
            print("Enter a valid number : ")
    

def get_float(prompt, min_value=None, default=None):
    while True:
        val = input(prompt).strip()
        if not val:
            return default
        try:
            val = float(val)
            if min_value is not None and val <min_value:
                 print(f"Enter a value greater than or equal to {min_value}.")
                 continue
            return val
        except ValueError:
            print("Enter a valid number : ")
