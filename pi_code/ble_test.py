import asyncio
from bleak import BleakScanner, BleakClient
from bleak.backends.characteristic import BleakGATTCharacteristic
import time
import sys

BATTERY_LEVEL_UUID = "00002a19-0000-1000-8000-00805f9b34fb"

class DeviceNotFoundError(Exception):
    pass

async def run_ble_client(queue: asyncio.Queue):
    print("starting scan...")

    devices = await BleakScanner.discover(timeout=5.0)
    device = None
    for d in devices:
        if d.name == "Anthony's A13":
            print(d)
            device = d

    async def callback_handler(_, data):
        await queue.put((time.time(), data))

    async with BleakClient(address_or_ble_device=device) as client:
        print("connected")
        await client.start_notify(BATTERY_LEVEL_UUID, callback_handler)
        try:
            while True:
                await asyncio.sleep(1.0)
        except KeyboardInterrupt as e:
            sys.exit(0)
        finally:
            await queue.put((time.time(), None))
            await client.disconnect()
            print("The client has disconnected.")
        #await client.stop_notify(BATTERY_LEVEL_UUID)
        # Send an "exit command to the consumer"
        

    print("disconnected")

async def run_queue_consumer(queue: asyncio.Queue):
    print("Starting queue consumer")

    while True:
        # Use await asyncio.wait_for(queue.get(), timeout=1.0) if you want a timeout for getting data.
        epoch, data = await queue.get()
        if data is None:
            print(
                "Got message from client about disconnection. Exiting consumer loop..."
            )
            break
        else:
            print("Received callback data via async queue at %s: %r", epoch, data)

async def main():
    queue = asyncio.Queue()
    client_task = run_ble_client(queue)
    consumer_task = run_queue_consumer(queue)

    try:
        await asyncio.gather(client_task, consumer_task)
    except DeviceNotFoundError:
        pass

    print("Main method done.")

asyncio.run(main())


# def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
#     print("Here")
#     print("Characteristic: {}, Value: {}".format(characteristic, list(data)))


# async def main():
#     devices = await BleakScanner.discover(timeout=5.0)
#     device = None
#     for d in devices:
#         if d.name == "Anthony's A13":
#             print(d)
#             device = d
    
#     async with BleakClient(address_or_ble_device=device) as client:
#         print("Connected")
#         battery_service = None
#         for service in client.services:
#             print(service)
#             for characteristic in service.characteristics:
#                 client.start_notify(characteristic, notification_handler)
                 
#             await asyncio.sleep(5.0)

#         # await client.start_notify(BATTERY_LEVEL_UUID, notification_handler)
#         # await asyncio.sleep(5.0)
#         #await client.stop_notify(BATTERY_LEVEL_UUID)


#         # print("Services:")
#         # for service in client.services:
#         #     print(service)
#         #     for char in service.characteristics:
#         #         if "read" in char.properties:
#         #             try:
#         #                 value = await client.read_gatt_char(char.uuid)
#         #                 print("Characteristic: {}, Value: {}, UUID: {}".format(char, list(value), char.uuid))

#         #             except Exception as e:
#         #                 print("Characteristic: {}, Error: {}".format(char, e))
#         #         else:
#         #             print("Characteristic: {}, Properties: {}".format(char, char.properties))

# asyncio.run(main())