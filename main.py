import sys
from PySide2 import *
from PySide2.QtCore import QUrl, QStringListModel, QObject,Signal, Property,Slot, Qt
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
import threading
import random
import requests
import json
import time
import uuid
import paho.mqtt.client as mqtt

# Global Variables Declaration starts here
model_cost_per_unit = QStringListModel()
model_slot1 = QStringListModel()
model_slot2 = QStringListModel()
model_slot3 = QStringListModel()
model_slot4 = QStringListModel()
model_slot5 = QStringListModel()
model_slot6 = QStringListModel()
model_slot7 = QStringListModel()
model_slot8 = QStringListModel()
model_late_fees=QStringListModel()
model_final_payment = QStringListModel()
model_slot_energy = QStringListModel()
model_soc_summary = QStringListModel()
model_voltage_summary = QStringListModel()
model_temp_summary = QStringListModel()
model_imbalance_summary = QStringListModel()
model_soh_summary = QStringListModel()
model_v_cell_summary = QStringListModel()
model_v_cell_avg_summary = QStringListModel()
model_charging_max = QStringListModel()
model_discharging_min = QStringListModel()
model_module_tem_sensor_summary = QStringListModel()
model_cell1_temp_sensor = QStringListModel()
model_cell2_temp_sensor = QStringListModel()
model_cell3_temp_sensor = QStringListModel()
model_cell4_temp_sensor = QStringListModel()
model_cell5_temp_sensor = QStringListModel()
model_cell6_temp_sensor = QStringListModel()
model_cell7_temp_sensor = QStringListModel()
model_cell8_temp_sensor = QStringListModel()
model_selected_slot = QStringListModel()
model_retension_cost = QStringListModel()
model_time_taken_to_charge = QStringListModel()
model_booked_slot_soc = QStringListModel()
model_estimated_payment = QStringListModel()
model_slot1_status = QStringListModel()
model_slot2_status = QStringListModel()
model_slot3_status = QStringListModel()
model_slot4_status = QStringListModel()
model_slot5_status = QStringListModel()
model_slot6_status = QStringListModel()
model_slot7_status = QStringListModel()
model_slot8_status = QStringListModel()
model_customer_name = QStringListModel()
model_taxes = QStringListModel()

# Model declaration for BSU details
model_bsu_id            = QStringListModel()
model_bsu_mode          = QStringListModel()
model_bsu_state         = QStringListModel()
model_bsu_man_name      = QStringListModel()
model_order_status      = QStringListModel()
model_inservice_hrs     = QStringListModel()
model_batterypack_id    = QStringListModel()

# global variable for BSU Details
bsu_id,slot_no,bsu_state,bsu_mode,order_status,inservice_hrs,battery_pack_id,bsu_man_name,station_id=0,0,0,0,0,0,0,0,0
#declaration end

#Global variable for order payload
order_id,charging_id,pyment_id,customer_id,payment_status = "","","","",""
#declaration end

# global variable declaration for station telemetry
station_messageID,stationID,station_accountID,station_mode,station_voltage,station_current,station_temp="","","","",0,0,0
#declaration end

# global variable for slot telemetry
soh1,slot1_message_id,station_id,slot1_id,bsu1_id,customer1_id,slot1_status,slot1_soh,slot1_current,slot1_voltage=0,"","","","","","",0,0,0
soh2,slot2_message_id,slot2_id,bsu2_id,customer2_id,slot2_status,slot2_soh,slot2_current,slot2_voltage=0,"","","","","",0,0,0
soh3,slot3_message_id,slot3_id,bsu3_id,customer3_id,slot3_status,slot3_soh,slot3_current,slot3_voltage=0,"","","","","",0,0,0
soh4,slot4_message_id,slot4_id,bsu4_id,customer4_id,slot4_status,slot4_soh,slot4_current,slot4_voltage=0,"","","","","",0,0,0
soh5,slot5_message_id,slot5_id,bsu5_id,customer5_id,slot5_status,slot5_soh,slot5_current,slot5_voltage=0,"","","","","",0,0,0
soh6,slot6_message_id,slot6_id,bsu6_id,customer6_id,slot6_status,slot6_soh,slot6_current,slot6_voltage=0,"","","","","",0,0,0
soh7,slot7_message_id,slot7_id,bsu7_id,customer7_id,slot7_status,slot7_soh,slot7_current,slot7_voltage=0,"","","","","",0,0,0
soh8,slot8_message_id,slot8_id,bsu8_id,customer8_id,slot8_status,slot8_soh,slot8_current,slot8_voltage=0,"","","","","",0,0,0
#declaration End

# models for battery pack specs
model_battery_man_name  = QStringListModel()
model_battery_capacity  = QStringListModel()
model_battery_chemistry = QStringListModel()
model_battery_config    = QStringListModel()
model_battery_cells     = QStringListModel()
model_battery_model     = QStringListModel()

# global variable for Battery Details
battery_man_name,battery_capacity,battery_chemistry,battery_config,battery_cell,battery_model=0,0,0,0,0,0
query_bsu_id=0
cost_per_unit,energy_slot,late_fees,final_payment,retension_cost,time_taken_to_charge,est_payment = 0,0,0,0,0,0,0
soc1,soc2,soc3,soc4,soc5,soc6,soc7,soc8,booked_slot_soc = 0,0,0,0,0,0,0,0,0
v1,v2,v3,v4,v5,v6,v7,v8 = 0,0,0,0,0,0,0,0
c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp = 0,0,0,0,0,0,0,0
min_temp,max_temp,imbalance,soh,v_cell_min,v_cell_max,calcute_taxes = 0,0,0,0,0,0,0
v_cell_avg, charging_max, discharging_min, slot_number,booked_slot_flag = 0,0,0,0,False
thread_1_flag, thread_2_flag, thread_3_flag, thread_4_flag,thread_5_flag, thread_6_flag, thread_7_flag, thread_8_flag = False, False, False, False, False, False, False, False
main_th,slot_1_th,slot_2_th,slot_3_th,slot_4_th,slot_5_th,slot_6_th,slot_7_th,slot_8_th = 0,0,0,0,0,0,0,0,0
payload = []
pack_temp = []
slot_status = {}
get_cust_id = 0
slot1_status_flag,slot2_status_flag,slot3_status_flag,slot4_status_flag,slot5_status_flag,slot6_status_flag,slot7_status_flag,slot8_status_flag,slot_status_string = 0,0,0,0,0,0,0,0,""
SLOT1_STATUS,SLOT2_STATUS,SLOT3_STATUS,SLOT4_STATUS,SLOT5_STATUS,SLOT6_STATUS,SLOT7_STATUS,SLOT8_STATUS = "","","","","","","",""
slot1_status,slot2_status="Charging","Charging"
payment_gateway,payment_id,payment_method,payment_done = "","","",0
# Global Variables Declaration ends  here

#MQTT publisher client creation
pub_client_name = "mqtt-client"
pub_client = mqtt.Client(pub_client_name)
# Global Variables Declaration ends  here

"""
Function Name: on_message
Input Args   : Null
Return       : Null
Description  : This APi will fetch slot status data using mqtt subscribe.
"""
def on_message(client, userdata, message):
    global slot_status,SLOT1_STATUS,SLOT2_STATUS,SLOT3_STATUS,SLOT4_STATUS,SLOT5_STATUS,SLOT6_STATUS,SLOT7_STATUS,SLOT8_STATUS
    slot_status = json.loads(message.payload.decode("utf-8"))
    SLOT1_STATUS = slot_status['slot1']
    SLOT1_STATUS = SLOT1_STATUS.capitalize()
    SLOT2_STATUS = slot_status['slot2']
    SLOT2_STATUS = SLOT2_STATUS.capitalize()
    SLOT3_STATUS = slot_status['slot3']
    SLOT3_STATUS = SLOT3_STATUS.capitalize()
    SLOT4_STATUS = slot_status['slot4']
    SLOT4_STATUS = SLOT4_STATUS.capitalize()
    SLOT5_STATUS = slot_status['slot5']
    SLOT5_STATUS = SLOT5_STATUS.capitalize()
    SLOT6_STATUS = slot_status['slot6']
    SLOT6_STATUS = SLOT6_STATUS.capitalize()
    SLOT7_STATUS = slot_status['slot7']
    SLOT7_STATUS = SLOT7_STATUS.capitalize()
    SLOT8_STATUS = slot_status['slot8']
    SLOT8_STATUS = SLOT8_STATUS.capitalize()

# Global variable for slot status using mqtt subscribe:
sub_client = mqtt.Client("QT_App_MQTT_Client")
sub_client.on_message=on_message
sub_client.connect("localhost", 9001)
sub_client.subscribe("bsuStation/slotStatus")


