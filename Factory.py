print("Welcome to Yamba Tech Gadgets! Grab yours now with promos & Freebies!")
order = ""

class Gadgets:
    def __init__(self, brands):
        self.brands = brands

    def print(self):
        print(self.brands)

class GadgetsFactory:
    def createSmartPhone(self):
        brands = ["Lenovo", "Samsung", "Huawei", "Vivo", "Realme"]
        return Gadgets(brands)

    def createLaptop(self):
        brands = ["Acer", "Asus", "Apple", "HP", "Razer"]
        return Gadgets(brands)
        
    def createDigitalCamera(self):
        brands = ["Canon", "Sony", "Nikon", "Panasonic"]
        return Gadgets(brands)
        
    def createPrinter(self):
        brands = ["Epson", "Brother", "Panasonic", "Xerox"]
        return Gadgets(brands)
        
class Gadgets:
    def __init__(self, freebies):
        self.freebies = freebies

    def print(self):
        print(self.freebies)

class GadgetsFreebiesFactory:
    def createSmartPhone(self):
        freebies = ["Fast Charger", "Headset", "Casing", "Phone Ring Light"]
        return Gadgets(freebies)

    def createLaptop(self):
        freebies = ["Charger", "Headset", "Mouse", "USB Hub", "Keyboard Film", "Laptop Bag"]
        return Gadgets(freebies)
        
    def createDigitalCamera(self):
        freebies = ["Charger", "Lenses", "64Gb SD Card", "Tripods"]
        return Gadgets(freebies)
        
    def createPrinter(self):
        freebies = ["Charger", "Inks", "Bond Paper", "HDMI"]
        return Gadgets(freebies)
        
gadgetsFactory = GadgetsFactory()
gadgetsfreebiesFactory = GadgetsFreebiesFactory()


def introduction():
    print("Visit at Camaman-an Tierra Delpuerto CDO at Cjane Building 3rd floor ")
    print("1. SmartPhone \n2. Laptop \n3. Digital Camera \n4. Printer")
    order = int (input("\nChoose a number: "))


    if(order == 1):
        print("\nThis is the Following brands of SmartPhone: ")
        gadgetsFactory.createSmartPhone().print()

        print("You can now choose any of the available Brands (okay)")
        question = input()
        
        if(question == 'okay'): 
            print("Congratulation you own: SmartPhone with Freebies")
        elif(question == 'no'):
            return introduction(), 
        else:
            print("Choices not available")
            
        gadgetsfreebiesFactory.createSmartPhone().print()
        
    if(order == 2):
        print("\nThis is the Following brands of Laptop: ")
        gadgetsFactory.createLaptop().print()
            
        print("You can now choose any of the available Brands (okay)")
        question = input()

        if(question == 'okay'): 
            print("Congratulation you own: Laptop with Freebies ")
        elif(question == 'no'):
            return introduction(), 
        else:
            print("Choices not available")
                
        gadgetsfreebiesFactory.createLaptop().print()

    if(order == 3): 
        print("\nThis is the Following brands of Digital Camera: ")
        gadgetsFactory.createDigitalCamera().print()  
            
        print("You can now choose any of the available Brands (okay)")
        question = input()

        if(question == 'okay'): 
            print("Congratulation you own: Digital Camera with Freebies")
        elif(question == 'no'):
            return introduction(), 
        else:
            print("your choices is not available")
                
        gadgetsfreebiesFactory.createDigitalCamera().print()
                
    if(order == 4): 
        print("\nThis is the Following brands of Printer: ")
        gadgetsFactory.createPrinter().print()  
            
        print("You can now choose any of the available Brands (okay)")
        question = input()

        if(question == 'okay'): 
            print("Congratulation you own: Printer with Freebies")
        elif(question == 'no'):
            return introduction(), 
        else:
            print("your choices is not available")
                
        gadgetsfreebiesFactory.createPrinter().print()
        

introduction()

