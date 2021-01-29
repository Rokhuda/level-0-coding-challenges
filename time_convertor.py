def time_convertor(num):

    hours = num // 60
    minutes = num % 60
    
    if hours < 1 and minutes < 1:
        return (str(hours) + " hour, " + str(minutes) + " minute")
    elif hours <= 1:
        return (str(hours) + " hour, " + str(minutes) + " minutes")
    elif minutes <= 1:
        return (str(hours) + " hours, " + str(minutes) + " minute")
    else:
        return (str(hours) + " hours, " + str(minutes) + " minutes")


print(time_convertor(0))

