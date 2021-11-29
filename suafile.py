with open("data.csv", 'r', encoding='utf-8') as f:
    datalist = f.readlines()
for data in datalist:
    with open("data2.csv", 'a', encoding="utf-8") as f:
        dot = data.rfind(",")
        f.write(data[:dot]+";"+data[dot+1:])
