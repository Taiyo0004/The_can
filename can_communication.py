from canlib import Frame, canlib


def open_channel(channel):
    ch = canlib.openChannel(channel, canlib.canOPEN_ACCEPT_VIRTUAL)
    ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
    ch.setBusParams(canlib.canBITRATE_500K)
    ch.busOn()
    return ch


# Open two channels
ch_send = open_channel(channel=0)

# Setup both channels
ch_send.setBusOutputControl(canlib.canDRIVER_NORMAL)
ch_send.busOn()
while True:
    command_int = input("Enter the command: ")
    command = int(command_int, 0)
    command_array = [command, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    # Send on one channel
    frame = Frame(id_=4, data=bytearray(command_array))
    ch_send.write(frame)
