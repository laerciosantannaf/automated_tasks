import paramiko


class RestartRemoteApp:
 cli = None

 def __int__(self, host, username, key_path):
  self.cli = paramiko.client.SSHClient()
  self.cli.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
  self.cli.connect(host, username=username, key_filename=key_path)

 def send(self, c):
  if self.cli:
   self.cli.exec_command(c)


conn = RestartRemoteApp()
conn.__int__('<host_ip>', '<username>', '<key_path>')

command = '<command_shell>'
if command.find(' && '):
 commands = command.split(' && ')
 for line in commands:
  conn.send(line.strip())
else:
 conn.send(command)
