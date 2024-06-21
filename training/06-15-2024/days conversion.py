def convert_days(total_days):
   
    days_in_year = 360
    days_in_month = 30
    days_in_week = 6
    
    years = total_days // days_in_year
    remaining_days = total_days % days_in_year
    
    months = remaining_days // days_in_month
    remaining_days %= days_in_month
    
    weeks = remaining_days // days_in_week
    remaining_days %= days_in_week
    
    return years, months, weeks, remaining_days


total_days = 65476

years, months, weeks, days = convert_days(total_days)

print(f"  {years} y {months} mon {weeks} w {days}d")
