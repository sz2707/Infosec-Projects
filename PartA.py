def convert_sec():
    days = int(input("Enter the number of days: "))
    seconds = days*24*60*60
    print(f" {days} equates to {seconds} seconds")
    return seconds

convert_sec()