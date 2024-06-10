def isPangram(data):
    for x in range(ord('a'),ord('z')+1):
        if chr(x) not in data:
            return "NO"
    return "YES"


get = str(input("Enter: "))
get.lower()

print(isPangram(get))
