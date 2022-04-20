import sys
from PySide2 import *
from PySide2.QtCore import QUrl, QStringListModel, QObject,Signal, Property,Slot, Qt
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
import time
import threading
import random
import requests
import json
import time

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

cost_per_unit,energy_slot,late_fees,final_payment,retension_cost,time_taken_to_charge,est_payment = 0,0,0,0,0,0,0
soc1,soc2,soc3,soc4,soc5,soc6,soc7,soc8,booked_slot_soc = 0,0,0,0,0,0,0,0,0
v1,v2,v3,v4,v5,v6,v7,v8 = 0,0,0,0,0,0,0,0
c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp = 0,0,0,0,0,0,0,0
voltage,min_temp,max_temp,imbalance,soh,v_cell_min,v_cell_max,calcute_taxes = 0,0,0,0,0,0,0,0
v_cell_avg, charging_max, discharging_min, slot_number,booked_slot_flag = 0,0,0,0,False
thread_1_flag, thread_2_flag, thread_3_flag, thread_4_flag,thread_5_flag, thread_6_flag, thread_7_flag, thread_8_flag = False, False, False, False, False, False, False, False
slot_1_th,slot_2_th,slot_3_th,slot_4_th,slot_5_th,slot_6_th,slot_7_th,slot_8_th = 0,0,0,0,0,0,0,0
payload = []
get_cust_id = 0
slot1_status_flag,slot2_status_flag,slot3_status_flag,slot4_status_flag,slot5_status_flag,slot6_status_flag,slot7_status_flag,slot8_status_flag,slot_status_string = 0,0,0,0,0,0,0,0,0
SLOT1_STATUS,SLOT2_STATUS = 0,0
slot1_status,slot2_status="Charging","Charging"
payment_gateway,payment_id,payment_method = "","",""
# Global Variables Declaration ends  here

"""
Function Name: create_json_payload
Input Args   : Null
Return       : Null
Description  : This APi will create jason paylod for post method for
               station order
"""
def create_json_payload():
    global payload,payment_gateway,payment_method,retension_cost,late_fees,energy_slot,slot_number
    URL = "http://localhost:3002/api/v1/order/station"
    payload={
                "gps_geolocation": [
                  18.9888,
                  73.4332
                ],
                "order_id": "1c6614161259641c1b765a2f71e9527c",
                 "slot_id": "slot123",
                 "charging_id": "123213sdsdLT33224YC33",
                 "station_id": "station01",
                 "customer_id": "cust01",
                 "slot_no": 1,
                 "payment_method": payment_method,
                 "payment_gateway": payment_gateway,
                 "payment_id": "132sdfs324dsafsfdsf",
                 "charging_start_time_epoch": "2022-03-19T11:34:00.000Z",
                 "charging_stop_time_epoch": "2022-03-19T14:34:00.000Z",
                 "charging_delta_time_epoch": 3,
                 "start_soc": 49,
                 "stop_soc": 79,
                 "delta_soc": 10,
                 "acc_charge_totalizer": energy_slot,
                 "acc_charge_totalizer_unit": "KWh",
                 "charging_total_amount": final_payment,
                 "charging_total_unit": "INR",
                 "charging_battery_retention_cost": retension_cost,
                 "charging_Late_Fees": late_fees,
            }
    result = requests.post(url=URL,data=payload)
    print("Status code: ", result.status_code)

"""
Function Name: get_data_for_selcted_slot
Input Args   : Null
Return       : Null
Description  : This APi will fetch data from the localhost which is running
               in docker container and fetch into json format and store data into
               variables
"""
def get_data_for_selcted_slot():
    global soc1,soh,slot1_status_flag,get_cust_id
    result = requests.get('http://localhost:3001/api/v1/telemetry/bsu')
    response = result.json()
    json_dump = json.dumps(response)
    dict_json = json.loads(json_dump)
    soc1 = dict_json['bsuTelemetrys'][0]['Pack SoC']
    get_cust_id = dict_json['bsuTelemetrys'][0]['Customer ID']

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

        self.soc = soc
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
        global model_taxes
        model_soc_summary.setStringList([self.soc])
        engine_py_to_qml.rootContext().setContextProperty("model_soc_summary", model_soc_summary)
        model_voltage_summary.setStringList(self.voltage)
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

