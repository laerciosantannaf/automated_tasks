import paramiko


def is_alive(app_name):
 stdin, stdout, stderr = client.exec_command(f'ps aux | grep "[{app_name[:1]}]{app_name[1:]}.jar" | wc -l')
 return stdout.read().decode('ascii').strip('\n')


print('Connecting to server')
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
client.connect('<host_ip>', username='<username>', key_filename='path/key.pem')

apps = ['app_name']

for app in apps:
 print(f'Killing {app}')
 client.exec_command(f'pkill -f {app}.jar')
 assert int(is_alive(app)) == 0, f"{app} still alive!"

 print(f'Restarting {app}\n')
 client.exec_command(f'./path/file.sh>')
 assert int(is_alive(app)) == 1, f'{app} still dead!'
