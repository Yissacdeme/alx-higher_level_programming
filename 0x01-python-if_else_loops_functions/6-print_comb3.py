#!/usr/bin/python3
for num_one in range(10):
    for num_two in range(10):
        if (num_one != num_two and num_one < num_two) and num_one < 9:
            if (num_one == 8 and num_two == 9):
                print('{0}{1}'.format(num_one, num_two))
            else:
                print('{0}{1}, '.format(num_one, num_two), end='')
