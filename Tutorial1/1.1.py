def sec_to_hms(sec):
    hrs = sec // 3600
    mins = (sec % 3600) // 60
    secs = sec % 60
    return f"{hrs:02}:{mins:02}:{secs:02}"

seconds = int(input("Enter the time in seconds: "))
formatted_time = sec_to_hms(seconds)
print("Time in HH:MM:SS format:", formatted_time)
