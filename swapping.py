def SwappingFile():

    fileName1 = input("Enter the file name:- ")
    file1 = open(fileName1, 'r')

    fileName2 = input("Enter the file name:- ")
    file2 = open(fileName2, 'r')

    with open(file1, 'r') as a:
    data_a = a.read()
    
    with open(file2, 'r') as b:
    data_b = b.read()

    with open(file1, 'w') as a:
    a.write(data_b)

    with open(file2, 'w') as b:
    b.write(data_a)