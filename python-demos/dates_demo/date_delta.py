""" date delta module """

from datetime import datetime, timedelta
import time

start = datetime.now()

time.sleep(2)

# end = start + timedelta(days = 20)
end = datetime.now()

print(start)
print(end)
print(end - start)
print(type(end - start))
