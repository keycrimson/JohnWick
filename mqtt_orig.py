import paho.mqtt.client as mqtt
# from ast import literal_eval
import time,json
mqttc = mqtt.Client()

mqtt_broker = #broker name
mqtt_port = #port
mqtt_user = ''
mqtt_pass = ''
mqtt_sub = 'kono powa'


def on_message(client, userdata, message):
    pass
def on_publish(client,userdata,result):   #create function for callback 
    print("\nData successfully  published \n")
    pass
def on_log(client, userdata, level, buf):
    print("log: ",buf)
def on_connect(client, userdata, flags, rc):
# logging.info("MQTT Connected ")
    print("MQTT Connected ")
    mqttc.subscribe(mqtt_sub, qos=2)
def handle_modbus(client, userdata, message):
    x = message.payload
    global d
    # print(x)
    # print('____________________________________')
    try:
    # data = json.loads(x)
    x = str(x)
    data = x.split("'")
    d = data[1]
    print('-',d)
    if d == 'w':
        print('masuk w')
    else:
        print('stop')
    except Exception as e:
        print('Error json loads')
        # logging.info('Error json loads')
        # logging.info(e)
        print(e)
    return


import ssl

mqttc=mqtt.Client()
print("Connecting to broker")
mqttc.username_pw_set(mqtt_user, mqtt_pass)
mqttc.connect(mqtt_broker, mqtt_port, 60)

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish=on_publish


mqttc.message_callback_add(mqtt_sub,handle_modbus)
while True:
    try:
        #start loop to process received messages
        mqttc.loop_start()
        #wait to allow publish and logging and exit

    except Exception as e:
        pass
        #new comment line