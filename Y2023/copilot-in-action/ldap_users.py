import ldap

ldap_server = "ldap://your-ldap-servername-or-ip"
ldap_port = 389  # Default port for LDAP
ldap_user = "cn=admin,dc=example,dc=com"  # Usually a privileged user
ldap_password = "your-password"


# Bind to the LDAP server using the provided user and password
ldap_conn = ldap.initialize(ldap_server)
try:
    ldap_conn.simple_bind_s(ldap_user, ldap_password)
    print("Successfully connected to LDAP server!")
except ldap.LDAPError as e:
    print("Error connecting to LDAP server: ", e)
    exit(1)


# Search for all user objects in the LDAP directory
search_base = "ou=people,dc=example,dc=com"   # Change this to match your LDAP directory structure
search_filter = "(objectClass=person)"       # Filter to retrieve only user objects
try:
    search_result = ldap_conn.search_s(search_base, ldap.SCOPE_SUBTREE, search_filter)
    print("Retrieved", len(search_result), "user objects from the LDAP server:")
    for uid, user_data in search_result:
        if "uid" in user_data:
            # Print the user data in a readable format
            print("UID:", user_data["uid"][0])
            if "cn" in user_data:
                print("Name:", user_data["cn"][0])
            if "mail" in user_data:
                print("Email:", user_data["mail"][0])
            print()
except ldap.LDAPError as e:
    print("Error searching LDAP directory: ", e)
finally:
    ldap_conn.unbind()
