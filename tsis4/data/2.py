import datetime


today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday.strftime("%A"), yesterday)
print("Today:", today.strftime("%A"), today)
print("Tomorrow:", yesterday.strftime("%A"), tomorrow)



