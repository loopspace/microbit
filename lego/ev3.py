# http://ev3directcommands.blogspot.co.uk/

from serial import Serial
import struct
import sys
from datetime import datetime
from map import Map

STD = 'STD'
SYNC = 'SYNC'
ASYNC = 'ASYNC'
BLUETOOTH = 'BLUETOOTH'
WIFI = 'WIFI'
USB = 'USB'
TEST = 'TEST'

DIRECT_COMMAND_REPLY = b'\x00'
DIRECT_COMMAND_NO_REPLY = b'\x80'

# Operations
op = Map({
    'Error': b'\x00',
    'Nop': b'\x01',
    'Program': Map({
        'Stop': b'\x02',
        'Start': b'\x03',
        'Info': b'\x0C',
    }),
    'Random': b'\x8E',
    'Com': Map({
        'Ready': b'\xD0',
        'Test': b'\xD1',
        'Read': b'\x91',
        'Write': b'\x92',
        'Get': b'\xD3',
        'Set': b'\xD4',
    }),
    'File': b'\xC0',
    'UI': Map({
        'Flush': b'\x80',
        'Read': b'\x81',
        'Write': b'\x82',
        'Button': b'\x83',
        'Draw': b'\x84',
    }),
    'Timer': Map({
        'Wait': b'\x85',
        'Ready': b'\x86',
        'Read': b'\x87'
    }),
    'Sound': Map({
        'Play': b'\x94',
        'Busy': b'\x95',
        'Ready': b'\x96'
    }),
    'Input': Map({
        'Device': b'\x99',
        'Read': b'\x9A',
        'Test': b'\x9B',
        'Ready': b'\x9C',
        'ReadSI': b'\x9D',
        'ReadExt': b'\x9E',
        'Write': b'\x9F'
    }),
    'Output': Map({
        'Set_Type': b'\xA1',
        'Reset': b'\xA2',
        'Stop': b'\xA3',
        'Power': b'\xA4',
        'Speed': b'\xA5',
        'Start': b'\xA6',
        'Polarity': b'\xA7',
        'Read': b'\xA8',
        'Test': b'\xA9',
        'Ready': b'\xAA',
        'Step': Map({
            'Power': b'\xAC',
            'Speed': b'\xAE',
            'Sync': b'\xB0'
        }),
        'Time': Map({
            'Power': b'\xAD',
            'Speed': b'\xAF',
            'Sync': b'\xB1',
        }),
        'Count': Map({
            'Clear': b'\xB2',
            'Get': b'\xB3',
        }),
        'Prg_Stop': b'\xB4'
    })
})

# Commands
cmds = Map({
    'get': Map({
        'ON_OFF': b'\x01',
        'VISIBLE': b'\x02',
        'RESULT': b'\x04',
        'PIN': b'\x05',
        'ID': b'\x0C',
        'BRICKNAME': b'\x0D',
        'NETWORK': b'\x0E',
        'PRESENT': b'\x0F',
        'ENCRYPT': b'\x10',
        'INCOMMING': b'\x11',
        'FORMAT': b'\x02',
        'TYPEMODE': b'\x05',
        'SYMBOL': b'\x06',
        'RAW': b'\x08',
        'CONNECTION': b'\x0C',
        'NAME': b'\x15',
        'MODENAME': b'\x16',
        'FIGURES': b'\x18',
        'CHANGES': b'\x19',
        'MINMAX': b'\x1E',
        'BUMPS': b'\x1F'
    }),
    'set': Map({
        'ON_OFF': b'\x01',
        'VISIBLE': b'\x02',
        'SEARCH': b'\x03',
        'PIN': b'\x05',
        'PASSKEY': b'\x06',
        'CONNECTION': b'\x07',
        'BRICKNAME': b'\x08',
        'MOVEUP': b'\x09',
        'MOVEDOWN': b'\x0A',
        'ENCRYPT': b'\x0B',
        'SSID': b'\x0C'
    }),
    'search': Map({
        'ITEMS': b'\x08',
        'ITEM': b'\x09',
    }),
    'favour': Map({
        'ITEMS': b'\x0A',
        'ITEM': b'\x0B'
    }),
    'cal': Map({
        'MINMAX': b'\x03',
        'DEFAULT': b'\x04',
        'MIN': b'\x07',
        'MAX': b'\x08',
    }),
    'clr': Map({
        'ALL': b'\x0A',
        'CHANGES': b'\x1A'
    }),
    'Stop': Map({
        'ALL': b'\x0D'
    }),
    'SETUP': b'\x09',
    'Ready': Map({
        'PCT': b'\x1B',
        'RAW': b'\x1C',
        'SI': b'\x1D'
    })
})

