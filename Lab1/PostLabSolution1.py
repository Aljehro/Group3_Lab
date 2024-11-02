# CPE106L-4/E01
# Lab1 || Postlab #1
# Group #3 Members: Abante, Alarilla, Fernandez

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sort_num = sorted(numbers)
    n = len(sort_num)
    mid = n // 2
    if n % 2 == 0:
        return (sort_num[mid - 1] + sort_num[mid]) / 2
    return sort_num[mid]

def mode(numbers):
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1
    max_freq = max(frequency.values())
    modes = [k for k, v in frequency.items() if v == max_freq]
    return modes

def main():
    while True:
        user_input = input("Enter a list of numbers separated by spaces. (Type 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Terminating program.....")
            break

        try:
            data = list(map(float, user_input.split()))
            print("Data:", data)
            print("Mean:", mean(data))
            print("Median:", median(data))
            print("Mode:", mode(data))
        except ValueError:
            print("Invalid input.")

if __name__ == "__main__":
    main()
