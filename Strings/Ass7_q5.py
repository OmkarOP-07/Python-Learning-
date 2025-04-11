# 5. Problem: Convert a list of temperatures from Celsius to Fahrenheit using map()
# Statement: Given a list of temperatures in Celsius, convert them to Fahrenheit using map().
# (Celsius * 1.8) + 32
celsius = [12,43,25,36]
farenhite = list(map(lambda a : a*1.8 + 32, celsius))

print(farenhite)