# Sound
sound = Map({
    'BREAK': b'\x00',
    'TONE': b'\x01',
    'PLAY': b'\x02',
    'REPEAT': b'\x03',
})

# UI_Write
ui = Map({
    'LED': b'\x1B',
    'UPDATE': b'\x00',
    'TOPLINE': b'\x12',
    'FILLWINDOW': b'\x13',
    'BMPFILE': b'\x1C',
    'LINE': b'\x03',
})

#UI_Draw
draw = Map({
    'UPDATE': b'\x00',
    'PIXEL': b'\x02',
    'LINE': b'\x03',
    'CIRCLE': b'\x04',
    'TEXT': b'\x05',
    'ICON': b'\x06',
    'PICTURE': b'\x07',
    'VALUE': b'\x08',
    'FILLRECT': b'\x09',
    'RECT': b'\x0A',
    'NOTIFICATION': b'\x0B',
    'QUESTION': b'\x0C',
    'KEYBOARD': b'\x0D',
    'BROWSE': b'\x0E',
    'VERTBAR': b'\x0F',
    'INVERSERECT': b'\x10',
    'SELECT_FRONT': b'\x11',
    'TOPLINE': b'\x12',
    'FILLWINDOW': b'\x13',
    'DOTLINE': b'\x15',
    'VIEW_VALUE': b'\x16',
    'VIEW_UNIT': b'\x17',
    'FILLCIRCLE': b'\x18',
    'STORE': b'\x19',
    'RESTORE': b'\x1A',
    'ICON_QUESTION': b'\x1B',
    'BMPFILE': b'\x1C',
    'GRAPH_SETUP': b'\x1E',
    'GRAPH_DRAW': b'\x1F',
    'TEXTBOX': b'\x20',
})

# LED Colours
led = Map({
    'OFF': b'\x00',
    'GREEN': Map({
        'ON': b'\x01',
        'FLASH': b'\x04',
        'PULSE': b'\x07'
    }),
    'RED': Map({
        'ON': b'\x02',
        'FLASH': b'\x05',
        'PULSE': b'\x08'
    }),
    'ORANGE': Map({
        'ON': b'\x03',
        'FLASH': b'\x06',
        'PULSE': b'\x09'
    })
})

# File
LOAD_IMAGE = b'\x08'

# Buttons
actions = Map({
    'SHORTPRESS': b'\x01',
    'LONGPRESS': b'\x02',
    'WAIT_FOR_PRESS': b'\x03',
    'FLUSH': b'\x04',
    'PRESS': b'\x05',
    'RELEASE': b'\x06',
    'GET_HORIZ': b'\x07',
    'GET_VERT': b'\x08',
    'PRESSED': b'\x09',
    'SET_BACK_BLOCK': b'\x0A',
    'GET_BACK_BLOCK': b'\x0B',
    'TESTSHORTPRESS': b'\x0C',
    'TESTLONGPRESS': b'\x0D',
    'GET_BUMPED': b'\x0E',
    'GET_CLICK': b'\x0F'
})

button = Map({
    'NO': b'\x00',
    'UP': b'\x01',
    'ENTER': b'\x02',
    'DOWN': b'\x03',
    'RIGHT': b'\x04',
    'LEFT': b'\x05',
    'BACK': b'\x06',
    'ANY': b'\x07'
})

# Motors
port = Map({
    'A': 1,
    'B': 2,
    'C': 4,
    'D': 8
})

class TestSocket():

    def __init__(self):
        self._messages = b''

    def write(self,bytes):
        msgctr = struct.unpack('<h',bytes[2:4])[0]
        msgrqd = bytes[4]
        if msgrqd == 0:
            hdr = struct.unpack('<h',bytes[5:7])[0]
            hdr %= 1024
            self._messages += b''.join([
                struct.pack('<h', hdr + 3),
                struct.pack('<h', msgctr),
                bytearray(6)
            ])
        print_hex('Received', bytes)

    def read(self,length):
        a = self._messages[0:length]
        self._messages = self._messages[length:]
        print_hex('Sending', a)
        return a

