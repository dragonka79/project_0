from flask import Flask
import yaml

app = Flask(__name__)

def import_devices():
    with open ("quokka/data/devices.yaml") as devices_file:
        devices = yaml.safe_load(devices_file.read())
        return devices


@app.route("/devices/")
def devices():
    devices = import_devices()
    return {'devices': devices}

# from flask import Flask

# app = Flask(__name__)

# @app.route("/device/")
# def hello_world():
#     device = {
#         "name": "sbx-n9kv-ao",
#         "vendor": "cisco",
#         "model": "Nexus9000 C9300c Chassis",
#         "os": "nxos",
#         "version": "9.3(3)",
#         "ip": "10.1.1.1",

#     }
#     return device
    # return "<p>Hello, zaultschy!</p>"