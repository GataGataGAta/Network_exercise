import datetime

now = datetime.datetime.now()  # 現在日時の取得
print(now)  # 日時の表示
print(now.year)  # 年の表示
print(now.month)  # 月の表示
print(now.day)  # 日の表示
print(now.hour)  # 時の表示
print(now.minute)  # 分の表示
print(now.second)  # 秒の表示

some_day = datetime.date(2023, 6, 8)  # 特定日付の取得
print(some_day)

some_day1 = datetime.datetime.fromisoformat("2023-06-08")  # 特定日付（文字列）の取得
print(some_day1)

some_time = datetime.time(16, 27, 30)  # 特定時刻の取得
print(some_time)

some_daytime = datetime.datetime.combine(some_day, some_time)  # 日付と時刻の連結
print(some_daytime)
print(some_daytime.date())  # 日付の表示
print(some_daytime.time())  # 時刻の表示

rest = now - some_daytime  # 日時の引き算
print(rest)
print(rest.days)  # 日数の表示
print(rest.seconds)  # 秒数の表示