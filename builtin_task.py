# Task

#- get user input of a float number
#- check if the number is lower than .50 then round the figure to lower end
#- check if the number is greater than .51 then round the figure to higher end
#- example - num_float = 23.66 - round it to 24, num_float = 23.50 - round it to lower end

user_inp = float(input("Input a decimal number: ")
user_inp_float = user_inp - floor(user_inp)
if user_inp_float < 0.51:
    user_inp_floor = floor(user_inp)
    print(user_inp_floor)
else:
    user_inp_ceil = ceil(user_inp)


#### ALTERNATIVE METHOD

    if number % 1 < 0.5:
        print(math.floor(number))
    else:
        print(math.ceil(number))
