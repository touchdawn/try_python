import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        #等待浏览器访问
        conn, addr = sock.accept()
        #接收浏览器发送来的内容
        data = conn.recv(1024)
        print(data)

        #给浏览器返回内容
        conn.send(b"HTTP/1.1 200 OK\r\n Content-Type:text/html; charset=utf-8\r\n\r\n")
        conn.send("Hello,World".encode("utf-8"))

        conn.close()


if __name__ == '__main__':
    main()
