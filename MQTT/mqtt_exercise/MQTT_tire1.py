import time, sys
import random
import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, rc):
    print("Connected.")


def on_message(mqttc, obj, msg):
    topic = msg.topic.split("/")
    if topic[2]=="inbox":
        sender = topic[3]
        message = msg.payload.decode("utf-8")
        print("Message recieved from: " + sender + ", with the data: " + message)
    else:
        print(topic[2])


if len(sys.argv)!=2:
    print("Usage: "+sys.argv[0]+" <username>")
    quit()


username = sys.argv[1]
print("MQTT Python tester program with a user: "+"("+username+")")

client = mqtt.Client()
#client.username_pw_set(username, "asdf") # Not working
client.on_message = on_message
client.on_connect = on_connect

client.connect("localhost", 1884, 60)
client.loop_start()

#qos=Quality of Service 0,1,2
client.publish("logged_in/", username + "connected", qos=2)

while True:
    try:
        psi=random.randrange(30, 35)
        client.publish("cars/car1/tires/pressure/"+username,str(psi), qos=2)
        print("Pressure is " + str(psi))
        time.sleep(10)
    except KeyboardInterrupt:
        print ("Disconnected")
        client.publish("logged_in/", username + "disconnected", qos=2)
        client.loop_stop()
        client.disconnect()
        sys.exit(0)

