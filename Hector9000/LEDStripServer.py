import paho.mqtt.client as mqtt

from Hector9000.utils.LEDStripConnector import LEDStripConnector as LEDStrip

MQTT_Server = "localhost"
port = 1883
MainTopic = "Hector9000/LEDStrip/"


def debugOut(message):
    print("LED_Strip_Server:" + message)


def on_message(client, userdata, msg):
    print("message recieved")
    print("LED_Server on_message: " + str(msg.topic) + " , " + msg.payload.decode("utf-8"))
    topic = str(msg.topic)
    topic = topic.replace(MainTopic, "")
    if topic == "standart":
        args = list(map(int, msg.payload.decode("utf-8").split(",")))
        print(args[0])
        pixels.mode=args[0]
    elif topic == "dosedrink":
        args = list(map(int, msg.payload.decode("utf-8").split(",")))
        print(args[0])
        if args[0] == 0:
            pixels.mode = 15
        elif args[0] ==1:
            pixels.mode = 16
    elif topic == "servos":
        args = list(map(int, msg.payload.decode("utf-8").split(",")))
        print(args[0])
        pixels.mode = args[0]
    else:
        debugOut("Unknown topic")


def on_connect(client, userdata, flags, rc):
    print("Server connected")
    client.subscribe(MainTopic + "#")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to Topic")


print("server started")
pixels = LEDStrip()
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.connect(MQTT_Server, port, 60)
client.loop_start()

while True:
    pixels.loop()