def generate_data_for_order():
    global order_id,payment_id,charging_id,slot_no,customer_id,payment_status
    order_id = str(uuid.uuid1())
    payment_id = str(uuid.uuid1())
    charging_id = str(uuid.uuid1())
    if slot_no == 1:
        customer_id = customer1_id
    elif slot_no == 2:
        customer_id = customer2_id
    elif slot_no == 3:
        customer_id = customer3_id
    elif slot_no == 4:
        customer_id = customer4_id
    elif slot_no == 5:
        customer_id = customer5_id
    elif slot_no == 6:
        customer_id = customer6_id
    elif slot_no == 7:
        customer_id = customer7_id
    elif slot_no == 8:
        customer_id = customer8_id


"""
Function Name: station_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for station telemetry and publish it
               to the cloud via mqtt broker.
"""
def station_telemetry_data():
    global station_messageID,stationID,station_accountID,station_mode,station_voltage,station_current,station_temp
    timestamp = time.time()
    topic="fromStation/{}/stationTelemetry".format(stationID)
    station_payload={
        "message_id": "KLT33224YC33",
        "station_id": stationID,
        "station_mode": "Charging",
        "voltage": station_voltage,
        "voltage_unit": 'KW',
        "current": station_current,
        "current_unit": 'Ampere',
        "temp": station_temp,
        "temp_unit": 'Celcius',
        "timestamp":timestamp,
    }
    pub_client.publish(topic, json.dumps(station_payload))

"""
Function Name: slot1_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot1 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot1_telemetry_data():
    global soc1,soh1,SLOT1_STATUS,get_cust_id,v1,slot_mode,slot1_temp
    global slot1_message_id,station_id,slot1_id,bsu1_id,customer1_id,slot1_status,slot1_soh,slot1_current,slot1_voltage
    topic="fromSlot/{}/slotTelemetry".format(slot1_id)
    timestamp = time.time()
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot1_payload={
        "message_id": slot1_message_id,
        "station_id": station_id,
        "slot_id": slot1_id,
        "bsu_id": bsu1_id,
        "customer_id": customer1_id,
        "current": slot1_current,
        "voltage": v1,
        "temp": 25,
        "slot_soc": soc1,
        "slot_soh": soh1,
        "slot_status": "In-Use",
        "slot_mode": SLOT1_STATUS,
        "timestamp" : timestamp
    }
    pub_client.publish(topic, json.dumps(slot1_payload))

"""
Function Name: slot2_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot2 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot2_telemetry_data():
    global soc2,soh2,SLOT2_STATUS,get_cust_id,v2,slot_mode,slot1_temp
    global slot2_message_id,station_id,slot2_id,bsu2_id,customer2_id,slot2_current
    timestamp = time.time()
    topic="fromSlot/{}/slotTelemetry".format(slot2_id)
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot2_payload={
        "message_id": slot2_message_id,
        "station_id": station_id,
        "slot_id": slot2_id,
        "bsu_id": bsu2_id,
        "customer_id": customer2_id,
        "current": slot2_current,
        "voltage": v2,
        "temp": 25,
        "slot_soc": soc2,
        "slot_soh": soh2,
        "slot_status": "In-Use",
        "slot_mode": SLOT2_STATUS,
        "timestamp": timestamp
    }
    pub_client.publish(topic, json.dumps(slot2_payload))

"""
Function Name: slot3_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot3 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot3_telemetry_data():
    global soc3,soh3,SLOT3_STATUS,get_cust_id,v3,slot_mode,slot3_temp
    global slot3_message_id,station_id,slot3_id,bsu3_id,customer3_id,slot3_current
    timestamp = time.time()
    topic="fromSlot/{}/slotTelemetry".format(slot3_id)
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot3_payload={
        "message_id": slot3_message_id,
        "station_id": station_id,
        "slot_id": slot3_id,
        "bsu_id": bsu3_id,
        "customer_id": customer3_id,
        "current": slot3_current,
        "voltage": v3,
        "temp": 25,
        "slot_soc": soc3,
        "slot_soh": soh3,
        "slot_status": "In-Use",
        "slot_mode": SLOT3_STATUS,
        "timestamp":timestamp
    }
    pub_client.publish(topic, json.dumps(slot3_payload))

"""
Function Name: slot4_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot4 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot4_telemetry_data():
    global soc4,soh4,SLOT4_STATUS,get_cust_id,v4,slot_mode,slot4_temp
    global slot4_message_id,station_id,slot4_id,bsu4_id,customer4_id,slot4_current
    timestamp = time.time()
    topic="fromSlot/{}/slotTelemetry".format(slot4_id)
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot4_payload={
        "message_id": slot4_message_id,
        "station_id": station_id,
        "slot_id": slot4_id,
        "bsu_id": bsu4_id,
        "customer_id": customer4_id,
        "current": slot4_current,
        "voltage": v4,
        "temp": 25,
        "slot_soc": soc4,
        "slot_soh": soh4,
        "slot_status": "In-Use",
        "slot_mode": SLOT4_STATUS,
        "timestamp":timestamp
    }
    pub_client.publish(topic, json.dumps(slot4_payload))

"""
Function Name: slot5_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot5 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot5_telemetry_data():
    global soc5,soh5,SLOT5_STATUS,get_cust_id,v5,slot_mode,slot5_temp
    global slot5_message_id,station_id,slot5_id,bsu5_id,customer5_id,slot5_current
    timestamp = time.time()
    topic="fromSlot/{}/slotTelemetry".format(slot5_id)
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot5_payload={
        "message_id": slot5_message_id,
        "station_id": station_id,
        "slot_id": slot5_id,
        "bsu_id": bsu5_id,
        "customer_id": customer5_id,
        "current": slot5_current,
        "voltage": v5,
        "temp": 25,
        "slot_soc": soc5,
        "slot_soh": soh5,
        "slot_status": "In-Use",
        "slot_mode": SLOT5_STATUS,
        "timestamp": timestamp
    }
    pub_client.publish(topic, json.dumps(slot5_payload))

"""
Function Name: slot6_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot6 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot6_telemetry_data():
    global soc6,soh6,SLOT6_STATUS,get_cust_id,v6,slot_mode,slot6_temp
    global slot6_message_id,station_id,slot6_id,bsu6_id,customer6_id,slot6_current
    timestamp = time.time()
    topic="fromSlot/{}/slotTelemetry".format(slot6_id)
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot6_payload={
        "message_id": slot6_message_id,
        "station_id": station_id,
        "slot_id": slot6_id,
        "bsu_id": bsu6_id,
        "customer_id": customer6_id,
        "current": slot6_current,
        "voltage": v6,
        "temp": 25,
        "slot_soc": soc6,
        "slot_soh": soh6,
        "slot_status": "In-Use",
        "slot_mode": SLOT6_STATUS,
        "timestamp": timestamp
    }
    pub_client.publish(topic, json.dumps(slot6_payload))

"""
Function Name: slot7_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot7 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot7_telemetry_data():
    global soc7,soh7,SLOT7_STATUS,get_cust_id,v7,slot_mode,slot7_temp
    global slot7_message_id,station_id,slot7_id,bsu7_id,customer7_id,slot7_current
    timestamp = time.time()
    topic="fromSlot/{}/slotTelemetry".format(slot7_id)
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot7_payload={
        "message_id": slot7_message_id,
        "station_id": station_id,
        "slot_id": slot7_id,
        "bsu_id": bsu7_id,
        "customer_id": customer7_id,
        "current": slot7_current,
        "voltage": v7,
        "temp": 25,
        "slot_soc": soc7,
        "slot_soh": soh7,
        "slot_status": "In-Use",
        "slot_mode": SLOT7_STATUS,
        "timestamp": timestamp
    }
    pub_client.publish(topic, json.dumps(slot7_payload))

"""
Function Name: slot8_telemetry_data
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for slot8 telemetry and publish it
               to the cloud via mqtt broker.
"""
def slot8_telemetry_data():
    global soc8,soh8,SLOT8_STATUS,get_cust_id,v7,slot_mode,slot8_temp
    global slot8_message_id,station_id,slot8_id,bsu8_id,customer8_id,slot8_current
    timestamp = time.time()
    topic="fromSlot/{}/slotTelemetry".format(slot8_id)
    #pub_client.connect("localhost", port=9001)
    pub_client.connect("evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com",port=9001)
    slot8_payload={
        "message_id": slot8_message_id,
        "station_id": station_id,
        "slot_id": slot8_id,
        "bsu_id": bsu8_id,
        "customer_id": customer8_id,
        "current": slot8_current,
        "voltage": v8,
        "temp": 25,
        "slot_soc": soc8,
        "slot_soh": soh8,
        "slot_status": "In-Use",
        "slot_mode": SLOT8_STATUS,
        "timestamp":timestamp
    }
    pub_client.publish(topic, json.dumps(slot8_payload))

"""
Function Name: create_json_payload
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for post method for
               station order
