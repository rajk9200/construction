from datetime import datetime, timedelta

N = 2

date_N_days_ago = datetime.now() - timedelta(days=N)

print(datetime.now().strftime("%d-%m-%y"))
print(date_N_days_ago.strftime("%d-%m-%y"))
