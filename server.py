import socket
import threading
import socketserver


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # self.request.recv(1024)
        # self.request.sendall(response)
        print(self.request.recv(1024))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 1021

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.deamon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    # wait until thread ends ..
    server_thread.join()
    server.shutdown()
    server.server_close()
