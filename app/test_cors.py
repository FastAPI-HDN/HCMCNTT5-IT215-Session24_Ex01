import requests

URL = "http://127.0.0.1:8000/api/profile"

# 1. Giả lập kẻ tấn công từ Origin lạ
headers_evil = {
    "Origin": "https://evil-attacker.xyz",
    "X-User-Role": "ADMIN"
}
res_evil = requests.get(URL, headers=headers_evil)

print("=== TEST 1: ORIGIN BẤT HỢP PHÁP ===")
print("Origin gửi đi:", headers_evil["Origin"])
print("Header Access-Control-Allow-Origin trả về:",
      res_evil.headers.get("access-control-allow-origin"))
if "access-control-allow-origin" not in res_evil.headers:
    print("=> KẾT QUẢ: THÀNH CÔNG CHẶN CORS (Không có header cho phép truy cập)")

print("\n" + "="*40 + "\n")

# 2. Giả lập Frontend nội bộ hợp lệ
headers_valid = {
    "Origin": "https://internal.megamart.com",
    "X-User-Role": "ADMIN"
}
res_valid = requests.get(URL, headers=headers_valid)

print("=== TEST 2: ORIGIN HỢP LỆ ===")
print("Origin gửi đi:", headers_valid["Origin"])
print("Header Access-Control-Allow-Origin trả về:",
      res_valid.headers.get("access-control-allow-origin"))
