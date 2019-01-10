"""A module for interacting with the ELEGOO 8 Channel board for the Raspberry Pi."""
# =========================================================
# Raspberry Pi Relay Board Library
#
# by John M. Wargo (www.johnwargo.com)
# https://gpiozero.readthedocs.io/en/stable/
#
# by G. Shaughnessy
# =========================================================

from __future__ import print_function

import RPi.GPIO as GPIO

# Turn off GPIO warnings
GPIO.setwarnings(False)

# Set the GPIO numbering convention to be header pin numbers
GPIO.setmode(GPIO.BOARD)

# The number of relay ports on the relay board.
# This value should never change!
NUM_RELAY_PORTS = 8
RELAY_PORTS = ()
RELAY_STATUS = NUM_RELAY_PORTS * [0]

# Some relay boards have a default on state with a low pin
ON_STATE = 0
OFF_STATE = 1 - ON_STATE



def init_relay(port_list):
    """Initialize the module

    Args:
        port_list: A list containing the relay port assignments
    """
    global RELAY_PORTS
    print("\nInitializing relay")
    # Get the relay port list from the main application
    # assign the local variable with the value passed into init
    RELAY_PORTS = port_list
    print("Relay port list:", RELAY_PORTS)
    # setup the relay ports for output
    for relay in enumerate(RELAY_PORTS):
        GPIO.setup(relay[1], GPIO.OUT)
    # return true if the number of passed ports equals the number of ports
    return len(RELAY_PORTS) == NUM_RELAY_PORTS


def relay_on(relay_num):
    """Turn the specified relay (by relay #) on.

    Call this function to turn a single relay on.

    Args:
        relay_num (int): The relay number that you want turned on.
    """
    if isinstance(relay_num, int):
        # do we have a valid relay number?
        if 0 < relay_num <= NUM_RELAY_PORTS:
            print('Turning relay', relay_num, 'ON')
            GPIO.output(RELAY_PORTS[relay_num - 1], ON_STATE)
            # set the status for this relay to 'on'
            RELAY_STATUS[relay_num - 1] = ON_STATE
        else:
            print('Invalid relay #:', relay_num)
    else:
        print('Relay number must be an Integer value')


def relay_off(relay_num):
    """Turn the specified relay (by relay #) off.

    Call this function to turn a single relay off.

    Args:
        relay_num (int): The relay number that you want turned off.
    """
    if isinstance(relay_num, int):
        # do we have a valid relay number?
        if 0 < relay_num <= NUM_RELAY_PORTS:
            print('Turning relay', relay_num, 'OFF')
            GPIO.output(RELAY_PORTS[relay_num - 1], OFF_STATE)
            # set the status for this relay to 'off'
            RELAY_STATUS[relay_num - 1] = OFF_STATE
        else:
            print('Invalid relay #:', relay_num)
    else:
        print('Relay number must be an Integer value')


def relay_all_on():
    """Turn all of the relays on.

     Call this function to turn all of the relays on.
     """
    print('Turning all relays ON')
    for relay in enumerate(RELAY_PORTS):
        # turn the relay on
        GPIO.output(relay[1], ON_STATE)
        # set the status for this relay to 'on'
        RELAY_STATUS[relay[0]] = ON_STATE
        # yes, I know I probably could have done the following:
        # for i, relay in enumerate(RELAY_PORTS):
        #     # turn the relay on
        #     GPIO.output(relay, 1)
        #     # set the status for this relay to 'on'
        #     RELAY_STATUS[i] = 1


def relay_all_off():
    """Turn all of the relays on.

    Call this function to turn all of the relays on.
    """
    print('Turning all relays OFF')
    for relay in enumerate(RELAY_PORTS):
        # turn the relay off
        GPIO.output(relay[1], OFF_STATE)
        # set the status for this relay to 'off'
        RELAY_STATUS[relay[0]] = OFF_STATE


def relay_toggle_port(relay_num):
    """Toggle the specified relay (on to off, or off to on).

    Call this function to toggle the status of a specific relay.

    Args:
        relay_num (int): The relay number to toggle.
    """
    print('Toggling relay:', relay_num)
    if relay_get_port_status(relay_num):
        # it's on, so turn it off
        relay_off(relay_num)
    else:
        # it's off, so turn it on
        relay_on(relay_num)


def relay_get_port_status(relay_num):
    """Returns the status of the specified relay (True for on, False for off)

    Call this function to retrieve the status of a specific relay.

    Args:
        relay_num (int): The relay number to query.
    """
    # determines whether the specified port is ON/OFF
    print('Checking status of relay', relay_num)
    return RELAY_STATUS[relay_num - 1] == ON_STATE
