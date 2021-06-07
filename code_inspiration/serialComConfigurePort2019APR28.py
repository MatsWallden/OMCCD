"""
FUNCTION: CONFIGURES SERIAL PORT

AUTHOR MATS WALLDEN

EMAIL: mats@wallden.eu

"""

def serialComConfigurePort2019APR28(obj):
    obj.baudrate=115200
    obj.bytesize=8
    obj.parity='N'
    obj.stopbits=1
    obj.xonxoff=False
    obj.dsrdtr=False
    obj.timeout=0.05
