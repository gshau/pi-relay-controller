# =========================================================
# ModMyPi Raspberry Pi Relay Board Library
#
# by John M. Wargo (www.johnwargo.com)
# https://gpiozero.readthedocs.io/en/stable/
# =========================================================

from __future__ import print_function

from gpiozero import LED

# The number of relay ports on the relay board.
# This value should never change!
NUM_RELAY_PORTS = 4
RELAY_PORTS = ()
RELAYS = ()


def init_relay(port_list):
    global RELAY_PORTS
    print("\nInitializing relay")
    # Get the relay port list from the main application
    # assign the local variable with the value passed into init
    RELAY_PORTS = port_list
    print("Relay port list:", RELAY_PORTS)
    # populate the RELAYS list with OutputDevice objects for each relay
    for relay in enumerate(RELAY_PORTS):
        print("Assiging outputDevice for pin", relay)
        tmp_object = LED(relay)
        RELAYS.append(tmp_object)
    # return true if the number of passed ports equals the number of ports
    return len(RELAY_PORTS) == NUM_RELAY_PORTS


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
