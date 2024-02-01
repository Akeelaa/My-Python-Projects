# I want print out a fortune for the user, whos wondering
# whats going to happen to them.

import random

Lucky_number = random.randint(1,100)

fortune_number = random.randint(1,3) # Allows us to have 3 diffent fortunes 
fortune_text = '' # empty string

# so if the 1, 2 or 3 and change the fortune text string
# depending on those situations.

if fortune_number == 1:
    fortune_text = 'You Will Have A Great Day!'
if fortune_number == 2:
   fortune_text = 'Today is going to be tough...but worth it'
if fortune_number == 3:
    fortune_text == 'You will get married this year'
    


print(f" {fortune_text}, Your lucky number is: {Lucky_number}")




