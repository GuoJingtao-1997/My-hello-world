#!/usr/bin/env python
# -*- coding : utf-8 -*-
print('What do you think I am')
right = False
while right is False:
    answer = input()
    if answer == 'good' or answer == 'beautiful':
        print('Oh yes Du bist ', end=answer)
        print()
    elif answer == 'bad':
        print('What is your problem?')
        right = True
    else:
        print('You do not really know me')
