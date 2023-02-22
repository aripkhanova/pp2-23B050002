from datetime import datetime, timedelta
print("Yesterday: ", datetime.now() - timedelta(days=1))
print("Current time: ", datetime.now())
print("Tomorrow: ", datetime.now() + timedelta(days=1))