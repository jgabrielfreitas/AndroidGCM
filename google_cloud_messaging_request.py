import http.client
import json
# Samsung device token:
# dE36xWRTwWE:APA91bELwq4DjOPWpxiz2Ig93zIdQTLe30RImvt47V3z6eolJyMiTFGuOR1VjXcu_
# CWxT6oTaQXmrHsmL08QZbGqjgh5h25St7A4u6OvKEp8A9TtOrwByPxve1-Pzv-P3QWNzLzFWBdL

# ==============================
def main():
    devices_in_parse = get_all_devices()
    option = input("Digite:\n1. Para listar os dispositivos na base\n2. Para enviar mensagem\n\nInput: ")

    option = int(option)

    if option == 1:
        # show all devices
        print ("====================================")
        for item in devices_in_parse:
            print (item['name'])
        print ("====================================")
        main()
    elif option == 2:
        message = input("Mensagem para enviar: ")

        notification_type = input("A notificacao sera enviada para todos os dispositivos? [S/N]")

        if notification_type.upper() == "S":
            send_message(message)
        else:
            device_position = 0;
            for device in devices_in_parse:
                print("{0}. {1}".format(device_position, device['name']))
                device_position = device_position + 1

            position_at_list = int(input("Qual item? (numero do dispositivo)\n"))

            position = 0
            for device in devices_in_parse:
                if position == position_at_list:
                    send_message(message, device['token'])
                    break
                else:
                    position = position + 1

        main()

    else:
        print(">>> fim")

# ==============================
def send_message(message, token_device="/topics/global"):

    root = {}
    data = {}
    data['message'] = message
    root['data'] = data
    root['to'] = token_device
    json_data = json.dumps(root)

    conn = http.client.HTTPSConnection("android.googleapis.com")

    payload = "{\n    \"data\":{\n        \"message\":\"Hello world\"\n        \n    },\n    \"to\":\"/topics/global\"\n    \n}\n"

    headers = {
        'authorization': "key=AIzaSyBslNn4JhlD6NBHtgpsWjLn4Kd-saX0yt0",
        'content-type': "application/json",
        }

    conn.request("POST", "/gcm/send", json_data, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

# ==============================
def get_all_devices():
    print("Carregando dispositivos....")
    conn = http.client.HTTPSConnection("api.parse.com")

    headers = {
        'x-parse-application-id': "m5iHVUqFIP2B34D1zcpYbDpD2eLTlrrzgWrFVfqc",
        'x-parse-rest-api-key': "Li6SQ0tQTtAmwJbv1Zxi72f8S2Td4EegGQSqWGRD",
        'content-type': "application/json"
        }

    conn.request("GET", "/1/classes/Device", headers=headers)

    res = conn.getresponse()
    data = res.read()

    results = json.loads(data.decode("utf-8"))
    return results['results']

#  Init
main()
