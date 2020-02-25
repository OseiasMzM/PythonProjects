print(' -- ICM CALCULATOR -- ')
alt = float(input("Type your height: "))
ps = float(input("Type your weight: "))

x = alt * alt
y = ps / x

if y <= 18.5:
    print("Your ICM is {:.2f}, you are underweight!".format(y))
elif y > 18.5 and y <= 24.9:
    print("Your ICM is {:.2f}, you are normal weight!".format(y))
elif y >= 25 and y <= 29.9:
    print("Your ICM is {:.2f}, you are overweight!".format(y))
elif y > 30 and y <= 34.9:
    print("Your ICM is {:.2f}, you are with grade 1 obesity!".format(y))
elif y > 35 and y <= 39.9:
    print("Your ICM is {:.2f}, you are with grade 2 obsity!".format(y))
elif y > 40:
    print("Your ICM is {:.2f}, you are with grade 3 obsity!".format(y))


for i in range(5):
    print("")

print("Developed by Oséias Martins (GitHub -> OseiasMzM) \nin order to feed his knowledge in the Python Language")
