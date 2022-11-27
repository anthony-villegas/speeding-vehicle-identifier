import asyncio
from bleak import BleakScanner, BleakClient

BATTERY_LEVEL_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
DEVICE_NAME = "Anthony's A13"
DEVICE_ID = "50:C9:8D:93:10:69"

class DeviceNotFoundError(Exception):
    pass

async def run_ble_client(ble_input):
    print("starting scan...")

    devices = await BleakScanner.discover(timeout=5.0)
    device = None
    for d in devices:
        if d.name == "Anthony's A13":
            print(d)
            device = d

    async def callback_handler(_, data):
        print("Received data: {}".format(data))
        ble_input.schedule(0, list(data)[0])

    async with BleakClient(address_or_ble_device=device) as client:
        print("connected")
        await client.start_notify(BATTERY_LEVEL_UUID, callback_handler)
        while True:
            await asyncio.sleep(0.0)

async def main(self, ble_input):
    client_task = run_ble_client(ble_input)
    try:
        await asyncio.gather(client_task)
    except DeviceNotFoundError:
        pass

    print("Main method done.")
