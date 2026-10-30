def replace_value(values, index, new_value):
    values[index] = new_value
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1
def summarize(values):
    stats_record = min(values),max(values),sum(values)
    return stats_record
def main():
    days = int(input("Enter the number of days: "))
    original = []
    for i in range (days):
        puzzles = int(input("Enter the number of puzzles solved: "))
        original.append(puzzles)
    updated = original[:]    
    index = int(input("Enter the index to correct: "))
    new_value = int(input("Enter the new number of puzzles: "))
    replace_value(updated, index, new_value)
    target = int(input("Enter the number of puzzles to searchh for: "))
    first_index = find_first(updated, target)
    matching_count = updated.count(target)
    minimum, maximum, total = summarize(updated)
    sorted_values = sorted(updated)
    print(f"Original: {original}")
    print(f"updated: {updated}")
    print(f"sorted {sorted_values}")
    print(f"Minimum number of puzzles: {minimum}")
    print(f"Maximum number of puzzles: {maximum}")
    print(f"Total number of puzzles: {total}")
    if first_index == -1:
        print("Target not found")
    else:
        print(f"First matching index: {first_index}")
    print(f"Matching values: {matching_count}")
if __name__ == "__main__":
        main()