class EV3():

    __msg_ctr = -1
    
    def __init__(self, protocol: str=None, host: str=None, ev3_obj=None):
        assert ev3_obj or protocol, \
            'Either protocol or ev3_obj needs to be given'
        if ev3_obj:
            assert isinstance(ev3_obj,EV3), \
                'ev3_obj needs to be instance of EV3'
            self._protocol = ev3_obj._protocol
            self._device = ev3_obj._device
            self._socket = ev3_obj._socket
        elif protocol:
            assert protocol in [BLUETOOTH, WIFI, USB, TEST], \
                'Protocol ' + protocol + ' is not valid'
            self._protocol = None
            self._device = None
            self._socket = None
            if protocol == BLUETOOTH:
                assert host, 'Protocol ' + protocol + ' needs host-id'
                self._connect_bluetooth(host)
            elif protocol == WIFI:
                self._connect_wifi()
            elif protocol == USB:
                self._connect_usb()
            elif protocol == TEST:
                self._connect_test()
        self._verbosity = 0
        self._sync_mode = STD

    def __del__(self):
        pass

    def _connect_bluetooth(self,tty):
        try: 
            self._socket = Serial(tty, 9600, timeout=10)
        except:
            print ("Couldn't open the bluetooth tty:", sys.exc_info()[1])
            exit()

    def _connect_wifi(self):
        pass

    def _connect_usb(self):
        pass

    def _connect_test(self):
        self._socket = TestSocket()

    def send_direct_cmd(self, ops: bytes, local_mem: int=0, global_mem: int=0) -> bytes:
        EV3.__msg_ctr += 1
        if global_mem > 0 or self._sync_mode == SYNC:
            sync = DIRECT_COMMAND_REPLY
        else:
            sync = DIRECT_COMMAND_NO_REPLY

        cmd = b''.join([
            struct.pack('<h', len(ops) + 5),
            struct.pack('<h', self.__msg_ctr),
            sync,
            struct.pack('<h', local_mem*1024 + global_mem),
            ops
        ])
        self._socket.write(cmd)
        self.log('Sent', cmd)
        if (self._sync_mode == STD and global_mem > 0) or self._sync_mode == SYNC:
            return self.wait_for_reply(self.__msg_ctr)
        else:
            return self.__msg_ctr


    def wait_for_reply(self,ctr):
        replylen = struct.unpack('<h',self._socket.read(2))[0]
        reply = self._socket.read(replylen)
        self.log('Recv', reply)
        status = reply[2]
        msgctr = struct.unpack('<h',reply[0:2])[0]
        if msgctr == ctr:
            if status == 2:
                self.status = True
            else:
                self.status = False
            return reply
        else:
            return False

    def log(self, desc: str, data: bytes) -> None:
        if self._verbosity == 1:
            print_hex(desc,data)

    @property
    def sync_mode(self):
        return self._sync_mode
    @sync_mode.setter
    def sync_mode(self, value: str):
        assert isinstance(value, str), "sync_mode needs to be a string value"
        assert value in [SYNC, ASYNC, STD], "allowed sync_mode values are: ev3.SYNC, ev3.ASYNC, ev3.STD"
        self._sync_mode = value

    @property
    def verbosity(self):
        return self._verbosity
    @sync_mode.setter
    def verbosity(self, value: int):
        assert isinstance(value, int), "verbosity needs to be an integer value"
        assert value in [0,1], "allowed verbosity values are 0 and 1"
        self._verbosity = value


