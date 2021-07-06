#2
'''
Take the temperature of five different countries in Centigrade
and finally, Convert all temperatures from Centigrade to Fahrenheit.
Also, print individual temperatures of all countries and find the average temperature value.
Reference Equation: C = (5/9) * (F -32)
'''

temperature_centigrade = []
temperature_fahrenheit = []
print("Enter temperature of five different countries in Centigrade:")
for t in range(1,6):
    temp = float(input())
    temperature_centigrade.append(temp)
    temperature_fahrenheit.append((temp * 1.8) + 32 )

print("\nIndividual temperatures of all countries:")
for i in temperature_fahrenheit:
    print(str(i)+" F")
print("Average average temperature value: "+str(sum(temperature_fahrenheit)/len(temperature_fahrenheit))+" F")