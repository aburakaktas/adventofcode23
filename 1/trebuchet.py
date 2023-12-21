def find_first_digit(raw_key: str):
    for char in raw_key:
        if char.isnumeric():
            return char
            

def find_last_digit(raw_key: str):
    for char in raw_key[::-1]:
        if char.isnumeric():
            return char

change = {
    "one" : "one1one",
    "two" : "two2two",
    "three" : "three3three",
    "four" : "four4four",
    "five" : "five5five",
    "six" : "six6six",
    "seven" : "seven7seven",
    "eight" : "eight8eight",
    "nine" : "nine9nine"
}


def main():
    sum = 0
    with open("data.txt") as file:
        for line in file:
            raw_key = line.strip()
            for key, value in change.items():
                raw_key = raw_key.replace(key, value)
            first_digit = find_first_digit(raw_key)
            last_digit = find_last_digit(raw_key)
            code = first_digit + last_digit
            sum += int(code)
    print(sum)
                


if __name__ == "__main__":
    main()