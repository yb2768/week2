# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))

    # Fill in start
    serverSocket.listen(1)
    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            # Receive request message from the client
            message = connectionSocket.recv(1024)
            filename = message.split()[1].decode()

            # Open the requested file
            f = open(filename[1:], "rb")
            file_data = f.read()
            f.close()

            # Create HTTP response header for valid request
            header = (
                "HTTP/1.1 200 OK\r\n"
                "Server: SimplePythonWebServer\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                "Content-Length: " + str(len(file_data)) + "\r\n"
                "Connection: close\r\n"
                "\r\n"
            ).encode()

            # Send header and file content in ONE send
            connectionSocket.send(header + file_data)

            connectionSocket.close()

        except Exception:
            # Create HTTP response for file not found
            body = b"<html><body><h1>404 Not Found</h1></body></html>"
            header = (
                "HTTP/1.1 404 Not Found\r\n"
                "Server: SimplePythonWebServer\r\n"
                "Content-Type: text/html; charset=UTF-8\r\n"
                "Content-Length: " + str(len(body)) + "\r\n"
                "Connection: close\r\n"
                "\r\n"
            ).encode()

            # Send 404 response in ONE send
            connectionSocket.send(header + body)

            connectionSocket.close()


if __name__ == "__main__":
    webServer(13331)
