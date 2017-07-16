# Raspberry Pi Relay Controller: ModMyPi Version

from __future__ import print_function

import sys

from flask import Flask
from flask import make_response
from flask import render_template
from flask_bootstrap import Bootstrap

from relay_lib_modmypi import *

error_msg = '{msg:"error"}'
success_msg = '{msg:"success"}'

# Update the following list/tuple with the port numbers assigned to your relay board
PORTS = (7, 8, 10, 11)
NUM_RELAY_PORTS = 4

# initialize the relay library with the system's port configuration
if init_relay(PORTS):
    # turn all of the relays off, so we're starting with a clean slate.
    relay_all_off()
else:
    print("Port configuration error")
    # exit the application
    sys.exit(0)

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    print("Loading app Main page")
    # return success_resp
    return render_template('index.html')


@app.route('/status/<int:relay>')
def api_get_status(relay):
    res = relay_get_port_status(relay)
    if res:
        print("Relay is ON")
        return make_response("1", 200)
    else:
        print("Relay is OFF")
        return make_response("0", 200)


@app.route('/toggle/<int:relay>')
def api_toggle_relay(relay):
    print("Executing api_relay_toggle:", relay)
    relay_toggle_port(relay)
    return make_response(success_msg, 200)


@app.route('/on/<int:relay>')
def api_relay_on(relay):
    print("Executing api_relay_on:", relay)
    if validate_relay(relay):
        print("valid relay")
        relay_on(relay)
        return make_response(success_msg, 200)
    else:
        print("invalid relay")
        return make_response(error_msg, 404)


@app.route('/off/<int:relay>')
def api_relay_off(relay):
    print("Executing api_relay_off:", relay)
    if validate_relay(relay):
        print("valid relay")
        relay_off(relay)
        return make_response(success_msg, 200)
    else:
        print("invalid relay")
        return make_response(error_msg, 404)


@app.route('/all_on/')
def api_relay_all_on():
    print("Executing api_relay_all_on")
    relay_all_on()
    return make_response(success_msg, 200)


@app.route('/all_off/')
def api_all_relay_off():
    print("Executing api_relay_all_off")
    relay_all_off()
    return make_response(success_msg, 200)


@app.errorhandler(404)
def page_not_found(e):
    print("ERROR: 404")
    return render_template('404.html', the_error=e), 404


@app.errorhandler(500)
def internal_server_error(e):
    print("ERROR: 500")
    return render_template('500.html', the_error=e), 500


def validate_relay(relay):
    # Make sure the port falls between 1 and NUM_RELAY_PORTS
    return (relay > 0) and (relay <= NUM_RELAY_PORTS)


if __name__ == "__main__":
    # On the Pi, you need to run the app using this command to make sure it
    # listens for requests outside of the device.
    # app.run(host='0.0.0.0')
    app.run(host='0.0.0.0', port=5000, debug=True)
