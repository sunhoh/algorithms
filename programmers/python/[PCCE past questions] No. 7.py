
def valSet(value):
    if value >= 0 and value < 10:
        return '5단계'
    elif value >= 10 and value < 20:
        return '4단계'
    elif value >= 20 and value < 30:
        return '3단계'
    elif value >= 30 and value < 40:
        return '2단계'
    elif value >= 40 and value < 50:
        return '1단계'
    else :
        return '0단계'

def solution(mode_type, humidity, val_set):
    if mode_type == "auto":
        return valSet(humidity)
    elif mode_type == "target":
        if humidity < val_set:
            return '3단계'
        elif humidity >= val_set:
            return '1단계'
    elif mode_type == "minimum":
        if humidity < val_set :
            return '1단계'
        elif humidity >= val_set :
            return '0단계'

print(solution("auto",23,45))