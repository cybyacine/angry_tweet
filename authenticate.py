
from ldap3 import Connection, Server, ALL
from ldap3.core.exceptions import LDAPBindError
import socket_client


def authenticate():
    server_uri = f"ldap://192.168.76.140:389"
    server = Server(server_uri, get_info=ALL)
    username = input('Enter username : ')
    password = input("saisir votre mot de passe : ")
    try:
        # Provide the hostname and port number of the openLDAP
        server = Server(server_uri, get_info=ALL)
        # username and password can be configured during openldap setup
        connection = Connection(server,
                                user='uid=ybenouirane,ou=users,dc=tekup,dc=local',
                                password='ybenouirane')
        bind_response = connection.bind()  # Returns True or False
        print(bind_response)
        if bind_response:
            socket_client.start()
        connection.unbind()
    except LDAPBindError as e:
        connection = e
    finally:
        connection.unbind()

authenticate()