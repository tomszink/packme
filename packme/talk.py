import datetime

# can be called by: packme.talk.tell_me_the_time()
def tell_me_the_time():
    dt_now = datetime.datetime.now()
    print(f"Hey, current time is: { dt_now.strftime('%H:%M') }")