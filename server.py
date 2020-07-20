import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("",40000))
# name=input("输入昵称：")
print("等待连接中。。。")
addrList=[]
while True:
    data,address=server.recvfrom(2048)
    if address not in addrList:
        addrList.append(address)
    receive_info = str(address) + ":" + data.decode("utf-8")
    for addr in addrList:
        #print(receive_info)
        receive_msg=data.decode("utf-8")
        server.sendto(receive_msg.encode("utf-8"), addr)
    print(addrList)
    # if send_msg=="quit":
    #     send_msg="已下线"
    #     server.sendto(send_msg.encode("utf-8"),address)
    #     break
    # else:
    #     server.sendto(send_msg.encode("utf-8"), address)
server.close()