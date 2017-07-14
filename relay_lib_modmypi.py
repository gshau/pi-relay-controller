# =========================================================
# ModMyPi Raspberry Pi Relay Board Library
#
# by John M. Wargo (www.johnwargo.com)
#
# =========================================================

from __future__ import print_function

# The number of relay ports on the relay board.
# This value should never change!
NUM_RELAY_PORTS = 4


def relay_on(relay_num):
    if isinstance(relay_num, int):
        # do we have a valid relay number?
        if 0 < relay_num <= NUM_RELAY_PORTS:
            print('Turning relay', relay_num, 'ON')
            pass

        else:
            print('Invalid relay #:', relay_num)
    else:
        print('Relay number must be an Integer value')


def relay_off(relay_num):
    if isinstance(relay_num, int):
        # do we have a valid relay number?
        if 0 < relay_num <= NUM_RELAY_PORTS:
            print('Turning relay', relay_num, 'OFF')
            pass

        else:
            print('Invalid relay #:', relay_num)
    else:
        print('Relay number must be an Integer value')


def relay_all_on():
    print('Turning all relays ON')
    pass


def relay_all_off():
    print('Turning all relays OFF')
    pass


def relay_toggle_port(relay_num):
    print('Toggling relay:', relay_num)
    if relay_get_port_status(relay_num):
        # it's on, so turn it off
        relay_off(relay_num)
    else:
        # it's off, so turn it on
        relay_on(relay_num)


def relay_get_port_status(relay_num):
    # determines whether the specified port is ON/OFF
    print('Checking status of relay', relay_num)

    if res > 0:

        # do this a different way

        return True
    else:
        # otherwise (invalid port), always return False
        print("Specified relay port is invalid")
        return False
