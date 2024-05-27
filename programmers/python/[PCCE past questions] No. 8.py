def solution(storage, num):
    hash = {}
    max_key = ''
    max_value = 0

    for item, count in zip(storage, num):
        if item in hash:
            hash[item] += count
        else:
            hash[item] = count
    
    for key, value in hash.items():
        if value > max_value:
            max_value = value
            max_key = key

    max_item = max(hash, key=hash.get)
    print(max_item, max_value, max_key)

solution(["pencil", "pencil", "pencil", "book"],[2, 4, 3, 1])
