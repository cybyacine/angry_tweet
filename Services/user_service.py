import ldap3

from Entities.user import User


class UserService:
    connection = None
    PASSWORD = "tekup"
    server_uri = f"ldap://192.168.76.140:389"

    def __init__(self):
        self.connect_ldap()

    def connect_ldap(self):
        print("INITIALIZING LDAP SERVER...")
        server = ldap3.Server(self.server_uri, get_info=ldap3.ALL)
        self.connection = ldap3.Connection(server,
                                           user='cn=admin,dc=tekup,dc=local',
                                           password=self.PASSWORD)
        # At this point, we're connected as an anonymous user
        # If we want to be associated to an account
        # you can log by binding your account details to your connection
        self.connection.bind()
        print("LDAP Server Listening...")

    def add_user(self, user):
        print("ADDING USER")
        dn = "uid=" + user.name + ",ou=Users,dc=chat,dc=app"
        modlist = {
            "objectClass": ["inetOrgPerson", "person"],
            "uid": user.name,
            "sn": user.surname,
            "givenName": user.name,
            "cn": user.name + " " + user.surname,
            "displayName": user.name + " " + user.surname,
            "userPassword": user.password,
            "description": user.card_number,
            "mail": user.email
        }
        # USE "strongAuthenticationUser" objectClass for Certification, it needs a binary file,
        # addModList transforms your dictionary into a list that is conformed to ldap input.
        result = self.connection.add(dn, ldap3.modlist.addModlist(modlist))
        print("User ADDED!")
        print("Result : " + str(result))
        self.connection.unbind()

    def delete_user(self, uid):
        # ----------- deleting (a user) -----------
        print("Deleting user " + uid)
        dn = "uid=" + uid + ",ou=Users,dc=chat,dc=app"
        self.connection.delete(dn)

    def search_user(self, uid):
        ldap_base = "ou=Users,dc=tekup,dc=local"
        query = "(uid=" + uid + ")"
        try:
            self.connection.search(search_base=ldap_base, search_scope=ldap3.LEVEL, search_filter=query, attributes=ldap3.ALL_ATTRIBUTES)
            entry = self.connection.entries[0]
            if not entry:
                print("User not found")
                return None
            else:
                uid = entry['uid']
                surname = entry['sn']
                name = entry['givenName']
                password = entry['userPassword']
                email = entry['mail']
                user = User(uid, name, surname, email, password, "")
                return user
        except Exception as e:
            print("Error in SEARCH USER " + e)
            return None
        finally:
            self.connection.unbind()
            print("Connection closed!")
