un 镜像，创建容器，启动容器
docker run -p 389:389 -p 636:636 --name my-openldap-container --env LDAP_ORGANISATION="ihopeit" --env LDAP_DOMAIN="ihopeit.com" --env LDAP_ADMIN_PASSWORD="admin_passwd_4_ldap" --detach osixia/openldap
修改了命令，添加权限，禁用 https
docker run -d --privileged -p 80:80 -p 443:443 --name phpldapadmin-service --hostname phpldapadmin-service --link my-openldap-container:ldap-host --env PHPLDAPADMIN_HTTPS=false --env PHPLDAPADMIN_LDAP_HOSTS=ldap-host --detach osixia/phpldapadmin
用户名、密码
CN=admin,DC=ihopeit,DC=com
admin_passwd_4_ldap

pip3 install django_python3_ldap