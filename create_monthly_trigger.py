import datetime

def check_last_saturday():
    today = datetime.date.today()
    last_day = today.replace(day=28) + datetime.timedelta(days=4)
    last_saturday = last_day - datetime.timedelta(days=(last_day.weekday() + 2) % 7)
    return last_saturday == today

def create_monthly_trigger():
    print("Simulating scheduling of a pipeline to trigger every last Saturday of the month.")
    if check_last_saturday():
        print("Today is the last Saturday of the month. Triggering the pipeline...")
        # Simulate pipeline trigger
    else:
        print("Today is not the last Saturday of the month.")

if __name__ == "__main__":
    create_monthly_trigger()
