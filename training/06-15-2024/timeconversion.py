def convert_seconds(k):
    hours = k // 3600  
    k %= 3600  
    minutes = k // 60  
    k %= 60  
    return hours, minutes, k
k = 7262
hours, minutes, seconds = convert_seconds(k)
print(f"{hours} h {minutes} min {seconds} sec.")
