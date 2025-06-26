

##current weather

weather = input("what's the weather like today?(Sunny/Cold/Rainy):")

if weather == "sunny":

    print ("wear a t-shirt and sunglasses")

# Rainy = "Don't forget your umbrella and raincoat"
elif weather == "Rainy":
    print("Don't forget your umbrella and raincoat")
    # cold = "Make sure to wear a warm coat and scarf"
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf")

# invalid input 
else:
 print ("Sorry, I don't have recommendations for this weather.")
