#TempConvert.py
#Name:Liam Gillispie
#Date:2/8/26
#Assignment:Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  print("Hello User!")
  name=input("What is your name User?")
  print(f"Welcome {name}")
  temp_f=input("What is the temperature outside in Fahenheit?")
  #Convert that temperature to celsius, rounding to 1 decimal percision

  #Output converted temperature.
  tempF=float(temp_f)

  tempC=round((tempF-32)*5/9,0)

  print(f"{tempF}F is {tempC}C")
if __name__ == '__main__':
    main()
    