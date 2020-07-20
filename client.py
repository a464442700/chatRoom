import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
toAddr=("192.168.50.61",40000)
print("-------输入quit结束聊天-------")
name=input("请输入昵称：")
if name=="":
    name=socket.gethostname()
while True:
    send_data=input("：")
    if send_data=="quit":
        client.sendto((name+":"+send_data).encode(),toAddr)
        break
    else:
        client.sendto((name + ":" + send_data).encode(), toAddr)
    client_data,address=client.recvfrom(1024)
    print(client_data.decode("utf-8"))
client.close()