# Get slot 1 summary details thread routine
def get_slot_1_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment
    global discharging_min,thread_1_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc1,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_1_th,slot_number,time_taken_to_charge,calcute_taxes
    close_the_thread()
    thread_1_flag = True
    voltage = random.randint(0,30)
    voltage = round(voltage,2)
    min_temp = random.randint(0,20)
    max_temp = random.randint(0,50)
    imbalance = random.randint(0,70)
    imbalance = round(imbalance/200,2)
    #soh = random.randint(0,90)
    #soh = round(soh,2)
    v_cell_max = random.randint(0,30)
    v_cell_max = round(v_cell_max,2)
    v_cell_min = random.randint(0,40)
    v_cell_min = round(v_cell_min,2)
    v_cell_avg = random.randint(0,20)
    v_cell_avg = round(v_cell_avg,2)
    charging_max = random.randint(-150,0)
    discharging_min = random.randint(0,50)
    c1_temp = random.randint(0,28)
    c2_temp = random.randint(0,28)
    c3_temp = random.randint(0,28)
    c4_temp = random.randint(0,28)
    c5_temp = random.randint(0,28)
    c6_temp = random.randint(0,28)
    c7_temp = random.randint(0,28)
    c8_temp = random.randint(0,28)
    energy_slot = 28.1
    soc_1_temp = 20.0
    time_taken_to_charge = time.strftime("%H:%M", time.gmtime(10000))
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{voltage:.2f}"
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
    C5_TEMP = f"{c5_temp:.1f}\260c"
    C6_TEMP = f"{c6_temp:.1f}\260c"
    C7_TEMP = f"{c7_temp:.1f}\260c"
    C8_TEMP = f"{c8_temp:.1f}\260c"
    SOH = f"{soh}%"
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
    slot1_obj = selected_slot_details(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER,RETENSION_COST,TIME,BOOKED_SLOT_SOC,EST_PAYMET,TAXES)
    slot1_obj.send_data_to_frontend()
    slot_1_th = threading.Timer(4, get_slot_1_data)
    slot_1_th.start()

