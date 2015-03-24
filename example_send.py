"""

This file demonstrates how not to send file using os.sendfile().
This file also demonstrate use of socket.send(), which can be use to handle virtual files 
(StringIO)

"""

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler, DTPHandler
from pyftpdlib.servers import FTPServer


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', os.getcwd(), perm='elradfmw')
    authorizer.add_anonymous(os.getcwd())
    dtp_handler = DTPHandler
    dtp_handler.use_sendfile = False   
    ftp_handler = FTPHandler
    ftp_handler.authorizer = authorizer
    ftp_handler.dtp_handler = dtp_handler
    server = FTPServer(('', 2121), ftp_handler)
    server.serve_forever()

if __name__ == '__main__':
    main()
