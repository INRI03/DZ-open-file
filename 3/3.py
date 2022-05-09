
file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
main = 'all.txt'

def docs(a, b, c):
    data1 = []
    data2 = []
    data3 = []
    with open(a, 'r', encoding="utf-8") as f1:
        data1 += [file1, len(f1.readlines())]
    with open(a, 'r', encoding="utf-8") as f1:
        data1.append(f1.read())
    with open(b, 'r', encoding="utf-8") as f2:
        data2 += [file2, len(f2.readlines())]
    with open(b, 'r', encoding="utf-8") as f2:
        data2.append(f2.read())
    with open(c, 'r', encoding="utf-8") as f3:
        data3 += [file3, len(f3.readlines())]
    with open(c, 'r', encoding="utf-8") as f3:
        data3.append(f3.read())

    list_ = [data1, data2, data3]
    sort = sorted(list_, key = lambda l : l[1])

    def complete(d):
        with open(d, 'a', encoding="utf-8") as f:
            for elem in sort:
                for line in elem:
                    f.write(str(line) + '\n')

        with open(d, 'r', encoding="utf-8") as f:
            print(f.read())

    complete(main)

docs(file1, file2, file3)
