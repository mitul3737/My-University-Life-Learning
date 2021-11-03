str_0=int(input("")[1:-1])

def ymd(num):
    year_0=num//365
    r_year_0=num/365-num//365
    num=r_year_0*365
    month_0=round(num//30)
    r_month_0=num/30-num//30
    num=round(r_month_0*30)
    day_0=num
    print(f"{year_0} years, {month_0} months and {day_0} days")

ymd(str_0)