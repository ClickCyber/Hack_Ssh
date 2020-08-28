import ssh_tools
while True:
    world_list = input('insert name file world list\n')
    nickName = input('insert usernmae\n')
    Host = input('insert name host\n')
    port = int(input('insert port\n'))
    obj = ssh_tools.ssh_hacker(world_list,nickName, Host,port)
    obj.guess_Login()
