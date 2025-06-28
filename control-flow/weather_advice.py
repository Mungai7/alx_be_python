

##current weather

weather_condition = input("What's the weather like today? (sunny/rainy/cold:")

if weather_condition == "sunny":

    print ("wear a t-shirt and sunglasses")

# Rainy = "Don't forget your umbrella and raincoat"
elif weather_condition == "Rainy":
    print("Don't forget your umbrella and raincoat")
    # cold = "Make sure to wear a warm coat and scarf"
elif weather_condition == "cold":
    print("Make sure to wear a warm coat and a scarf")

# invalid input 
else:
 print ("Sorry, I don't have recommendations for this weather.")
