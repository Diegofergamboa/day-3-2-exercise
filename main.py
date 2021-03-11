# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Pivote variable
bmi = weight / ( height ** 2)

#Operational algorithm

if bmi >= 18.5 and bmi < 25 :
	print('normal weight')
elif bmi >= 25 and bmi < 30 :
	print('overweight')
elif bmi >= 30 and bmi < 35 :
	print('obese')
elif bmi >= 35 :
	print('clinical obese')
else: 
	print('underweight')




