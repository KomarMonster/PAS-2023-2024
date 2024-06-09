import socket

host = 'httpbin.org'
port = 80

request = (
    "GET /html HTTP/1.1\r\n"
    "Host: httpbin.org\r\n"
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A\r\n"
    "Connection: close\r\n"
    "\r\n"
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(request.encode())

    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

header_data, html_data = response.split(b'\r\n\r\n', 1)

with open('response.html', 'wb') as f:
    f.write(html_data)

print("Zapisano strone HTML jako 'response.html'")
