option = "y"
while option == 'y':
    val1 = int(input('Enter first number: '))
    val2 = int(input('Enter second number: '))
    result = val1 + val2
    print('The sum of the two numbers is ', result)
    while True:
        print('Do you want to continue? Type Y/y if yes and N/n if no.')
        option = input('Choice: ').lower()
        if option == 'y':
            break
        elif option == 'n':
            break
        else:
            continue
print('Thankyou!')
