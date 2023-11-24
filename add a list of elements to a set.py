#Given a Python list, Write a program to add all its elements into a given set.

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

sample_set.update(sample_list)

sample_set


#Expected output {'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
