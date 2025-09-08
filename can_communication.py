from canlib import Frame, canlib


def open_channel(channel):
    "Open a new channel, set bitrate 1Mbit/s and go bus on."
    ch = canlib.openChannel(channel, canlib.canOPEN_ACCEPT_VIRTUAL)
    ch.setBusOutputControl(canlib.canDRIVER_NORMAL)
    ch.setBusParams(canlib.canBITRATE_1M)
    ch.busOn()
    return ch


def close_channel(ch):
    "Go bus off and close channel."
    ch.busOff()
    ch.close()


def send_receive_raw(ch0, ch1, message):
    # send a CAN frame without using kvadblib
    frame = Frame(id_=4, data=bytearray(message))
    print("Sending frame: % s" % frame)
    ch0.write(frame)

    # read message back
    print("Receiving frame: % s" % str(ch1.read()))


ch0 = open_channel(1)
ch1 = open_channel(0)

message = "0x35, 0x00, 0x00, 0x00, 0x00, 0x00 0x00, 0x00"
send_receive_raw(
    ch0,
    ch1,
    message,
)

close_channel(ch0)
close_channel(ch1)
