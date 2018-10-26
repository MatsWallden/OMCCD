"""
FUNCTION: CONFIGURES SERIAL PORT

AUTHOR MATS WALLDEN

EMAIL: mats@wallden.eu

"""

def serialComConfigurePort2018MAY16a(obj):
    obj.baudrate=384000
    obj.bytesize=8
    obj.parity='N'
    obj.stopbits=1
    obj.xonxoff=False
    obj.dsrdtr=False
    obj.timeout=0.5