"""
def create_json_payload():
    global payload,payment_gateway,payment_method,retension_cost,late_fees,energy_slot,slot_no,payment_status
    global cost_per_unit,payment_done,bsu_id,customer_id,station_id,order_status,order_id,charging_id,pyment_id
    status = 0
    if status != 201:
        payment_status = "Awaited"
    else:
        payment_status = "Confirmed"
    URL = "http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3002/api/v1/order/station"
    #URL = "http://localhost:3002/api/v1/order/station"
    generate_data_for_order()
    payload={
        "gps_geolocation": [
          18.9888,
          73.4332
        ],
        "order_id": order_id,
        "order_type": "bsu",
        "order_status": order_status,
        "station_id": station_id,
        "customer_id": customer_id,
        "bsu_id": bsu_id,
        "slot_id": slot_id,
        "charging_id": charging_id,
        "slot_no": slot_no,
        "payment_id": payment_id,
        "payment_method": payment_method,
        "payment_gateway": payment_gateway,
        "payment_status": payment_status,
        "start_time_epoch": "2022-03-19T11:34:00.000Z",
        "end_time_epoch": "2022-03-19T14:34:00.000Z",
        "retention_fee": retension_cost,
        "late_fee": late_fees,
        "total_fee": final_payment,
        "cost_unit": cost_per_unit,
        "comments": "Booking Confirmed",
        "booking_time": 35,
    }
    result = requests.post(url=URL,data=payload)
    status = result.status_code
    print("Status code: ", result.status_code)
    payment_done=1

def get_bsu_details():
    global bsu_id,station_id,slot_id,slot_no,bsu_state,bsu_mode,bsu_config_id,query_bsu_id
    global account_id,order_status,inservice_hrs,battery_pack_id,bsu_man_name,bsu_serialno
    #URL = "http://localhost:3001/api/v1/info/bsu/{}".format(query_bsu_id)
    URL = "http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/info/bsu/{}".format(query_bsu_id)
    result = requests.get(URL)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    bsu_id = dict_json['bsuInfo'][0]['BSU ID']
    bsu_id = f"{bsu_id}"
    bsu_state = dict_json['bsuInfo'][0]['Status']
    bsu_state = f"{bsu_state}"
    bsu_mode  = dict_json['bsuInfo'][0]['Mode']
    bsu_mode = f"{bsu_mode}"
    order_status = dict_json['bsuInfo'][0]['Order Status']
    order_status = f"{order_status}"
    inservice_hrs = dict_json['bsuInfo'][0]['In service Hrs']
    inservice_hrs = f"{inservice_hrs}"
    battery_pack_id = dict_json['bsuInfo'][0]['Battery Pack ID']
    battery_pack_id = f"{battery_pack_id}"
    bsu_man_name = dict_json['bsuInfo'][0]['Thing Name']
    bsu_man_name = f"{bsu_man_name}"
    details = bsu_detials(bsu_id,bsu_state,bsu_mode,order_status,inservice_hrs,battery_pack_id,bsu_man_name)
    details.send_bsudata_to_frontend()

def get_battery_details():
    global battery_man_name,battery_capacity,battery_chemistry,battery_config,battery_cell,battery_model,query_bsu_id
    #URL = "http://localhost:3001/api/v1/info/bsu/spec/batteryPack/{}".format(query_bsu_id)
    URL = "http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/info/bsu/spec/batteryPack/{}".format(query_bsu_id)
    result = requests.get(URL)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    battery_man_name = dict_json['batteryPackSpecData']['battery_pack_manufacturer_name']
    battery_man_name = f"{battery_man_name}"
    battery_capacity = dict_json['batteryPackSpecData']['battery_pack_capacity']
    battery_capacity = f"{battery_capacity} Ah"
    battery_chemistry  = dict_json['batteryPackSpecData']['battery_pack_chemistry']
    battery_chemistry = f"{battery_chemistry}"
    battery_config = dict_json['batteryPackSpecData']['battery_pack_configuration']
    battery_config = f"{battery_config}"
    battery_cell = dict_json['batteryPackSpecData']['battery_pack_no_of_cells']
    battery_cell = f"{battery_cell}"
    battery_model = dict_json['batteryPackSpecData']['battery_pack_model_number']
    battery_model = f"{battery_model}"
    batterydetails = battery_details(battery_man_name,battery_capacity,battery_chemistry,battery_config,battery_cell,battery_model)
    batterydetails.send_batterydata_to_frontend()

class battery_details:
    def __init__(self,battery_man_name,battery_capacity,battery_chemistry,battery_config,battery_cell,battery_model):
        self.battery_man_name = battery_man_name
        self.battery_capacity = battery_capacity
        self.battery_chemistry = battery_chemistry
        self.battery_config    = battery_config
        self.battery_cell      = battery_cell
        self.battery_model     = battery_model

    def send_batterydata_to_frontend(self):
        global model_battery_man_name ,model_battery_capacity,model_battery_chemistry,model_battery_config
        global model_battery_cells,model_battery_model
        model_battery_man_name.setStringList([self.battery_man_name])
        engine_py_to_qml.rootContext().setContextProperty("model_battery_man_name", model_battery_man_name)
        model_battery_capacity.setStringList([self.battery_capacity])
        engine_py_to_qml.rootContext().setContextProperty("model_battery_capacity", model_battery_capacity)
        model_battery_chemistry.setStringList([self.battery_chemistry])
        engine_py_to_qml.rootContext().setContextProperty("model_battery_chemistry", model_battery_chemistry)
        model_battery_config.setStringList([self.battery_config])
        engine_py_to_qml.rootContext().setContextProperty("model_battery_config", model_battery_config)
        model_battery_cells.setStringList([self.battery_cell])
        engine_py_to_qml.rootContext().setContextProperty("model_battery_cells", model_battery_cells)
        model_battery_model.setStringList([self.battery_model])
        engine_py_to_qml.rootContext().setContextProperty("model_battery_model", model_battery_model)


class bsu_detials:
    def __init__(self,bsu_id,bsu_state,bsu_mode,order_status,inservice_hrs,battery_pack_id,bsu_man_name):
        self.bsu_id                 = bsu_id
        self.bsu_state              = bsu_state
        self.bsu_mode               = bsu_mode
        self.order_status           = order_status
        self.inservice_hrs          = inservice_hrs
        self.battery_pack_id        = battery_pack_id
        self.bsu_man_name           = bsu_man_name

    def send_bsudata_to_frontend(self):
        global model_bsu_id,model_bsu_man_name,model_bsu_state,model_bsu_mode
        global model_order_status,model_inservice_hrs,model_batterypack_id
        model_bsu_id.setStringList([self.bsu_id])
        engine_py_to_qml.rootContext().setContextProperty("model_bsu_id", model_bsu_id)
        model_bsu_state.setStringList([self.bsu_state])
        engine_py_to_qml.rootContext().setContextProperty("model_bsu_state", model_bsu_state)
        model_bsu_mode.setStringList([self.bsu_mode])
        engine_py_to_qml.rootContext().setContextProperty("model_bsu_mode", model_bsu_mode)
        model_order_status.setStringList([self.order_status])
        engine_py_to_qml.rootContext().setContextProperty("model_order_status", model_order_status)
        model_inservice_hrs.setStringList([self.inservice_hrs])
        engine_py_to_qml.rootContext().setContextProperty("model_inservice_hrs", model_inservice_hrs)
        model_batterypack_id.setStringList([self.battery_pack_id])
        engine_py_to_qml.rootContext().setContextProperty("model_batterypack_id", model_batterypack_id)
        model_bsu_man_name.setStringList([self.bsu_man_name])
        engine_py_to_qml.rootContext().setContextProperty("model_bsu_man_name", model_bsu_man_name)

class slot_data:
    def __init__(self,slot_number):
        self.slot_number = slot_number
    def get_data_for_selcted_slot(self):
        global soc1,soc2,soc3,soc4,soc5,soc6,soc7,soc8,v1,v2,v3,v4,v5,v6,v7,v8,get_cust_id,stationID
        global SLOT1_STATUS,SLOT2_STATUS,SLOT3_STATUS,SLOT4_STATUS,SLOT5_STATUS,SLOT6_STATUS,SLOT7_STATUS,SLOT8_STATUS
        global slot1_message_id,station_id,slot1_id,bsu1_id,customer1_id,slot1_status,slot1_soh,slot1_current,slot1_voltage
        global slot2_message_id,slot2_id,bsu2_id,customer2_id,slot2_status,slot2_soh,slot2_current,slot2_voltage
        global slot3_message_id,slot3_id,bsu3_id,customer3_id,slot3_status,slot3_soh,slot3_current,slot3_voltage
        global slot4_message_id,slot4_id,bsu4_id,customer4_id,slot4_status,slot4_soh,slot4_current,slot4_voltage
        global slot5_message_id,slot5_id,bsu5_id,customer5_id,slot5_status,slot5_soh,slot5_current,slot5_voltage
        global slot6_message_id,slot6_id,bsu6_id,customer6_id,slot6_status,slot6_soh,slot6_current,slot6_voltage
        global slot7_message_id,slot7_id,bsu7_id,customer7_id,slot7_status,slot7_soh,slot7_current,slot7_voltage
        global slot8_message_id,slot8_id,bsu8_id,customer8_id,slot8_status,slot8_soh,slot8_current,slot8_voltage

        query_params=""
        if self.slot_number == 1:
            query_params={"station_id":"station01","slot_no":"1"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu1_id = dict_json['bsuTelemetry'][0]['BSU ID']
            soc1 = dict_json['bsuTelemetry'][0]['Pack SoC']
            v1 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot1_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer1_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot1_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot1_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']
        elif self.slot_number == 2:
            query_params={"station_id":"station01","slot_no":"2"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu2_id = dict_json['bsuTelemetry'][0]['BSU ID']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            soc2 = dict_json['bsuTelemetry'][0]['Pack SoC']
            v2 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            slot2_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer2_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot2_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot2_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']
        elif self.slot_number == 3:
            query_params={"station_id":"station01","slot_no":"3"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu3_id = dict_json['bsuTelemetry'][0]['BSU ID']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            soc3 = dict_json['bsuTelemetry'][0]['Pack SoC']
            v3 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            slot3_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer3_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot3_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot3_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']
        elif self.slot_number == 4:
            query_params={"station_id":"station01","slot_no":"4"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu4_id = dict_json['bsuTelemetry'][0]['BSU ID']
            soc4 = dict_json['bsuTelemetry'][0]['Pack SoC']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            v4 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            station_id = dict_json['bsuTelemetry'][0]['Station ID']
            slot4_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer4_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot4_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot4_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']
        elif self.slot_number == 5:
            query_params={"station_id":"station01","slot_no":"5"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu5_id = dict_json['bsuTelemetry'][0]['BSU ID']
            soc5 = dict_json['bsuTelemetry'][0]['Pack SoC']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            v5 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            station_id = dict_json['bsuTelemetry'][0]['Station ID']
            slot5_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer5_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot5_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot5_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']
        elif self.slot_number == 6:
            query_params={"station_id":"station01","slot_no":"6"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu6_id = dict_json['bsuTelemetry'][0]['BSU ID']
            soc6 = dict_json['bsuTelemetry'][0]['Pack SoC']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            v6 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            station_id = dict_json['bsuTelemetry'][0]['Station ID']
            slot6_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer6_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot6_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot6_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']
        elif self.slot_number == 7:
            query_params={"station_id":"station01","slot_no":"7"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu7_id = dict_json['bsuTelemetry'][0]['BSU ID']
            soc7 = dict_json['bsuTelemetry'][0]['Pack SoC']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            v7 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            station_id = dict_json['bsuTelemetry'][0]['Station ID']
            slot7_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer7_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot7_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot7_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']
        elif self.slot_number == 8:
            query_params={"station_id":"station01","slot_no":"8"}
            #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
            response = result.json()
            json_dump = json.dumps(response)
            dict_json = json.loads(json_dump)
            bsu8_id = dict_json['bsuTelemetry'][0]['BSU ID']
            soc8 = dict_json['bsuTelemetry'][0]['Pack SoC']
            get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
            v8 = dict_json['bsuTelemetry'][0]['Pack Voltage']
            station_id = dict_json['bsuTelemetry'][0]['Station ID']
            slot8_message_id = dict_json['bsuTelemetry'][0]['Message ID']
            customer8_id = dict_json['bsuTelemetry'][0]['Customer ID']
            slot8_id = dict_json['bsuTelemetry'][0]['Slot ID']
            slot8_current = dict_json['bsuTelemetry'][0]['Pack Current']
            stationID = dict_json['bsuTelemetry'][0]['Station ID']

"""
Class name: Slected slot details
Input args: data to send to qml
Retrun: Null
Descriptoion: This class take input arguments while object get instatiated.
              Pass the required data to qml using different models.
              for sneding data to qml send_data_to_frontend is being called
              from the class.
