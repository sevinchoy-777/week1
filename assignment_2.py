a = int(input("Enter the number of paint tins: "))
s = 0
below = 0
inrange = 0
above = 0
def classify(b):
    if b < 748:
        return "Below range"
    elif 748 <= b <= 752:
        return "In range"
    else:
        return "Above range"
for i in range(a):
    b = int(input("Enter the tile width: "))
    s += b
    cat = classify(b)
    print(cat)
    if cat == "Below range":
        below += 1
    elif cat == "In range":
        inrange += 1
    else:
        above += 1
def calculate_average(total, count):
    return total / count
avg = calculate_average(s, a)
print(f"Total width: {s} ml")
print(f"Average width: {avg} ml")
print(f"Below range: {below}")
print(f"In range: {inrange}")
print(f"Above range: {above}")
