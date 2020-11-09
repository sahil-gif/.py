def swapFileData():
    file1 = open("D:\whitehatjr\project98\Sahil.txt")
    file2 = open("D:\whitehatjr\project98\Parikshit.txt")


    with open(file1, 'r') as s:
    data1 = s.read()

    with open(file2, 'r') as p:
    data2 = p.read()

    with open(file1, 'w') as s:
    s.write(data2)

    with open(file2, 'w') as p:
    p.write(data1)

swapFileData()