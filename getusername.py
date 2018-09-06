from keystoneauth1.identity import v3
from keystoneauth1 import session
import keystoneclient.v3
from keystoneclient.v3 import client

# Credentials
auth_url_adm="http://192.168.125.100:35357/v2.0"
auth_url_pub="http://192.168.123.100:5000/v3"
username="admin"
password="qwerty"
tenant_name="demo"
project_name="admin"
user_domain_id="default"
project_domain_id="default"

auth = v3.Password(auth_url=auth_url_pub,
                   username=username,
                   password=password,
                   project_name=project_name,
                   user_domain_id=user_domain_id,
                   project_domain_id=project_domain_id)
sess = session.Session(auth=auth)
keystone = client.Client(session=sess)

# FN Get project name
def get_project_name (uid, project_count):
    try:
        user_project_name = keystone.role_assignments.list(user=uid, include_names=True)[project_count].scope['project']['name']
    except:
        user_project_name = "none"
    return user_project_name

# FN Get role name
def get_role_name (uid, project_count):
    try:
        user_role_name = keystone.role_assignments.list(user=uid, include_names=True)[project_count].role['name']
    except:
        user_role_name = "none"
    return user_role_name

# Get user list

print("=" * 40)
print("List of usres:")
print("=" * 40 + "\n")

for i_user in range (len(keystone.users.list())):
    print("-" * 40)
    i_user_name = str(keystone.users.list()[i_user].name)
    i_user_id = str(keystone.users.list()[i_user].id)
    i_user_project_count = (len(keystone.role_assignments.list(user=i_user_id)))

    if i_user_project_count == 1:
        i_user_project_name = get_project_name(i_user_id, 0)
        i_user_role_name = get_role_name(i_user_id, 0)
        print("User name: \t" + i_user_name)
        print("Project mane: \t" + str(i_user_project_name))
        print("Role mane: \t" + str(i_user_role_name) + "\n")
    else:
        for i_prj_count in range (i_user_project_count):
            i_user_project_name = get_project_name(i_user_id, i_prj_count)
            i_user_role_name = get_role_name(i_user_id, i_prj_count)
            print("User name: \t" + i_user_name)
            print("Project mane: \t" + str(i_user_project_name))
            print("Role mane: \t" + str(i_user_role_name) + "\n")
            
print("#" * 40)

