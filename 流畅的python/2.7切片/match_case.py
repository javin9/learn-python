def handle_http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # 默认情况
            return "Unknown Status"


# 测试
print(handle_http_status(200))  # OK
print(handle_http_status(404))  # Not Found
print(handle_http_status(999))  # Unknown Status