"""
class selected_slot_details:
    def __init__(self,soc,voltage,min_temp,max_temp,imbalance,soh,v_cell_min,v_cell_max,v_cell_avg,
    charging_max,discharging_min, c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,
    energy_slot, final_payment, slot_number,retension_cost,time_taken_to_charge,booked_slot_soc,est_payment,taxes):

        self.soc                    = soc
        self.voltage                = voltage
        self.min_temp               = min_temp
        self.max_temp               = max_temp
        self.imbalance              = imbalance
        self.soh                    = soh
        self.v_cell_min             = v_cell_min
        self.v_cell_max             = v_cell_max
        self.v_cell_avg             = v_cell_avg
        self.charging_max           = charging_max
        self.discharging_min        = discharging_min
        self.c1_temp                = c1_temp
        self.c2_temp                = c2_temp
        self.c3_temp                = c3_temp
        self.c4_temp                = c4_temp
        self.c5_temp                = c5_temp
        self.c6_temp                = c6_temp
        self.c7_temp                = c7_temp
        self.c8_temp                = c8_temp
        self.energy_slot            = energy_slot
        self.final_payment          = final_payment
        self.slot_number            = slot_number
        self.retension_cost         = retension_cost
        self.time_taken_to_charge   = time_taken_to_charge
        self.booked_slot_soc        = booked_slot_soc
        self.est_payment            = est_payment
        self.taxes                  = taxes


    def send_data_to_frontend(self):
        global model_soc_summary, model_voltage_summary, model_temp_summary, model_imbalance_summary, model_soh_summary
        global model_v_cell_avg_summary, model_v_cell_summary,model_cell1_temp_sensor,model_cell2_temp_sensor,retension_cost,time_taken_to_charge,booked_slot_soc
        global model_cell1_temp_sensor,model_cell2_temp_sensor,model_cell3_temp_sensor,model_cell4_temp_sensor,model_cell5_temp_sensor,model_cell6_temp_sensor,model_cell7_temp_sensor,model_cell8_temp_sensor
        global model_module_tem_sensor_summary, model_selected_slot,model_final_payment,model_retension_cost,model_time_taken_to_charge,model_booked_slot_soc,model_estimated_payment
        global model_taxes,model_bsu_id,model_slot_id,model_slot_no,model_bsu_state,model_bsu_mode
        model_soc_summary.setStringList([self.soc])
        engine_py_to_qml.rootContext().setContextProperty("model_soc_summary", model_soc_summary)
        model_voltage_summary.setStringList([self.voltage])
        engine_py_to_qml.rootContext().setContextProperty("model_voltage_summary", model_voltage_summary)
        model_temp_summary.setStringList([self.min_temp,self.max_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_temp_summary", model_temp_summary)
        model_imbalance_summary.setStringList([self.imbalance])
        engine_py_to_qml.rootContext().setContextProperty("model_imbalance_summary", model_imbalance_summary)
        model_soh_summary.setStringList([self.soh])
        engine_py_to_qml.rootContext().setContextProperty("model_soh_summary", model_soh_summary)
        model_v_cell_summary.setStringList([self.v_cell_min,self.v_cell_max])
        engine_py_to_qml.rootContext().setContextProperty("model_v_cell_summary", model_v_cell_summary)
        model_v_cell_avg_summary.setStringList([self.v_cell_avg])
        engine_py_to_qml.rootContext().setContextProperty("model_v_cell_avg_summary", model_v_cell_avg_summary)
        model_charging_max.setStringList([self.charging_max])
        engine_py_to_qml.rootContext().setContextProperty("model_charging_max", model_charging_max)
        model_discharging_min.setStringList([self.discharging_min])
        engine_py_to_qml.rootContext().setContextProperty("model_discharging_min", model_discharging_min)
        model_slot_energy.setStringList([self.energy_slot])
        engine_py_to_qml.rootContext().setContextProperty("model_slot_energy", model_slot_energy)
        model_cell1_temp_sensor.setStringList([self.c1_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell1_temp_sensor", model_cell1_temp_sensor)
        model_cell2_temp_sensor.setStringList([self.c2_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell2_temp_sensor", model_cell2_temp_sensor)
        model_cell3_temp_sensor.setStringList([self.c3_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell3_temp_sensor", model_cell3_temp_sensor)
        model_cell4_temp_sensor.setStringList([self.c4_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell4_temp_sensor", model_cell4_temp_sensor)
        model_cell5_temp_sensor.setStringList([self.c5_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell5_temp_sensor", model_cell5_temp_sensor)
        model_cell6_temp_sensor.setStringList([self.c6_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell6_temp_sensor", model_cell6_temp_sensor)
        model_cell7_temp_sensor.setStringList([self.c7_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell7_temp_sensor", model_cell7_temp_sensor)
        model_cell8_temp_sensor.setStringList([self.c8_temp])
        engine_py_to_qml.rootContext().setContextProperty("model_cell8_temp_sensor", model_cell8_temp_sensor)
        model_selected_slot.setStringList([self.slot_number])
        engine_py_to_qml.rootContext().setContextProperty("model_selected_slot", model_selected_slot)
        model_retension_cost.setStringList([self.retension_cost])
        engine_py_to_qml.rootContext().setContextProperty("model_retension_cost", model_retension_cost)
        model_time_taken_to_charge.setStringList([self.time_taken_to_charge])
        engine_py_to_qml.rootContext().setContextProperty("model_time_taken_to_charge", model_time_taken_to_charge)
        model_booked_slot_soc.setStringList([self.booked_slot_soc])
        engine_py_to_qml.rootContext().setContextProperty("model_booked_slot_soc", model_booked_slot_soc)
        model_final_payment.setStringList([self.final_payment])
        engine_py_to_qml.rootContext().setContextProperty("model_final_payment", model_final_payment)
        model_estimated_payment.setStringList([self.est_payment])
        engine_py_to_qml.rootContext().setContextProperty("model_estimated_payment", model_estimated_payment)
        model_taxes.setStringList([self.taxes])
        engine_py_to_qml.rootContext().setContextProperty("model_taxes", model_taxes)



"""
Function Name: close_the_thread()
Input args   : Null
Retrun       : Null
Description  : this function will cancle the already running thread
"""
def close_the_thread() :
    global thread_1_flag, thread_2_flag, thread_3_flag, thread_4_flag, thread_5_flag, thread_6_flag, thread_7_flag, thread_8_flag
    global slot_1_th, slot_2_th, slot_3_th, slot_4_th, slot_5_th, slot_6_th, slot_7_th, slot_8_th
    if thread_1_flag :
        slot_1_th.cancel()
        thread_1_flag = False
    if thread_2_flag :
        slot_2_th.cancel()
        thread_2_flag = False
    if thread_3_flag :
        slot_3_th.cancel()
        thread_3_flag = False
    if thread_4_flag :
        slot_4_th.cancel()
        thread_4_flag = False
    if thread_5_flag :
        slot_5_th.cancel()
        thread_5_flag = False
    if thread_6_flag :
        slot_6_th.cancel()
        thread_6_flag = False
    if thread_7_flag :
        slot_7_th.cancel()
        thread_7_flag = False
    if thread_8_flag :
        slot_8_th.cancel()
        thread_8_flag = False

def join_the_slot_thread():
    global main_th
    global slot_1_th, slot_2_th, slot_3_th, slot_4_th, slot_5_th, slot_6_th, slot_7_th, slot_8_th
    if slot_1_th:
        slot_1_th.join()
    if slot_2_th:
        slot_2_th.join()
    if slot_3_th:
        slot_3_th.join()
    if slot_4_th:
        slot_4_th.join()
    if slot_5_th:
        slot_5_th.join()
    if slot_6_th:
        slot_6_th.join()
    if slot_7_th:
        slot_7_th.join()
    if slot_8_th:
        slot_8_th.join()
    if main_th:
        main_th.join()

# Get slot 1 summary details thread routine
def get_slot_1_data():
    global discharging_min,thread_1_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc1,retension_cost,booked_slot_soc,est_payment
    global slot_1_th,slot_number,time_taken_to_charge,calcute_taxes,bsu_id,station_id,slot_id,slot_no,bsu_state,bsu_mode,query_bsu_id,soh1;
    global soc1
    volatage_base_index=4.2
    close_the_thread()
    thread_1_flag = True
    charging_max = 20
    slot_no = 1
    query_params={"station_id":"station01","slot_no":"1"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    soh1 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    energy_slot = 28.1
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V1 = f"{v:.1f} V"
    SOC = f"{soc1:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    SOH = f"{soh1}%"
    slot_number = "S1"
    SLOT_NUMBER = f"{slot_number}"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    RETENSION_COST = f"{retension_cost}"
    TIME = f"{time_taken_to_charge}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    TAXES = f"{calcute_taxes:.2f}"
    slot1_obj = selected_slot_details(SOC,V1,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot1_obj.send_data_to_frontend()
    slot_1_th = threading.Timer(4, get_slot_1_data)
    slot_1_th.start()

# Get slot 2 summary details thread routine
def get_slot_2_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_2_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc2,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_2_th,slot_number,time_taken_to_charge,slot_no
    global query_bsu_id,soh2,soc2,slot_id
    close_the_thread()
    volatage_base_index=4.2
    thread_2_flag = True
    slot_no = 2
    query_params={"station_id":"station01","slot_no":"2"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    soh2 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    energy_slot = 40.1
    slot_number = "S2"
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{v:.1f} V"
    SOC = f"{soc2:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    SOH = f"{soh2}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    TAXES = f"{calcute_taxes:.2f}"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    TIME = f"{time_taken_to_charge}"
    slot2_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot2_obj.send_data_to_frontend()
    slot_2_th = threading.Timer(4, get_slot_2_data)
    slot_2_th.start()

# Get slot 3 summary details thread routine
def get_slot_3_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_3_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc3,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_3_th,slot_number,time_taken_to_charge
    global query_bsu_id,soh3,slot_id
    close_the_thread()
    volatage_base_index=4.2
    thread_3_flag = True
    slot_no = 3
    query_params={"station_id":"station01","slot_no":"3"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    soc = dict_json['bsuTelemetry'][0]['Pack SoC']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    soh3 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    energy_slot = 28.1
    slot_number = "S3"
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{v:.2f}"
    SOC = f"{soc:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{3.92:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    SOH = f"{soh3}%"
    CHARGE_MAX = f"{-35}A"
    DISCHARGE_MIN = f"{500}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    TAXES = f"{calcute_taxes}"
    EST_PAYMET = f"{est_payment:.2f}"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    TIME = f"{time_taken_to_charge}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    slot3_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot3_obj.send_data_to_frontend()
    slot_3_th = threading.Timer(4, get_slot_3_data)
    slot_3_th.start()

# Get slot 4 summary details thread routine
def get_slot_4_data():
    global thread_4_flag,energy_slot,final_payment,late_fees,cost_per_unit,retension_cost,booked_slot_soc
    global slot_4_th,slot_number,time_taken_to_charge,est_payment,calcute_taxes,slot_no
    global query_bsu_id,soh4,slot_id
    close_the_thread()
    thread_4_flag = True
    volatage_base_index=4.2
    slot_no = 4
    query_params={"station_id":"station01","slot_no":"4"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    soc = dict_json['bsuTelemetry'][0]['Pack SoC']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    soh4 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    energy_slot = 20.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{v:.2f}"
    SOC = f"{soc:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    SOH = f"{soh4}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    TAXES = f"{calcute_taxes:.2f}"
    slot_number = "S4"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    TIME = f"{time_taken_to_charge}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    slot4_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot4_obj.send_data_to_frontend()
    slot_4_th = threading.Timer(4, get_slot_4_data)
    slot_4_th.start()

# Get slot 5 summary details thread routine
def get_slot_5_data():
    global thread_5_flag,energy_slot,final_payment,late_fees,cost_per_unit,retension_cost,booked_slot_soc
    global slot_5_th,slot_number,time_taken_to_charge,est_payment,calcute_taxes,slot_no
    global query_bsu_id,soh5,slot_id
    close_the_thread()
    thread_5_flag = True
    volatage_base_index=4.2
    charging_max = 20
    slot_no = 5
    query_params={"station_id":"station01","slot_no":"5"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    soc = dict_json['bsuTelemetry'][0]['Pack SoC']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    soh5 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    energy_slot = 50.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{v:.2f}"
    SOC = f"{soc:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    SOH = f"{soh5}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    TAXES = f"{calcute_taxes:.2f}"
    slot_number = "S5"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    TIME = f"{time_taken_to_charge}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    slot5_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot5_obj.send_data_to_frontend()
    slot_5_th = threading.Timer(4, get_slot_5_data)
    slot_5_th.start()

# Get slot 6 summary details thread routine
def get_slot_6_data():
    global thread_6_flag,energy_slot,final_payment,late_fees,cost_per_unit,retension_cost,booked_slot_soc
    global slot_6_th,slot_number,time_taken_to_charge,est_payment,calcute_taxes,slot_no
    global query_bsu_id,soh6,slot_id
    close_the_thread()
    thread_6_flag = True
    volatage_base_index=4.2
    charging_max = 20
    slot_no = 6
    query_params={"station_id":"station01","slot_no":"6"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    soc = dict_json['bsuTelemetry'][0]['Pack SoC']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    soh6 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    energy_slot = 25.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{v:.2f}"
    SOC = f"{soc:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    SOH = f"{soh6}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    TAXES = f"{calcute_taxes:.2f}"
    slot_number = "S6"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    TIME = f"{time_taken_to_charge}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    slot6_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot6_obj.send_data_to_frontend()
    slot_6_th = threading.Timer(4, get_slot_6_data)
    slot_6_th.start()

# Get slot 7 summary details thread routine
def get_slot_7_data():
    global thread_7_flag,energy_slot,final_payment,late_fees,cost_per_unit,retension_cost,booked_slot_soc
    global slot_7_th,slot_number,time_taken_to_charge,est_payment,calcute_taxes,slot_no
    global query_bsu_id,soh7,slot_id
    close_the_thread()
    thread_7_flag = True
    volatage_base_index=4.2
    slot_no = 7
    charging_max = 20
    query_params={"station_id":"station01","slot_no":"7"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    soc = dict_json['bsuTelemetry'][0]['Pack SoC']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    soh7 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    energy_slot = 29.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{v:.2f}"
    SOC = f"{soc:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    SOH = f"{soh7}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    TAXES = f"{calcute_taxes:.2f}"
    slot_number = "S7"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(1000))
    TIME = f"{time_taken_to_charge}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    slot7_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot7_obj.send_data_to_frontend()
    slot_7_th = threading.Timer(4, get_slot_7_data)
    slot_7_th.start()

# Get slot 8 summary details thread routine
def get_slot_8_data():
    global thread_8_flag,energy_slot,final_payment,late_fees,cost_per_unit,retension_cost,booked_slot_soc
    global slot_8_th,slot_number,time_taken_to_charge,est_payment,calcute_taxes,slot_no
    global query_bsu_id,soh8,slot_id
    close_the_thread()
    thread_8_flag = True
    volatage_base_index=4.2
    charging_max = 20
    slot_no = 8
    query_params={"station_id":"station01","slot_no":"8"}
    #result = requests.get('http://localhost:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    result = requests.get('http://evbs-nlb-a7b4d2ac5c830679.elb.us-east-1.amazonaws.com:3001/api/v1/telemetry/bsu/station/slot',params=query_params)
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    query_bsu_id = dict_json['bsuTelemetry'][0]['BSU ID']
    slot_id = dict_json['bsuTelemetry'][0]['Slot ID']
    soc = dict_json['bsuTelemetry'][0]['Pack SoC']
    get_cust_id = dict_json['bsuTelemetry'][0]['Customer ID']
    soh8 = dict_json['bsuTelemetry'][0]['Pack SoH']
    v = dict_json['bsuTelemetry'][0]['Pack Voltage']
    pack_voltage = dict_json['bsuTelemetry'][0]['Cell Voltage']
    v_cell_max = max(pack_voltage)
    v_cell_min = min(pack_voltage)
    v_cell_avg = sum(pack_voltage)/len(pack_voltage)
    pack_temp = dict_json['bsuTelemetry'][0]['Cell Temperature']
    min_temp = min(pack_temp)
    max_temp = max(pack_temp)
    imbalance = ((volatage_base_index-pack_voltage[0])+(volatage_base_index-pack_voltage[1])+(volatage_base_index-pack_voltage[2])+(volatage_base_index-pack_voltage[3]))
    discharging_min = 10
    c1_temp = pack_temp[0]
    c2_temp = pack_temp[1]
    c3_temp = pack_temp[2]
    c4_temp = pack_temp[3]
    c5_temp = "NA"
    c6_temp = "NA"
    c7_temp = "NA"
    c8_temp = "NA"
    energy_slot = 15.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{v:.2f}"
    SOC = f"{soc:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp}"
    C6_TEMP = f"{c6_temp}"
    C7_TEMP = f"{c7_temp}"
    C8_TEMP = f"{c8_temp}"
    SOH = f"{soh8}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    TAXES = f"{calcute_taxes:.2f}"
    slot_number = "S8"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    TIME = f"{time_taken_to_charge}"
    BOOKED_SLOT_SOC = f"{booked_slot_soc:.2f}%"
    slot8_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot8_obj.send_data_to_frontend()
    slot_8_th = threading.Timer(4, get_slot_8_data)
    slot_8_th.start()

# Available Slots information thread routine
def get_data_thread_routine():
    global model_slot1, model_slot2, model_slot3, model_slot4,model_slot4
    global model_slot5,model_slot6,model_slot7,model_slot8,model_cost_per_unit,model_late_fees
    global model_uniqueID,cost_per_unit,late_fees,model_customer_name,get_cust_id
    global main_th,soc1, soc2, soc3, soc4,soc5,soc6,soc7,soc8
    global v1, v2, v3, v4, v5, v6, v7, v8,slot1_status,slot2_status,slot1_status_flag,slot2_status_flag,slot3_status_flag,slot4_status_flag,slot5_status_flag,slot6_status_flag,slot7_status_flag,slot8_status_flag
    global model_slot1_status,model_slot2_status,model_slot3_status,model_slot4_status,model_slot5_status,model_slot6_status,model_slot7_status,model_slot8_status
    global SLOT1_STATUS,SLOT2_STATUS,SLOT3_STATUS,SLOT4_STATUS,SLOT5_STATUS,SLOT6_STATUS,SLOT7_STATUS,SLOT8_STATUS
    V1,V2,V3,V4,V5,V6,V7,V6,SOC1,SOC2,SOC3,SOC4,SOC5,SOC6,SOC7,SOC8="","","","","","","","","","","","","","","",""
    # Starting the loop thread for MQTT subscription
    sub_client.loop_start()
    slot1 = slot_data(1);
    slot2 = slot_data(2);
    slot3 = slot_data(3);
    slot4 = slot_data(4);
    slot5 = slot_data(5);
    slot6 = slot_data(6);
    slot7 = slot_data(7);
    slot8 = slot_data(8);
    cost_per_unit = 12
    late_fees = 50
    slot1.get_data_for_selcted_slot();
    slot2.get_data_for_selcted_slot();
    slot3.get_data_for_selcted_slot();
    slot4.get_data_for_selcted_slot();
    slot5.get_data_for_selcted_slot();
    slot6.get_data_for_selcted_slot();
    slot7.get_data_for_selcted_slot();
    slot8.get_data_for_selcted_slot();
    COST = f"{cost_per_unit}"
    LATE_FEES = f"{late_fees}"
    CUST_NAME = f"{get_cust_id}"
    if SLOT1_STATUS == "Empty" or SLOT1_STATUS == "Fault"  or slot1_status_flag ==2 or slot1_status_flag ==4:
        if SLOT1_STATUS == "Empty":
            slot1_status_flag =2
        if SLOT1_STATUS == "Fault":
            slot1_status_flag =4
        V1,SOC1="",""
        model_slot1.setStringList([V1,SOC1])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_1", model_slot1)
        if payment_done == 0 and (SLOT1_STATUS == "Available" or SLOT1_STATUS == "Charging" or SLOT1_STATUS == "Prebooked" or SLOT1_STATUS == "Discharging"):
            slot1_status_flag=0
    if SLOT2_STATUS == "Empty" or SLOT2_STATUS == "Fault"  or slot2_status_flag ==2 or slot2_status_flag ==4:
        if SLOT2_STATUS == "Empty":
            slot2_status_flag =2
        if SLOT2_STATUS == "Fault":
            slot2_status_flag =4
        V2,SOC2="",""
        model_slot2.setStringList([V2,SOC2])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_2", model_slot2)
        if payment_done == 0 and (SLOT2_STATUS == "Available" or SLOT2_STATUS == "Charging" or SLOT2_STATUS == "Prebooked" or SLOT2_STATUS == "Discharging"):
            slot2_status_flag=0
    if SLOT3_STATUS =="Empty" or SLOT3_STATUS == "Fault" or slot3_status_flag ==2 or slot3_status_flag ==4:
        if SLOT3_STATUS == "Empty":
            slot3_status_flag =2
        elif SLOT3_STATUS == "Fault":
            slot3_status_flag =4
        v3,soc3="",""
        V3,SOC3="",""
        model_slot3.setStringList([V3,SOC3])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_3", model_slot3)
        if payment_done == 0 and (SLOT3_STATUS == "Available" or SLOT3_STATUS == "Charging" or SLOT3_STATUS == "Prebooked" or SLOT3_STATUS == "Discharging"):
            slot3_status_flag=0
    if SLOT4_STATUS =="Empty" or SLOT4_STATUS == "Fault" or slot4_status_flag ==2 or slot4_status_flag ==4:
        if SLOT4_STATUS == "Empty":
            slot4_status_flag =2
        elif SLOT4_STATUS == "Fault":
            slot4_status_flag =4
        V4,SOC4="",""
        model_slot4.setStringList([V4,SOC4])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_4", model_slot4)
        if payment_done == 0 and (SLOT4_STATUS == "Available" or SLOT4_STATUS == "Charging" or SLOT4_STATUS == "Prebooked" or SLOT4_STATUS == "Discharging"):
            slot4_status_flag=0
    if SLOT5_STATUS =="Empty" or SLOT5_STATUS == "Fault" or slot5_status_flag ==2 or slot5_status_flag ==4:
        if SLOT5_STATUS == "Empty":
            slot5_status_flag =2
        elif SLOT5_STATUS == "Fault":
            slot5_status_flag =4
        V5,SOC5="",""
        model_slot5.setStringList([V5,SOC5])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_5", model_slot5)
        if payment_done == 0 and (SLOT5_STATUS == "Available" or SLOT5_STATUS == "Charging" or SLOT5_STATUS == "Prebooked" or SLOT5_STATUS == "Discharging"):
            slot5_status_flag=0

    if SLOT6_STATUS =="Empty" or SLOT6_STATUS == "Fault" or slot6_status_flag ==2 or slot6_status_flag ==4:
        if SLOT6_STATUS == "Empty":
            slot6_status_flag =2
        elif SLOT6_STATUS == "Fault":
            slot6_status_flag =4
        V6,SOC6="",""
        model_slot6.setStringList([V6,SOC6])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_6", model_slot6)
        if payment_done == 0 and (SLOT6_STATUS == "Available" or SLOT6_STATUS == "Charging" or SLOT6_STATUS == "Prebooked" or SLOT6_STATUS == "Discharging"):
            slot6_status_flag=0

    if SLOT7_STATUS =="Empty" or SLOT7_STATUS == "Fault" or slot7_status_flag ==2 or slot7_status_flag ==4:
        if SLOT7_STATUS == "Empty":
            slot7_status_flag =2
        elif SLOT7_STATUS == "Fault":
            slot7_status_flag =4
        V7,SOC7="",""
        model_slot7.setStringList([V7,SOC7])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_7", model_slot7)
        if payment_done == 0 and (SLOT7_STATUS == "Available" or SLOT7_STATUS == "Charging" or SLOT7_STATUS == "Prebooked" or SLOT7_STATUS == "Discharging"):
            slot7_status_flag=0

    if SLOT8_STATUS =="Empty" or SLOT8_STATUS == "Fault" or slot8_status_flag ==2 or slot8_status_flag ==4:
        if SLOT8_STATUS == "Empty":
            slot8_status_flag =2
        elif SLOT8_STATUS == "Fault":
            slot8_status_flag =4
        V8,SOC8="",""
        model_slot8.setStringList([V8,SOC8])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_8", model_slot8)
        if payment_done == 0 and (SLOT8_STATUS == "Available" or SLOT8_STATUS == "Charging" or SLOT8_STATUS == "prebooked" or SLOT8_STATUS == "Discharging"):
            slot8_status_flag=0
    if (slot1_status_flag == 0 or slot1_status_flag == 1 or slot1_status_flag == 5 or slot1_status_flag == 3):
        if SLOT1_STATUS == "Available":
            slot1_status_flag = 1
        if SLOT1_STATUS == "Charging":
            slot1_status_flag = 0
        if SLOT1_STATUS == "Discharging":
            slot1_status_flag = 5
        if SLOT1_STATUS == "Prebooked":
            slot1_status_flag = 3
        slot1_status=SLOT1_STATUS
        SLOT1_STATUS=f"{slot1_status}"
        V1 = f"         {v1:.2f}V"
        SOC1 = f"SoC:{soc1:.2f}%"
        model_slot1.setStringList([V1,SOC1])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_1", model_slot1)
    if (slot2_status_flag == 0 or slot2_status_flag == 1 or slot2_status_flag == 5 or slot2_status_flag == 3):
        if SLOT2_STATUS == "Available":
            slot2_status_flag = 1
        if SLOT2_STATUS == "Charging":
            slot2_status_flag = 0
        if SLOT2_STATUS == "Discharging":
            slot2_status_flag = 5
        if SLOT2_STATUS == "Prebooked":
            slot2_status_flag = 3
        V2 = f"         {v2:.2f}V"
        SOC2 = f"SoC:{soc2:.2f}%"
        slot2_status=SLOT2_STATUS
        SLOT2_STATUS=f"{slot2_status}"
        model_slot2.setStringList([V2,SOC2])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_2", model_slot2)
    if (slot3_status_flag == 0 or slot3_status_flag == 1 or slot3_status_flag == 5 or slot3_status_flag == 3):
        if SLOT3_STATUS == "Available":
            slot3_status_flag = 1
        if SLOT3_STATUS == "Charging":
            slot3_status_flag = 0
        if SLOT3_STATUS == "Discharging":
            slot3_status_flag = 5
        if SLOT3_STATUS == "Prebooked":
            slot3_status_flag = 3
        V3 = f"         {v3:.2f}V"
        SOC3 = f"SoC:{soc3:.2f}%"
        slot3_status = SLOT3_STATUS
        SLOT3_STATUS = f"{slot3_status}"
        model_slot3.setStringList([V3,SOC3])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_3", model_slot3)
    if (slot4_status_flag == 0 or slot4_status_flag == 1 or slot4_status_flag == 5 or slot4_status_flag == 3):
        if SLOT4_STATUS == "Available":
            slot4_status_flag = 1
        if SLOT4_STATUS == "Charging":
            slot4_status_flag = 0
        if SLOT4_STATUS == "Discharging":
            slot4_status_flag = 5
        if SLOT4_STATUS == "Prebooked":
            slot4_status_flag = 3
        V4 = f"         {v4:.2f}V"
        SOC4 = f"SoC:{soc4:.2f}%"
        slot4_status = SLOT4_STATUS
        SLOT4_STATUS = f"{slot4_status}"
        model_slot4.setStringList([V4,SOC4])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_4", model_slot4)
    if (slot5_status_flag == 0 or slot5_status_flag == 1 or slot5_status_flag == 5 or slot5_status_flag == 3):
        if SLOT5_STATUS == "Available":
            slot5_status_flag = 1
        if SLOT5_STATUS == "Charging":
            slot5_status_flag = 0
        if SLOT5_STATUS == "Discharging":
            slot5_status_flag = 5
        if SLOT5_STATUS == "Prebooked":
            slot5_status_flag = 3
        slot5_status=SLOT5_STATUS
        V5 = f"         {v5:.2f}V"
        SOC5 = f"SoC:{soc5:.2f}%"
        SLOT5_STATUS=f"{slot5_status}"
        model_slot5.setStringList([V5,SOC5])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_5", model_slot5)
    if (slot6_status_flag == 0 or slot6_status_flag == 1 or slot6_status_flag == 5 or slot6_status_flag == 3):
        if SLOT6_STATUS == "Available":
            slot6_status_flag = 1
        if SLOT6_STATUS == "Charging":
            slot6_status_flag = 0
        if SLOT6_STATUS == "Discharging":
            slot6_status_flag = 5
        if SLOT6_STATUS == "Prebooked":
            slot6_status_flag = 3
        slot6_status=SLOT6_STATUS
        V6 = f"         {v6:.2f}V"
        SOC6 = f"SoC:{soc6:.2f}%"
        SLOT6_STATUS=f"{slot6_status}"
        model_slot6.setStringList([V6,SOC6])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_6", model_slot6)
    if (slot7_status_flag == 0 or slot7_status_flag == 1 or slot7_status_flag == 5 or slot7_status_flag == 3):
        if SLOT7_STATUS == "Available":
            slot7_status_flag = 1
        if SLOT7_STATUS == "Charging":
            slot7_status_flag = 0
        if SLOT7_STATUS == "Discharging":
            slot7_status_flag = 5
        if SLOT7_STATUS == "Prebooked":
            slot7_status_flag = 3
        slot7_status = SLOT7_STATUS
        V7 = f"         {v7:.2f}V"
        SOC7 = f"SoC:{soc7:.2f}%"
        SLOT7_STATUS = f"{slot7_status}"
        model_slot7.setStringList([V7,SOC7])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_7", model_slot7)
    if (slot8_status_flag == 0 or slot8_status_flag == 1 or slot8_status_flag == 5 or slot8_status_flag == 3):
        if SLOT8_STATUS == "Available":
            slot8_status_flag = 1
        if SLOT8_STATUS == "Charging":
            slot8_status_flag = 0
        if SLOT8_STATUS == "Discharging":
            slot8_status_flag = 5
        if SLOT8_STATUS == "Prebooked":
            slot8_status_flag = 3
        slot8_status = SLOT8_STATUS
        V8 = f"         {v8:.2f}V"
        SOC8 = f"SoC:{soc8:.2f}%"
        SLOT8_STATUS = f"{slot8_status}"
        model_slot8.setStringList([V8,SOC8])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_8", model_slot8)
    model_cost_per_unit.setStringList([COST])
    model_late_fees.setStringList([LATE_FEES])
    model_slot1_status.setStringList([SLOT1_STATUS])
    model_slot2_status.setStringList([SLOT2_STATUS])
    model_slot3_status.setStringList([SLOT3_STATUS])
    model_slot4_status.setStringList([SLOT4_STATUS])
    model_slot5_status.setStringList([SLOT5_STATUS])
    model_slot6_status.setStringList([SLOT6_STATUS])
    model_slot7_status.setStringList([SLOT7_STATUS])
    model_slot8_status.setStringList([SLOT8_STATUS])
    engine_py_to_qml.rootContext().setContextProperty("model_cost_per_unit", model_cost_per_unit)
    engine_py_to_qml.rootContext().setContextProperty("model_late_fees", model_late_fees)
    engine_py_to_qml.rootContext().setContextProperty("model_slot1_status", model_slot1_status)
    engine_py_to_qml.rootContext().setContextProperty("model_slot2_status", model_slot2_status)
    engine_py_to_qml.rootContext().setContextProperty("model_slot3_status", model_slot3_status)
    engine_py_to_qml.rootContext().setContextProperty("model_slot4_status", model_slot4_status)
    engine_py_to_qml.rootContext().setContextProperty("model_slot5_status", model_slot5_status)
    engine_py_to_qml.rootContext().setContextProperty("model_slot6_status", model_slot6_status)
    engine_py_to_qml.rootContext().setContextProperty("model_slot7_status", model_slot7_status)
    engine_py_to_qml.rootContext().setContextProperty("model_slot8_status", model_slot8_status)
    model_customer_name.setStringList([CUST_NAME])
    engine_py_to_qml.rootContext().setContextProperty("model_customer_name", model_customer_name)
    slot1_telemetry_data()
    slot2_telemetry_data()
    slot3_telemetry_data()
    slot4_telemetry_data()
    slot5_telemetry_data()
    slot6_telemetry_data()
    slot7_telemetry_data()
    slot8_telemetry_data()
    station_telemetry_data()

    # Stopping the loop thread for MQTT subscription
    sub_client.loop_stop()

    main_th = threading.Timer(4, get_data_thread_routine)
    main_th.start()

#Catch slot class for frequently retention booking
class catch_retension_time(QObject):
    @Slot(int)
    def test_retension_timeline(self, hrs):
        global retension_cost
        retension_cost = hrs*10;

#Catch slot class for custom frequently retention booking
class catch_custom_time(QObject):
    @Slot(str)
    def test_custom_timeline(self, days,hrs):
        global retension_cost
        calculate_days,calculate_hrs = 0,0
        calculate_days = int(days)
        calculate_days = calculate_days*240
        calculate_hrs = int(hrs)
        calculate_hrs = calculate_hrs*10
        retension_cost = calculate_days + calculate_hrs

# Slot class which launch the thread once signal emits from QMl
class catch_slot(QObject):
    @Slot(str)
    def test_slot(self, string):
        global retension_cost,soc1,soc2,soc3,soc4,soc5,soc6,soc7,soc8,booked_slot_soc,booked_slot_flag
        global slot_status,payment_gateway,payment_method
        global slot_status_string,v1,soc1,slot_1_th,slot_2_th
        global slot1_status_flag,slot2_status_flag,slot3_status_flag,slot4_status_flag,slot5_status_flag,slot6_status_flag
        global slot7_status_flag,slot8_status_flag
        global SLOT1_STATUS,SLOT2_STATUS,SLOT3_STATUS,SLOT4_STATUS,SLOT5_STATUS,SLOT6_STATUS,SLOT7_STATUS,SLOT8_STATUS
        retension_cost = 0
        if string in "AAAA":
            slot_status_string=string
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc1
                booked_slot_flag=False
            get_slot_1_data()
            get_battery_details()
            get_bsu_details()
        elif string in "BBBB":
            slot_status_string=string
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc2
                booked_slot_flag=False
            get_slot_2_data()
            get_battery_details()
            get_bsu_details()
        elif string in "CCCC":
            booked_slot_flag=True
            slot_status_string=string
            if booked_slot_flag:
                booked_slot_soc=soc3
                booked_slot_flag=False
            get_slot_3_data()
            get_battery_details()
            get_bsu_details()
        elif string in "DDDD":
            booked_slot_flag=True
            slot_status_string=string
            if booked_slot_flag:
                booked_slot_soc=soc4
                booked_slot_flag=False
            get_slot_4_data()
            get_battery_details()
            get_bsu_details()
        elif string in "EEEE":
            booked_slot_flag=True
            slot_status_string=string
            if booked_slot_flag:
                booked_slot_soc=soc5
                booked_slot_flag=False
            get_slot_5_data()
            get_battery_details()
            get_bsu_details()
        elif string in "FFFF":
            booked_slot_flag=True
            slot_status_string=string
            if booked_slot_flag:
                booked_slot_soc=soc6
                booked_slot_flag=False
            get_slot_6_data()
            get_battery_details()
            get_bsu_details()
        elif string in "GGGG":
            booked_slot_flag=True
            slot_status_string=string
            if booked_slot_flag:
                booked_slot_soc=soc7
                booked_slot_flag=False
            get_slot_7_data()
            get_battery_details()
            get_bsu_details()
        elif string in "HHHH":
            booked_slot_flag=True
            slot_status_string=string
            if booked_slot_flag:
                booked_slot_soc=soc8
                booked_slot_flag=False
            get_slot_8_data()
            get_battery_details()
            get_bsu_details()
        elif string in "googlepay":
            payment_gateway = "Google Pay"
            payment_method = "UPI"
        elif string in "amazonpay":
            payment_gateway = "Amazon Pay"
            payment_method = "UPI"
        elif string in "bharatpay":
            payment_gateway = "Bharat Pay"
            payment_method = "UPI"
        elif string in "proceed":
            create_json_payload()
            if slot_status_string == "AAAA":
                slot1_status_flag=2;
                slot1_status="Empty"
                SLOT1_STATUS=f"{slot1_status}"
                model_slot1_status.setStringList([SLOT1_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot1_status", model_slot1_status)
            if slot_status_string == "BBBB":
                slot2_status="Empty"
                SLOT2_STATUS=f"{slot2_status}"
                model_slot2_status.setStringList([SLOT2_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot2_status", model_slot2_status)
                slot2_status_flag=2;
            if slot_status_string == "CCCC":
                slot3_status="Empty"
                SLOT3_STATUS=f"{slot3_status}"
                model_slot3_status.setStringList([SLOT3_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot3_status", model_slot3_status)
                slot3_status_flag=2;
            if slot_status_string == "DDDD":
                slot4_status="Empty"
                SLOT4_STATUS=f"{slot4_status}"
                model_slot4_status.setStringList([SLOT4_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot4_status", model_slot4_status)
                slot4_status_flag=2;
            if slot_status_string == "EEEE":
                slot5_status="Empty"
                SLOT5_STATUS=f"{slot5_status}"
                model_slot5_status.setStringList([SLOT5_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot5_status", model_slot5_status)
                slot5_status_flag=2;
            if slot_status_string == "FFFF":
                slot6_status="Empty"
                SLOT6_STATUS=f"{slot6_status}"
                model_slot6_status.setStringList([SLOT6_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot6_status", model_slot6_status)
                slot6_status_flag=2;
            if slot_status_string == "GGGG":
                slot7_status="Empty"
                SLOT7_STATUS=f"{slot7_status}"
                model_slot7_status.setStringList([SLOT7_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot7_status", model_slot7_status)
                slot7_status_flag=2
            if slot_status_string == "HHHH":
                slot8_status="Empty"
                SLOT8_STATUS=f"{slot8_status}"
                model_slot8_status.setStringList([SLOT8_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot8_status", model_slot8_status)
                slot8_status_flag=2;

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine_py_to_qml = QQmlApplicationEngine()
    catchtheslot = catch_slot()
    catchcustomtimeline = catch_custom_time()
    catchretensiontime = catch_retension_time()
    engine_qml_to_py = QQmlApplicationEngine()
    engine_py_to_qml.load(QUrl.fromLocalFile('main.qml'))
    engine_qml_to_py.rootContext().setContextProperty("catch_slot", catch_slot)
    engine_qml_to_py.rootContext().setContextProperty("catch_custom_time", catch_custom_time)
    # Below line is to connect the signal(comming from QML) to respective slot which is define in python file
    engine_py_to_qml.rootObjects()[0].test_signal.connect(catchtheslot.test_slot, type=Qt.ConnectionType.QueuedConnection)
    engine_py_to_qml.rootObjects()[0].test_customsignal.connect(catchcustomtimeline.test_custom_timeline, type=Qt.ConnectionType.QueuedConnection)
    engine_py_to_qml.rootObjects()[0].test_retension_timeline.connect(catchretensiontime.test_retension_timeline, type=Qt.ConnectionType.QueuedConnection)
    get_data_thread_routine()
    #join_the_slot_thread()
    if not engine_py_to_qml.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
