from fungsi import kuadrat, akar

test_data = []
with open("data.txt", "r") as file:
    test = file.readlines()
    for row in test:
        test_data.append(int(row))

    