# Get slot 2 summary details thread routine
def get_slot_2_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_2_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc2,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_2_th,slot_number,time_taken_to_charge
    close_the_thread()
    thread_2_flag = True
    voltage = random.randint(0,30)
    voltage = round(voltage,2)
    min_temp = random.randint(0,20)
    max_temp = random.randint(0,50)
    imbalance = random.randint(0,70)
    imbalance = round(imbalance/200,2)
    soh = random.randint(0,90)
    soh = round(soh,2)
    v_cell_max = random.randint(0,30)
    v_cell_max = round(v_cell_max,2)
    v_cell_min = random.randint(0,40)
    v_cell_min = round(v_cell_min,2)
    v_cell_avg = random.randint(0,20)
    v_cell_avg = round(v_cell_avg,2)
    charging_max = random.randint(-150,0)
    discharging_min = random.randint(0,50)
    c1_temp = random.randint(0,28)
    c2_temp = random.randint(0,28)
    c3_temp = random.randint(0,28)
    c4_temp = random.randint(0,28)
    c5_temp = random.randint(0,28)
    c6_temp = random.randint(0,28)
    c7_temp = random.randint(0,28)
    c8_temp = random.randint(0,28)
    energy_slot = 40.1
    slot_number = "S2"
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{voltage:.2f}"
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
    C5_TEMP = f"{c5_temp:.1f}\260c"
    C6_TEMP = f"{c6_temp:.1f}\260c"
    C7_TEMP = f"{c7_temp:.1f}\260c"
    C8_TEMP = f"{c8_temp:.1f}\260c"
    SOH = f"{soh}%"
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
    close_the_thread()
    thread_3_flag = True
    voltage = random.randint(0,30)
    voltage = round(voltage,2)
    min_temp = random.randint(0,20)
    max_temp = random.randint(0,50)
    imbalance = random.randint(0,70)
    imbalance = round(imbalance/200,2)
    soh = random.randint(0,90)
    soh = round(soh,2)
    v_cell_max = random.randint(0,30)
    v_cell_max = round(v_cell_max,2)
    v_cell_min = random.randint(0,40)
    v_cell_min = round(v_cell_min,2)
    v_cell_avg = random.randint(0,20)
    v_cell_avg = round(v_cell_avg,2)
    charging_max = random.randint(-150,0)
    discharging_min = random.randint(0,50)
    c1_temp = random.randint(0,28)
    c2_temp = random.randint(0,28)
    c3_temp = random.randint(0,28)
    c4_temp = random.randint(0,28)
    c5_temp = random.randint(0,28)
    c6_temp = random.randint(0,28)
    c7_temp = random.randint(0,28)
    c8_temp = random.randint(0,28)
    energy_slot = 30.1
    slot_number = "S3"
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{47.22:.2f}"
    SOC = f"{100:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{13.12:.2f}%"
    V_CELL_MIN = f"min:{3.90:.1f}"
    V_CELL_MAX = f"max:{3.99:.1f}"
    V_CELL_AVG = f"{3.92:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp:.1f}\260c"
    C6_TEMP = f"{c6_temp:.1f}\260c"
    C7_TEMP = f"{c7_temp:.1f}\260c"
    C8_TEMP = f"{c8_temp:.1f}\260c"
    SOH = f"{100}%"
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
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_4_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc4,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_4_th,slot_number,time_taken_to_charge
    close_the_thread()
    thread_4_flag = True
    voltage = random.randint(0,30)
    voltage = round(voltage,2)
    min_temp = random.randint(0,20)
    max_temp = random.randint(0,50)
    imbalance = random.randint(0,70)
    imbalance = round(imbalance/200,2)
    soh = random.randint(0,90)
    soh = round(soh,2)
    v_cell_max = random.randint(0,30)
    v_cell_max = round(v_cell_max,2)
    v_cell_min = random.randint(0,40)
    v_cell_min = round(v_cell_min,2)
    v_cell_avg = random.randint(0,20)
    v_cell_avg = round(v_cell_avg,2)
    charging_max = random.randint(-150,0)
    discharging_min = random.randint(0,50)
    c1_temp = random.randint(0,28)
    c2_temp = random.randint(0,28)
    c3_temp = random.randint(0,28)
    c4_temp = random.randint(0,28)
    c5_temp = random.randint(0,28)
    c6_temp = random.randint(0,28)
    c7_temp = random.randint(0,28)
    c8_temp = random.randint(0,28)
    energy_slot = 20.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{voltage:.2f}"
    SOC = f"{soc4:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp:.1f}\260c"
    C6_TEMP = f"{c6_temp:.1f}\260c"
    C7_TEMP = f"{c7_temp:.1f}\260c"
    C8_TEMP = f"{c8_temp:.1f}\260c"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    SOH = f"{soh}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}Kw"
    FINAL_PAYMENT = f"{final_payment:.2f}"
    EST_PAYMET = f"{est_payment:.2f}"
    TAXES = f"{calcute_taxes:.2f}"
    slot_number = "S4"
    SLOT_NUMBER = f"{slot_number}"
    RETENSION_COST = f"{retension_cost}"
    time_taken_to_charge = time.strftime("%H:%M:%S", time.gmtime(10000))
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
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_5_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc5,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_5_th,slot_number,time_taken_to_charge
    close_the_thread()
    thread_5_flag = True
    voltage += 1.33
    voltage = round(voltage,2)
    min_temp += 2
    max_temp += 1
    imbalance += 1.22
    imbalance += round(imbalance/150,2)
    soh += 1.55
    soh = round(soh,2)
    v_cell_max += 1.22
    v_cell_max = round(v_cell_max,2)
    v_cell_min += 1.66
    v_cell_min = round(v_cell_min,2)
    v_cell_avg  += 1.45
    v_cell_avg = round(v_cell_avg,2)
    charging_max -= 20
    discharging_min += 5
    c1_temp += 0.1
    c2_temp += 0.2
    c3_temp += 0.3
    c4_temp += 0.1
    c5_temp += 0.6
    c6_temp += 0.2
    c7_temp += 0.8
    c8_temp += 0.9
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp:.1f}\260c"
    C6_TEMP = f"{c6_temp:.1f}\260c"
    C7_TEMP = f"{c7_temp:.1f}\260c"
    C8_TEMP = f"{c8_temp:.1f}\260c"
    energy_slot = 50.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    #V = f"{voltage:.2f}"
    #SOC = f"{soc5:.2f}%"
    #MAX_TEMP = f"max:{max_temp:.1f}\260c"
    #MIN_TEMP = f"min:{min_temp:.1f}\260c"
    #IMBALANCE = f"{imbalance:.2f}%"
    #V_CELL_MIN = f"min:{v_cell_min:.1f}"
    #V_CELL_MAX = f"max:{v_cell_max:.1f}"
    #V_CELL_AVG = f"{v_cell_avg:.2f}"
    #C1_TEMP = f"{c1_temp:.1f} {c2_temp:.1f} {c3_temp:.1f} {c4_temp:.1f} {c5_temp:.1f} {c6_temp:.1f} {c7_temp:.1f} {c8_temp:.1f}"
    #SOH = f"{soh}%"
    #CHARGE_MAX = f"{charging_max}A"
    #DISCHARGE_MIN = f"{discharging_min}A"
    V = f"---"
    SOC = f"---%"
    MAX_TEMP = f"max:---"
    MIN_TEMP = f"min:---"
    IMBALANCE = f"---%"
    V_CELL_MIN = f"min:---"
    V_CELL_MAX = f"max:---"
    V_CELL_AVG = f"---"
    SOH = f"---%"
    CHARGE_MAX = f"---A"
    DISCHARGE_MIN = f"---A"
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
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_6_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc6,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_6_th,slot_number,time_taken_to_charge

    close_the_thread()
    thread_6_flag = True
    voltage = random.randint(0,30)
    voltage = round(voltage,2)
    min_temp = random.randint(0,20)
    max_temp = random.randint(0,50)
    imbalance = random.randint(0,70)
    imbalance = round(imbalance/200,2)
    soh = random.randint(0,90)
    soh = round(soh,2)
    v_cell_max = random.randint(0,30)
    v_cell_max = round(v_cell_max,2)
    v_cell_min = random.randint(0,40)
    v_cell_min = round(v_cell_min,2)
    v_cell_avg = random.randint(0,20)
    v_cell_avg = round(v_cell_avg,2)
    charging_max = random.randint(-150,0)
    discharging_min = random.randint(0,50)
    c1_temp = random.randint(0,28)
    c2_temp = random.randint(0,28)
    c3_temp = random.randint(0,28)
    c4_temp = random.randint(0,28)
    c5_temp = random.randint(0,28)
    c6_temp = random.randint(0,28)
    c7_temp = random.randint(0,28)
    c8_temp = random.randint(0,28)
    energy_slot = 25.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{voltage:.2f}"
    SOC = f"{soc6:.2f}%"
    MAX_TEMP = f"max:{max_temp:.1f}\260c"
    MIN_TEMP = f"min:{min_temp:.1f}\260c"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    C1_TEMP = f"{c1_temp:.1f} {c2_temp:.1f} {c3_temp:.1f} {c4_temp:.1f} {c5_temp:.1f} {c6_temp:.1f} {c7_temp:.1f} {c8_temp:.1f}"
    SOH = f"{soh}%"
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
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_7_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc7,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_7_th,slot_number,time_taken_to_charge
    close_the_thread()
    thread_7_flag = True
    voltage = random.randint(0,30)
    voltage = round(voltage,2)
    min_temp = random.randint(0,20)
    max_temp = random.randint(0,50)
    imbalance = random.randint(0,70)
    imbalance = round(imbalance/200,2)
    soh = random.randint(0,90)
    soh = round(soh,2)
    v_cell_max = random.randint(0,30)
    v_cell_max = round(v_cell_max,2)
    v_cell_min = random.randint(0,40)
    v_cell_min = round(v_cell_min,2)
    v_cell_avg = random.randint(0,20)
    v_cell_avg = round(v_cell_avg,2)
    charging_max = random.randint(-150,0)
    discharging_min = random.randint(0,50)
    c1_temp = random.randint(0,28)
    c2_temp = random.randint(0,28)
    c3_temp = random.randint(0,28)
    c4_temp = random.randint(0,28)
    c5_temp = random.randint(0,28)
    c6_temp = random.randint(0,28)
    c7_temp = random.randint(0,28)
    c8_temp = random.randint(0,28)
    energy_slot = 29.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{voltage:.2f}"
    SOC = f"{soc7:.2f}%"
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
    C5_TEMP = f"{c5_temp:.1f}\260c"
    C6_TEMP = f"{c6_temp:.1f}\260c"
    C7_TEMP = f"{c7_temp:.1f}\260c"
    C8_TEMP = f"{c8_temp:.1f}\260c"
    SOH = f"{soh}%"
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
    global voltage,min_temp, max_temp,imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max,est_payment,calcute_taxes
    global discharging_min,thread_8_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc8,retension_cost,booked_slot_soc
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_8_th,slot_number,time_taken_to_charge
    close_the_thread()
    thread_8_flag = True
    voltage = random.randint(0,30)
    voltage = round(voltage,2)
    min_temp = random.randint(0,20)
    max_temp = random.randint(0,50)
    imbalance = random.randint(0,70)
    imbalance = round(imbalance/200,2)
    soh = random.randint(0,90)
    soh = round(soh,2)
    v_cell_max = random.randint(0,30)
    v_cell_max = round(v_cell_max,2)
    v_cell_min = random.randint(0,40)
    v_cell_min = round(v_cell_min,2)
    v_cell_avg = random.randint(0,20)
    v_cell_avg = round(v_cell_avg,2)
    charging_max = random.randint(-150,0)
    discharging_min = random.randint(0,50)
    c1_temp = random.randint(0,28)
    c2_temp = random.randint(0,28)
    c3_temp = random.randint(0,28)
    c4_temp = random.randint(0,28)
    c5_temp = random.randint(0,28)
    c6_temp = random.randint(0,28)
    c7_temp = random.randint(0,28)
    c8_temp = random.randint(0,28)
    energy_slot = 15.1
    est_payment = ((booked_slot_soc*cost_per_unit)+retension_cost+late_fees)
    calcute_taxes = (((est_payment)*18.5)/100)
    final_payment = (est_payment+calcute_taxes)
    V = f"{47.22:.2f}"
    SOC = f"{soc8:.2f}%"
    MAX_TEMP = f"max:{18.5:.1f}\260c"
    MIN_TEMP = f"min:{27.5:.1f}\260c"
    IMBALANCE = f"{13.12:.2f}%"
    V_CELL_MIN = f"min:{3.90:.1f}"
    V_CELL_MAX = f"max:{3.99:.1f}"
    V_CELL_AVG = f"{3.92:.2f}"
    C1_TEMP = f"{c1_temp:.1f}\260c"
    C2_TEMP = f"{c2_temp:.1f}\260c"
    C3_TEMP = f"{c3_temp:.1f}\260c"
    C4_TEMP = f"{c4_temp:.1f}\260c"
    C5_TEMP = f"{c5_temp:.1f}\260c"
    C6_TEMP = f"{c6_temp:.1f}\260c"
    C7_TEMP = f"{c7_temp:.1f}\260c"
    C8_TEMP = f"{c8_temp:.1f}\260c"
    SOH = f"{100}%"
    CHARGE_MAX = f"{-35}A"
    DISCHARGE_MIN = f"{500}A"
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
    global soc1, soc2, soc3, soc4,soc5,soc6,soc7,soc8
    global v1, v2, v3, v4, v5, v6, v7, v8,slot1_status,slot2_status,slot1_status_flag,slot2_status_flag,slot3_status_flag,slot4_status_flag,slot5_status_flag,slot6_status_flag,slot7_status_flag,slot8_status_flag
    global model_slot1_status,model_slot2_status,model_slot3_status,model_slot4_status,model_slot5_status,model_slot6_status,model_slot7_status,model_slot8_status
    global SLOT1_STATUS,SLOT2_STATUS,SLOT3_STATUS,SLOT4_STATUS,SLOT5_STATUS,SLOT6_STATUS,SLOT7_STATUS,SLOT8_STATUS
    soc2 = random.randint(0,25)
    #soc3 = random.randint(0,100)
    soc3  = 100
    soc4 = random.randint(0,30)
    soc5 = random.randint(0,27)
    soc6 = random.randint(0,18)
    soc7 = random.randint(0,20)
    #soc8 = random.randint(0,100)
    soc8  = 100
    v1, v2, v3, v4 = round((soc1/100)*5.88,2), round((soc2/100)*5.88,2), round((soc3/100)*5.88,2), round((soc4/100)*5.88,2)
    v5, v6, v7, v8 = (soc5/100)*5.88, (soc6/100)*5.88, (soc7/100)*5.88, (soc8/100)*5.88
    cost_per_unit = 12
    late_fees = 50
    slot3_status_flag=1
    slot4_status_flag=2
    slot5_status_flag=4
    slot6_status_flag=3
    slot7_status_flag=5
    slot8_status_flag=1

    SOC1 = f"SoC:{soc1:.2f}%"
    SOC2 = f"SoC:{soc2:.2f}%"
    SOC3 = f"SoC:{100:.2f}%"
    SOC4 = f"SoC:{soc4:.2f}%"
    SOC5 = f"SoC:{soc5:.2f}%"
    SOC6 = f"SoC:{soc6:.2f}%"
    SOC7 = f"SoC:{soc7:.2f}%"
    SOC8 = f"SoC:{100:.2f}%"
    V1 = f"         {v1:.2f}V"
    V2 = f"         {v2:.2f}V"
    V3 = f"         {4.92:.2f}V"
    V4 = f"         {v4:.2f}V"
    V5 = f"         {v5:.2f}V"
    V6 = f"         {v6:.2f}V"
    V7 = f"         {v7:.2f}V"
    V8 = f"         {4.94:.2f}V"
    COST = f"{cost_per_unit}"
    LATE_FEES = f"{late_fees}"
    CUST_NAME = f"{get_cust_id}"
    if slot1_status_flag ==2:
        V1,SOC1="",""
    else:
        get_data_for_selcted_slot();
    if slot2_status_flag ==2:
        V2,SOC2="",""
    if slot1_status_flag == 0:
        slot1_status="Charging"
        SLOT1_STATUS=f"{slot1_status}"
        slot1_status_flag=1
    if slot2_status_flag == 0:
        slot2_status="Charging"
        SLOT2_STATUS=f"{slot2_status}"
        slot2_status_flag=1
    if slot3_status_flag == 1:
        slot3_status = "Available"
        SLOT3_STATUS = f"{slot3_status}"
    if slot4_status_flag == 2:
        slot4_status = "Empty"
        SLOT4_STATUS = f"{slot4_status}"
    elif slot4_status_flag == 0:
        model_slot4.setStringList([V4,SOC4])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_4", model_slot4)
    if slot5_status_flag == 4:
        slot5_status="Faulty"
        SLOT5_STATUS=f"{slot5_status}"
    elif slot5_status_flag == 0:
        model_slot5.setStringList([V5,SOC5])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_5", model_slot5)
    if slot6_status_flag == 3:
        slot6_status="Pre Booked"
        SLOT6_STATUS=f"{slot6_status}"
    elif slot6_status_flag == 0:
        model_slot6.setStringList([V6,SOC6])
        engine_py_to_qml.rootContext().setContextProperty("slotModel_6", model_slot6)
    if slot7_status_flag == 5:
        slot7_status = "Discharging"
        SLOT7_STATUS = f"{slot7_status}"
    if slot8_status_flag == 1:
        slot8_status = "Available"
        SLOT8_STATUS = f"{slot8_status}"
    model_slot1.setStringList([V1,SOC1])
    engine_py_to_qml.rootContext().setContextProperty("slotModel_1", model_slot1)
    model_slot2.setStringList([V2,SOC2])
    engine_py_to_qml.rootContext().setContextProperty("slotModel_2", model_slot2)
    model_slot3.setStringList([V3,SOC3])
    engine_py_to_qml.rootContext().setContextProperty("slotModel_3", model_slot3)
    model_slot7.setStringList([V7,SOC7])
    engine_py_to_qml.rootContext().setContextProperty("slotModel_7", model_slot7)
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

    threading.Timer(4, get_data_thread_routine).start()

