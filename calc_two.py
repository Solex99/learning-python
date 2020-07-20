# answer 1
answer_one =  (17 + 94) / (-5 + -5)


# answer 2
answer_two =  (17 + 94) / (-5 + 0)


# answer 3
try:
    answer_three =  (17 + 94) / (-5 + 5)
except ZeroDivisionError:
    answer_three = "That cant be done!"


print (answer_one)
print (answer_two)
print (answer_three)