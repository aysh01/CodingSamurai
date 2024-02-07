import requests

while True:
  print("Welcome to Weather Forecast Application..")
  Location=input("Enter City / Location..\n")
  api_key = '46d0bd303abd42bfbfbd437a98eaefee'
  url = f"http://api.openweathermap.org/data/2.5/weather?q={Location}&appid={api_key}&units=metric"
  response = requests.get(url)
  data = response.json()

  if Location:
    if 'weather' not in data:
       print("Invalid Location..")
       continue

    print("Weather Forecast for..\n|---",Location,"----|")
    print("|---",data['weather'][0]['description'])
    print("|---",data['main']['temp'],"°C")
    print("|---",data['main']['humidity'],"%")
    print("|---",data['wind']['speed'],"m/s")
    # break
    a=input("Want to Convert Temperature Units..? Yes | No\n").lower()
    if a == 'yes':
      # F=data['main']['temp']*(9/5)+32
      # print(str(F))
      print("Weather Forecast for..\n|---",Location,"----|")
      print("|---",data['weather'][0]['description'])
      print("|---",data['main']['temp']*(9/5)+32,"°F")
      print("|---",data['main']['humidity'],"%")
      print("|---",data['wind']['speed'],"m/s")
    else:
      pass
      
  elif not Location:
    print("Location Cannot be Empty..")
    pass
  elif data["cod"] == "404":
    print("Location Not Found..")
    pass
