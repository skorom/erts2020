import sys
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

client.connect("192.168.0.95", 1883, 60)
client.subscribe("users/"+username+"/inbox/#", 0)

#qos=Quality of Service 0,1,2
client.publish("logged_in/", username, qos=2)

client.loop_forever()

#client.disconnect()