class TwoWheelVehicle(EV3):

    def __init__(
            self,
            protocol: str=None,
            host: str=None,
            ev3_obj: EV3=None
    ):
        super().__init__(protocol=protocol, host=host, ev3_obj=ev3_obj)
        self._polarity = 1
        self._port_left = port.D
        self._port_right = port.A

    def move(self, speed: int, turn: int) -> None:
        assert self._sync_mode != SYNC, 'no unlimited operations allowed in sync_mode SYNC'
        assert isinstance(speed, int), 'speed needs to be an integer value'
        assert -100 <= speed and speed <= 100, 'speed needs to be in the range [-100, 100]'
        assert isinstance(turn, int), 'turn needs to be an integer value'
        assert -200 <= turn and turn <= 200, 'turn needs to be in the range [-200,200]'
        if self._polarity == -1:
            speed *= -1
        if self._port_left < self._port_right:
            turn *= -1
        ops = b''.join([
            op.Output.Step.Sync,
            LCX(0),
            LCX(self._port_left + self._port_right),
            LCX(speed),
            LCX(turn),
            LCX(0),
            LCX(0),
            op.Output.Start,
            LCX(0),
            LCX(self._port_left + self._port_right)
        ])
        self.send_direct_cmd(ops)

    def stop(self, brake: bool=False) -> None:
        assert isinstance(brake,bool), 'brake needs to be a boolean value'
        if brake:
            br = 1
        else:
            br = 0
        ops = b''.join([
            op.Output.Stop,
            LCX(0),
            LCX(self._port_left + self._port_right),
            LCX(br)
        ])
        self.send_direct_cmd(ops)

    @property
    def polarity(self):
        return self._polarity
    @polarity.setter
    def polarity(self, value: int):
        assert isinstance(value, int), "polarity needs to be an integer value"
        assert value in [1,-1], "allowed polarity values are: -1 or 1"
        self._polarity = value

    @property
    def port_right(self):
        return self._port_right
    @port_right.setter
    def port_right(self, value: int):
        assert isinstance(value, int), "port needs to be an integer value"
        assert value in [port.A, port.B, port.C, port.D], "value is not an allowed port"
        self._port_right = value

    @property
    def port_left(self):
        return self._port_left
    @port_right.setter
    def port_left(self, value: int):
        assert isinstance(value, int), "port needs to be an integer value"
        assert value in [port.A, port.B, port.C, port.D], "value is not an allowed port"
        self._port_left = value

            
            
def LCS(value: str) -> bytes:
    return b''.join([
        b'\x84',
        value.encode('ascii'),
        b'\x00'
    ])

def LCX(value: int) -> bytes:
    av = abs(value)
    if value < 0:
        sgn = 1
    else:
        sgn = 0
    if abs(value) < 32:
        av += sgn*32
        return av.to_bytes(1,byteorder='little')
    elif abs(value) < 128:
        av += sgn*128
        return b'\x81' + av.to_bytes(1,byteorder='little')
    elif abs(value) < 32768:
        av += sgn*32768
        return b'\x82' + av.to_bytes(2,byteorder='little')
    elif abs(value) < 2147483678:
        av += sgn*2147483678
        return b'\x83' + av.to_bytes(4,byteorder='little')
    else:
        return LCS(chr(value))
        

def LVX(value: int) -> bytes:
    if value < 32:
        value += 64
        return av.to_bytes(1,byteorder='little')
    elif value < 256:
        return b'\xC1' + av.to_bytes(1,byteorder='little')
    elif value < 65536:
        return b'\xC2' + av.to_bytes(2,byteorder='little')
    elif value < 4294967296:
        return b'\xC3' + av.to_bytes(4,byteorder='little')
    else:
        return LCS(chr(value))
    
def GVX(value: int) -> bytes:
    if value < 32:
        value += 96
        return value.to_bytes(1,byteorder='little')
    elif value < 256:
        return b'\xE1' + value.to_bytes(1,byteorder='little')
    elif value < 65536:
        return b'\xE2' + value.to_bytes(2,byteorder='little')
    elif value < 4294967296:
        return b'\xE3' + value.to_bytes(4,byteorder='little')
    else:
        return LCS(chr(value))
    
def port_motor_input(port_output: int) -> bytes:
    if port_output == port.A:
        return LCX(16)
    elif port_output == port.B:
        return LCX(17)
    elif port_output == port.C:
        return LCX(18)
    elif port_output == port.D:
        return LCX(19)
    else:
        raise ValueError('port_output needs to be one of the port numbers')

def print_hex(desc: str, data: bytes) -> None:
    print(str(datetime.now()) + ': ' + desc + ' 0x|' + ':'.join('{:02X}'.format(byte) for byte in data) + '|')

