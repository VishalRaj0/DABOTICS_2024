from datetime import datetime
not_now = datetime.now().replace(hour=1, minute=0, second=0)
now = datetime.now()
print(not_now - now)