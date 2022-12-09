import asyncio
from bleak import BleakScanner, BleakClient

BATTERY_LEVEL_UUID = "00002a19-0000-1000-8000-00805f9b34fb"
DEVICE_NAME = "Anthony's A13"

class DeviceNotFoundError(Exception):
    pass

async def run_ble_client(ble_input):
    print("starting scan...")
    devices = await BleakScanner.discover(timeout=5.0)
    device = None
    for d in devices:
        if d.name == "Anthony's A13":
            device = d

    async def callback_handler(_, data):
        ble_input.schedule(0, list(data)[0])

    async with BleakClient(address_or_ble_device=device) as client:
        print("Connected to {}".format(device))
        await client.start_notify(BATTERY_LEVEL_UUID, callback_handler) #setup callback handler
        while True:
            await asyncio.sleep(0.01)

def main(self, ble_input):
    asyncio.run(start_background_loop(ble_input))

async def start_background_loop(ble_input):
    client_task = run_ble_client(ble_input)
    try:
        await asyncio.gather(client_task)
    except DeviceNotFoundError:
        pass