from socket import socket, AF_INET, SOCK_STREAM


def run_server(port=13331):
    srv = socket(AF_INET, SOCK_STREAM)
    srv.bind(("", port))
    srv.listen(1)

    while True:
        conn, _ = srv.accept()
        try:
            request = conn.recv(1024)
            path = request.split()[1].decode()
            with open(path.lstrip("/"), "rb") as file:
                response = b"HTTP/1.1 200 OK\r\n"
                response += b"Connection: close\r\n"
                response += b"Content-Type: text/html; charset=utf-8\r\n\r\n"
                response += file.read()
        except Exception:
            response = b"HTTP/1.1 404 Not Found\r\n"
            response += b"Connection: close\r\n"
            response += b"Content-Type: text/html; charset=utf-8\r\n\r\n"
            response += b"<h1>Not Found</h1>"

        conn.sendall(response)
        conn.close()


if __name__ == "__main__":
    run_server(13331)
