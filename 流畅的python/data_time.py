from datetime import datetime, timedelta


def get_data():
    start_time = '2025-07-09'
    start_time_date = datetime.strptime(start_time, '%Y-%m-%d')
    print(start_time_date)
    for i in range(10):
        start_time_date += timedelta(days=1)
        print(start_time_date)


def yield_data():
    start_time = '2025-07-09'
    start_time_date = datetime.strptime(start_time, '%Y-%m-%d')
    for i in range(10):
        start_time_date += timedelta(days=1)
        yield start_time_date


def return_data():
    start_time = '2025-07-09'
    start_time_date = datetime.strptime(start_time, '%Y-%m-%d')
    for i in range(10):
        start_time_date += timedelta(days=1)
        return start_time_date


if __name__ == '__main__':
    get_data()
    print('-' * 100)
    for i in yield_data():
        print(i)

    print('-' * 100)
    print(return_data())
