import time
import requests
import math
import random
import hy_srf05

TOKEN = "BBFF-j2wMJEN77lfyLykaiDaAP57tIN6wtt"  # Put your TOKEN here
DEVICE_LABEL = "varici_week_10"  # Put your device label here 
VARIABLE_LABEL_1 = "keadaan_ruang"  # Put your first variable label here
VARIABLE_LABEL_2 = "hitung_telur"  # Put your second variable label here

jmlh = 0
while True:
    dist = hy_srf05.ambil()
    
    def build_payload(variable_1, variable_2):
        # Creates two random values for sending data
        value_1 = random.randint(-10, 50)
        value_2 = jmlh
     
        # Creates a data
        
        payload = {variable_1: value_1,
                   variable_2: value_2,
                   }

        return payload


    def post_request(payload):
        # Creates the headers for the HTTP requests
        url = "http://industrial.api.ubidots.com"
        url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

        # Makes the HTTP requests
        status = 400
        attempts = 0
        while status >= 400 and attempts <= 5:
            req = requests.post(url=url, headers=headers, json=payload)
            status = req.status_code
            attempts += 1
            time.sleep(1)

        # Processes results
        print(req.status_code, req.json())
        if status >= 400:
            print("[ERROR] Could not send data after 5 attempts, please check \
                your token credentials and internet connection")
            return False

        print("[INFO] request made properly, your device is updated")
        return True


    def main():
        payload = build_payload(
            VARIABLE_LABEL_1, VARIABLE_LABEL_2)

        print("[INFO] Attemping to send data")
        post_request(payload)
        print("[INFO] finished")


    if __name__ == '__main__':
        while (True):
            main()
            if dist < 5 :
                jmlh += 1
                print(jmlh)
            time.sleep(1)
