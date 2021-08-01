#!/usr/bin/env python
from pymodbus.client.sync import ModbusTcpClient as ModbusClient 
from pymodbus import mei_message
import time
import config


def to_str(s):
    str = ""
    for i in range(0, len(s)):
        high, low = divmod(s[i], 0x100)
        str = str + chr(high) + chr(low)
    return str

def to_U16(i):
    return i[0] & 0xffff

def to_I16(i):
    i = i[0] & 0xffff
    return (i ^ 0x8000) - 0x8000

def to_U32(i):
    return ((i[0] << 16) + i[1])  

def to_I32(i):
    i = ((i[0] << 16) + i[1]) 
    i = i & 0xffffffff
    return (i ^ 0x80000000) - 0x80000000

def to_Bit16(i):
    return i[0]

def to_Bit32(i):
    return (i[0] << 16) + i[1]


def read_holding(client, UnitID, i, nb):
    result = client.read_holding_registers(i, nb, unit=UnitID)
    ns = time.time()
    while (time.time() - ns < 1.5):
        try:
            j = result.registers[nb - 1]
            break
        except Exception as Error:
            if 'exception_code' in vars(result):
                break
            time.sleep(0.1)
            continue
    return result



ip = config.inverter_ip
PortN = config.inverter_port
num_reg = 0
nb_reg = 1
UnitID = 0
regs = [
30070,
30071,
30072,
30073,
30075,
30077,
30079,
30081,
32000,
32002,
32003,
32008,
32009, 
32010,
32016,
32017,
32018,
32019,
32064,
32066,
#32067,
#32068,
32069,
#32070,
#32071,
32072,
#32074,
#32076,
32078,
32080,
32082,
32084,
32085,
32086,
32087,
32088,
32089,
32090,
32091,
32093,
32106,
#32110,
32114,
#32156,
#32160,
#35113,
#37113,
#37115,
#37101,
#37103,
#37105,
#37107,
#37109,
#37111,
#37117,
#37118,
#37119,
#37126,
#37128,
#37130,
#37132,
#37134,
#37136,
#37121,
40000,
#40122,
40123,
40125,
40126,
40200,
40201,
#40500,
43006
]

#print("openning")
#f = open("/tmp2/sun2000 regs" + time.strftime("%m%d-%H%M%S") + ".txt", "a")
f = open("/tmp2/sun2000_min.txt", "w")
client = ModbusClient(host=ip, port=PortN, timeout=5)
time.sleep(1)
#print(time.strftime("%a, %d %b %Y %H:%M:%S"))
#f.write(time.strftime("%a, %d %b %Y %H:%M:%S"))
if client.connect():
    time.sleep(2)
    num_reg = - 1
    while ( num_reg < len(regs) - 1):
        num_reg += 1
#       time.sleep(0.1)
#       print("trying " + str(i))

#       result = client.read_holding_registers(regs[num_reg], 1, unit=UnitID)
        result = read_holding(client, UnitID, regs[num_reg], 1)
        try:
            j = result.registers[0]
#            print("reading " + str(regs[num_reg]) + " 1")
            f.write("\"Inverter\" \"sun2000.register-" + str(regs[num_reg]) + "\"") # reading and register ID (single value)
#            for item in result.registers:
#                f.write("\t" + str(item)) # Original register value
            f.write(" \"" + str(to_I16(result.registers)) + "\"") # Register value in Int16
            f.write("\n") # Newlinw

#            print(result.registers)
#            print(to_I16(result.registers))
            continue
        except:
#           result = client.read_holding_registers(regs[num_reg], 2, unit=UnitID)
            result = read_holding(client, UnitID, regs[num_reg], 2)
            try:
                j = result.registers[1]
#                print("reading " + str(regs[num_reg]) + " 2")
                f.write("\"Inverter\" \"sun2000.register-" + str(regs[num_reg]) + "\"") # reading and register ID (double value)
#                for item in result.registers:
#                    f.write("\t" + str(item)) # Original register value

#                print(result.registers)
                if (25000 > result.registers[0] > 23000):
#                    print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(to_I32(result.registers))))
                    f.write(" \"" + str(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(to_I32(result.registers)))) + "\"") # Register value in datetime
                else:
#                    print(to_I32(result.registers))
                    f.write(" \"" + str(to_I32(result.registers)) + "\"") # Register value in Int32
                f.write("\n") # Newline
                i += 1
            except:
                j = 0
            continue

#       print(toLong(result.registers))


client.close()
#print(time.strftime("%a, %d %b %Y %H:%M:%S"))
#f.write(time.strftime("%a, %d %b %Y %H:%M:%S"))
f.close()
