import datetime

def tell_the_time():
    dt_now = datetime.datetime.now()
    print(f"Hey, current time is: { dt_now.strftime('%H:%M') }")

if __name__ == "__main__":
    tell_the_time()