from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
import os, socket

HOSTNAME = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
PORT = 5555

print ("Starting Server...")

directory = os.path.expanduser(r"the folder which you want to act as a server")

authorizer = DummyAuthorizer()
authorizer.add_user("admin", "123", directory, perm='elradfmw')
authorizer.add_user("user", "321", directory, perm='elradfmw')
handler = FTPHandler
handler.authorizer = authorizer

connection = (HOSTNAME, PORT)
server = FTPServer(connection, handler)

server.serve_forever()