# Slot class which launch the thread once signal emits from QMl
class catch_slot(QObject):
    @Slot(str)
    def test_slot(self, string):
        global retension_cost,soc1,soc2,soc3,soc4,soc5,soc6,soc7,soc8,booked_slot_soc,booked_slot_flag
        global slot1_status_flag,slot_status,slot2_status_flag,payment_gateway,payment_method
        global slot_status_string,SLOT1_STATUS,SLOT2_STATUS,v1,soc1,slot_1_th,slot_2_th
        if string in "AAAA":
            slot_status_string=string
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc1
                booked_slot_flag=False
            get_slot_1_data()
        elif string in "BBBB":
            slot_status_string=string
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc2
                booked_slot_flag=False
            get_slot_2_data()
        elif string in "CCCC":
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc3
                booked_slot_flag=False
            get_slot_3_data()
        elif string in "DDDD":
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc4
                booked_slot_flag=False
            get_slot_4_data()
        elif string in "EEEE":
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc5
                booked_slot_flag=False
            get_slot_5_data()
        elif string in "FFFF":
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc6
                booked_slot_flag=False
            get_slot_6_data()
        elif string in "GGGG":
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc7
                booked_slot_flag=False
            get_slot_7_data()
        elif string in "HHHH":
            booked_slot_flag=True
            if booked_slot_flag:
                booked_slot_soc=soc8
                booked_slot_flag=False
            get_slot_8_data()
        elif string in "1":
            retension_cost=10
        elif string in "2":
            retension_cost=20
        elif string in "3":
            retension_cost=30
        elif string in "4":
            retension_cost=40
        elif string in "5":
            retension_cost=50
        elif string in "6":
            retension_cost=60
        elif string in "7":
            retension_cost=70
        elif string in "8":
            retension_cost=80
        elif string in "9":
            retension_cost=90
        elif string in "10":
            retension_cost=100
        elif string in "11":
            retension_cost=110
        elif string in "12":
            retension_cost=120
        elif string in "13":
            retension_cost=130
        elif string in "14":
            retension_cost=140
        elif string in "15":
            retension_cost=150
        elif string in "16":
            retension_cost=160
        elif string in "17":
            retension_cost=170
        elif string in "18":
            retension_cost=180
        elif string in "19":
            retension_cost=190
        elif string in "20":
            retension_cost=200
        elif string in "21":
            retension_cost=210
        elif string in "22":
            retension_cost=220
        elif string in "23":
            retension_cost=230
        elif string in "24":
            retension_cost=240
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
            if slot1_status_flag == 1 and slot_status_string == "AAAA":
                slot1_status="Empty"
                SLOT1_STATUS=f"{slot1_status}"
                model_slot1_status.setStringList([SLOT1_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot1_status", model_slot1_status)
                slot1_status_flag=2;
            elif slot2_status_flag == 1 and slot_status_string == "BBBB":
                slot2_status="Empty"
                SLOT2_STATUS=f"{slot2_status}"
                model_slot2_status.setStringList([SLOT2_STATUS])
                engine_py_to_qml.rootContext().setContextProperty("model_slot2_status", model_slot2_status)
                slot2_status_flag=2;

if __name__ == "__main__":
    try:
        app = QGuiApplication(sys.argv)
        engine_py_to_qml = QQmlApplicationEngine()
        catchtheslot = catch_slot()
        engine_qml_to_py = QQmlApplicationEngine()
        engine_py_to_qml.load(QUrl.fromLocalFile('main.qml'))
        engine_qml_to_py.rootContext().setContextProperty("catch_slot", catch_slot)
        # Below line is to connect the signal(comming from QML) to respective slot which is define in python file
        engine_py_to_qml.rootObjects()[0].test_signal.connect(catchtheslot.test_slot, type=Qt.ConnectionType.QueuedConnection)
        get_data_thread_routine()
        if not engine_py_to_qml.rootObjects():
            sys.exit(-1)
        sys.exit(app.exec_())
    except:
        print("Error in main code")
