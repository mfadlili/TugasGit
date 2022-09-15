# app.py
from fungsi import kuadrat, akar

test_data = []
with open("data.txt", "r") as file:
    test = file.readlines()
    for row in test:
        test_data.append(int(row))

if __name__ == "__main__":
    for bilangan in test_data :
        power = kuadrat(bilangan)
        root = akar(bilangan)
        print(f"Kuadrat dari {bilangan} adalah {power}, adapun akarnya adalah {root}.")    