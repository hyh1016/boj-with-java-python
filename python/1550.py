def get_hex(target):
    if target.isdigit():
        return int(target)
    ascii_code = ord(target)
    if 65 <= ascii_code <= 70:
        return ascii_code - 55


number = list(input())
result = 0
for idx, val in enumerate(reversed(number)):
    result += pow(16, idx) * get_hex(val)
print(result)