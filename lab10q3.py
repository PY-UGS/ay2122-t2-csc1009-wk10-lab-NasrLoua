def q2b():
    switcher = {
        'CSC1006': 'Mathematics 2',
        'CSC1007': 'Operating Systems',
        'CSC1008': 'Data Structure and Algorithms',
        'CSC1009': 'Object Oriented Programming',
        'CSC1010': 'Computer Networks'
    }
    print(switcher[input("Please input a module number: ")])  # switch case equivalent


def q2c():
    for i in range(102, 66, -1):
        if i % 2 != 0:
            print(i)


q2b()
q2c()
