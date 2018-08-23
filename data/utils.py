import paho.mqtt.client as mqtt
import requests
import json
connected = False

def on_connect(client, userdata, flags, rc):
    global connected
    print("Connected with result code "+str(rc))
    connected = True
    client.subscribe("auck/*tempandpress*")
    print('connnected')

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.payload)
    try:
        p = json.loads(msg.payload.decode())
        q = requests.post(' http://127.0.0.1:8000/',p)
        print(q.content)
    except:
        pass


client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
print('connnecting...')
client.connect("iot.eclipse.org", 1883, 60)
#while not connected:
#    pass
client.loop_start()
