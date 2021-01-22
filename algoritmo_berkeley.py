def convertmin(num): 
  return (int(num.split(':')[0]) * 60) + int(num.split(':')[1])

def atraso(base ,num):
  return num - base

def clock(num, num1, num2, base):
  hr = (((num + num1 + num2) / 3) + base) // 60
  mn = (((num + num1 + num2) / 3) + base) % 60
  if mn >= 10:
    return str(hr).split('.')[0] + ':' + str(mn).split('.')[0]
  else:
    return str(hr).split('.')[0] + ':0' + str(mn).split('.')[0]


daemon = input("Hora do daemon: ")
server = input("Hora do server: ")
net1 = input("Hora do dispositivo: ")
net2 = input("Hora do dispositivo: ")

daemon_min = convertmin(daemon)
server_min = convertmin(server)
net1_min = convertmin(net1)
net2_min = convertmin(net2)

server_atraso = atraso(daemon_min, server_min)
net1_atraso = atraso(daemon_min, net1_min)
net2_atraso = atraso(daemon_min, net2_min)

print(clock(server_atraso, net1_atraso, net2_atraso, daemon_min))
