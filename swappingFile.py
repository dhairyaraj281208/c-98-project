def swapFileData():
    file2 = "C:\\Users\\Dhairya\\Desktop\\python\\c 98\\project\\c_98_ project\\sampleText2.txt"
    file1 = "C:\\Users\\Dhairya\\Desktop\\python\\c 98\\project\\c_98_ project\\sampleText1.txt"

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as b:
        data_b = b.read()

    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file2, 'w') as a:
        a.write(data_a)

    print("Successfully Swaped!")

swapFileData()