def caught_speeding(speed, is_birthday):
    if speed <= 60 if not is_birthday else speed <= 65:
        return 0
    elif speed <= 80 if not is_birthday else speed <= 85:
        return 1
    else:
        return 2