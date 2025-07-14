from datetime import datetime, timedelta

# 获取当前时间
current_time = datetime.now()

# 当前时间的时间戳（以秒为单位）
current_timestamp = current_time.timestamp()

# 当前时间往后推5个小时
new_time = current_time + timedelta(hours=5)

# 获取新的时间戳（以秒为单位）
new_timestamp = new_time.timestamp()

print("当前时间:", current_time)
print("当前时间戳:", current_timestamp)
print("当前时间往后推5个小时后的时间:", new_time)
print("往后推5个小时后的时间戳:", int(new_timestamp) * 1000)
