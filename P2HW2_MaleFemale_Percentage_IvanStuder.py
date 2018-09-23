# Finding out Male and Female percentages
# 9/20/2018
# CTI-110 P2HW2 Male Female Percentage 
# Ivan Studer

#Get total number of males registered for class.
Males = int(input(' Enter total number of males registered: '))

#Get total number of females.
Females = int(input(' Enter total number of females registered: '))

#Find out the total number of Males and Females.
total_number_students = Males + Females

#Calculate male percentage.
male_percentage = Males / total_number_students

#Calculate female percantage.
female_percentage = Females / total_number_students

#Display the percentages.
print('The percanteges registered for the class:')
print('Males %', format(male_percentage, ',.2f'))
print('Females %', format(female_percentage, ',.2f'))
