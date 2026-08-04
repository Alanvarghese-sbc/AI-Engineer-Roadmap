ch = input("Select a language choice : 1 - English \n 2 - Malayalam \n 3 - Hindi \n 4 - Tamil \n enter (1,2,3,4)")


match ch:

    case "1":
        print("Welcome user")

    case "2":
        print("സ്വാഗതം ഉപയോക്താവ്")

    case "3":
        print("उपयोगकर्ता का स्वागत है")

    case "4":
        print("பயனரே வருக ")

    case _:
        print("Invalid")