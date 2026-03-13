def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    
    return (fahrenheit - 32)* 5/9





def main():
    print("==TEMPERATURE CONVERTER==") 
    print("1. Celsius to fahrenheit")
    print("2. Farhenheit to celsius")
    
    
    
    choice = input("\nChoose Option (1/2): ")
    
    try:
        if choice == '1':
            celsius = float(input("Enter Temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}C = {fahrenheit:.2f}F")
        elif choice == '2':
            fahrenheit = float(input("enter temperature in Fahrenheit "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} F = {celsius: .2f} C")
            
        else:
            print("Invalid Choice") 
            
    except ValueError:
        print("Please enter a valid number")          
    

if __name__ == "__main__":
    main()
    
    
    