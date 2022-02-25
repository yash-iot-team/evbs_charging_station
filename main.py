import sys
from PySide2 import *
from PySide2.QtCore import QUrl, QStringListModel, QObject,Signal, Property,Slot, Qt
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
import time
import threading
import random


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
cost_per_unit,energy_slot,late_fees,final_payment = 0,0,0,0
soc1,soc2,soc3,soc4,soc5,soc6,soc7,soc8 = 0,0,0,0,0,0,0,0
v1,v2,v3,v4,v5,v6,v7,v8 = 0,0,0,0,0,0,0,0
c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp = 0,0,0,0,0,0,0,0
voltage,min_temp,max_temp,imbalance,soh,v_cell_min,v_cell_max = 0,0,0,0,0,0,0
v_cell_avg, charging_max, discharging_min, slot_number = 0,0,0,0
thread_1_flag, thread_2_flag, thread_3_flag, thread_4_flag,thread_5_flag, thread_6_flag, thread_7_flag, thread_8_flag = False, False, False, False, False, False, False, False
slot_1_th,slot_2_th,slot_3_th,slot_4_th,slot_5_th,slot_6_th,slot_7_th,slot_8_th = 0,0,0,0,0,0,0,0
# Global Variables Declaration ends  here

class selected_slot_detials:
    def __init__(self,soc,voltage,min_temp,max_temp,imbalance,soh,v_cell_min,v_cell_max,v_cell_avg,
    charging_max,discharging_min, c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,
    energy_slot, final_payment, slot_number):

        self.soc = soc
        self.voltage            = voltage
        self.min_temp           = min_temp
        self.max_temp           = max_temp
        self.imbalance          = imbalance
        self.soh                = soh
        self.v_cell_min         = v_cell_min
        self.v_cell_max         = v_cell_max
        self.v_cell_avg         = v_cell_avg
        self.charging_max       = charging_max
        self.discharging_min    = discharging_min
        self.c1_temp            = c1_temp
        self.c2_temp            = c2_temp
        self.c3_temp            = c3_temp
        self.c4_temp            = c4_temp
        self.c5_temp            = c5_temp
        self.c6_temp            = c6_temp
        self.c7_temp            = c7_temp
        self.c8_temp            = c8_temp
        self.energy_slot        = energy_slot
        self.final_payment      = final_payment
        self.slot_number        = slot_number

    def send_data_to_frontend(self):
        global model_soc_summary, model_voltage_summary, model_temp_summary, model_imbalance_summary, model_soh_summary
        global model_v_cell_avg_summary, model_v_cell_summary,model_cell1_temp_sensor,model_cell2_temp_sensor
        global model_cell1_temp_sensor,model_cell2_temp_sensor,model_cell3_temp_sensor,model_cell4_temp_sensor,model_cell5_temp_sensor,model_cell6_temp_sensor,model_cell7_temp_sensor,model_cell8_temp_sensor
        global model_module_tem_sensor_summary, model_selected_slot,model_final_payment
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
        model_final_payment.setStringList([self.final_payment])
        engine_py_to_qml.rootContext().setContextProperty("model_final_payment", model_final_payment)
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


#Thread routine closing Function
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
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_1_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc1
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_1_th,slot_number

    close_the_thread()
    thread_1_flag = True
    voltage += 0.44
    voltage = round(voltage,2)
    min_temp += 0.1
    max_temp += 0.2
    imbalance += 1.33
    imbalance += round(imbalance/200,2)
    soh += 1.55
    soh = round(soh,2)
    v_cell_max += 0.22
    v_cell_max = round(v_cell_max,2)
    v_cell_min += 0.33
    v_cell_min = round(v_cell_min,2)
    v_cell_avg  += 0.55
    v_cell_avg = round(v_cell_avg,2)
    charging_max -= 2
    discharging_min += 2
    c1_temp += 0.1
    c2_temp += 0.2
    c3_temp += 0.3
    c4_temp += 0.4
    c5_temp += 0.5
    c6_temp += 0.6
    c7_temp += 0.7
    c8_temp += 0.8
    energy_slot += 0.1
    final_payment = ((soc1*cost_per_unit)+late_fees)
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
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    slot1_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot1_obj.send_data_to_frontend()
    slot_1_th = threading.Timer(4, get_slot_1_data)
    slot_1_th.start()

# Get slot 2 summary details thread routine
def get_slot_2_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_2_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc2
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_2_th,slot_number

    close_the_thread()
    thread_2_flag = True
    voltage += 0.33
    voltage = round(voltage,2)
    min_temp += 2
    max_temp += 1
    imbalance += 0.44
    imbalance += round(imbalance/150,2)
    soh += 0.55
    soh = round(soh,2)
    v_cell_max += 0.22
    v_cell_max = round(v_cell_max,2)
    v_cell_min += 0.66
    v_cell_min = round(v_cell_min,2)
    v_cell_avg  += 0.45
    v_cell_avg = round(v_cell_avg,2)
    charging_max -= 3
    discharging_min += 3
    c1_temp += 0.1
    c2_temp += 0.2
    c3_temp += 0.3
    c4_temp += 0.1
    c5_temp += 0.6
    c6_temp += 0.2
    c7_temp += 0.8
    c8_temp += 0.9
    energy_slot += 0.1
    slot_number = "S2"
    final_payment = ((soc2*cost_per_unit)+late_fees)
    V = f"{voltage:.2f}"
    SOC = f"{soc2:.2f}%"
    MAX_TEMP = f"max:{max_temp}"
    MIN_TEMP = f"min:{min_temp}"
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
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    SLOT_NUMBER = f"{slot_number}"
    slot2_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot2_obj.send_data_to_frontend()
    slot_2_th = threading.Timer(4, get_slot_2_data)
    slot_2_th.start()

# Get slot 3 summary details thread routine
def get_slot_3_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_3_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc3
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_3_th,slot_number
    close_the_thread()
    thread_3_flag = True
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
    c1_temp = 27.8
    c2_temp = 26.6
    c3_temp = 26.1
    c4_temp = 26.9
    c5_temp = 27.4
    c6_temp = 26.7
    c7_temp = 25.9
    c8_temp = 19.5
    energy_slot += 0.1
    slot_number = "S3"
    final_payment = ((soc3*cost_per_unit)+late_fees)
    V = f"{47.22:.2f}"
    SOC = f"{100:.2f}%"
    MAX_TEMP = f"max:{18.5}"
    MIN_TEMP = f"min:{27.8}"
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
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    SLOT_NUMBER = f"{slot_number}"
    slot3_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot3_obj.send_data_to_frontend()
    slot_3_th = threading.Timer(4, get_slot_3_data)
    slot_3_th.start()

# Get slot 4 summary details thread routine
def get_slot_4_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_4_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc4
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_4_th,slot_number

    close_the_thread()
    thread_4_flag = True
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
    c1_temp += 1.1
    c2_temp += 1.2
    c3_temp += 1.3
    c4_temp += 1.1
    c5_temp += 1.6
    c6_temp += 1.2
    c7_temp += 1.8
    c8_temp += 1.9
    energy_slot += 0.1
    final_payment = ((soc4*cost_per_unit)+late_fees)
    V = f"{voltage:.2f}"
    SOC = f"{soc4:.2f}%"
    MAX_TEMP = f"max:{max_temp}"
    MIN_TEMP = f"min:{min_temp}"
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
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    slot_number = "S4"
    SLOT_NUMBER = f"{slot_number}"
    slot4_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot4_obj.send_data_to_frontend()
    slot_4_th = threading.Timer(4, get_slot_4_data)
    slot_4_th.start()

# Get slot 5 summary details thread routine
def get_slot_5_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_5_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc5
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_5_th,slot_number
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
    energy_slot += 0.1
    final_payment = ((soc5*cost_per_unit)+late_fees)
    #V = f"{voltage:.2f}"
    #SOC = f"{soc5:.2f}%"
    #MAX_TEMP = f"max:{max_temp}"
    #MIN_TEMP = f"min:{min_temp}"
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
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    slot_number = "S5"
    SLOT_NUMBER = f"{slot_number}"
    slot5_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot5_obj.send_data_to_frontend()
    slot_5_th = threading.Timer(4, get_slot_5_data)
    slot_5_th.start()

# Get slot 6 summary details thread routine
def get_slot_6_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_6_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc6
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_6_th,slot_number

    close_the_thread()
    thread_6_flag = True
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
    c1_temp += 1.1
    c2_temp += 1.2
    c3_temp += 1.3
    c4_temp += 1.1
    c5_temp += 1.6
    c6_temp += 1.2
    c7_temp += 1.8
    c8_temp += 1.9
    energy_slot += 0.1
    final_payment = ((soc6*cost_per_unit)+late_fees)
    V = f"{voltage:.2f}"
    SOC = f"{soc6:.2f}%"
    MAX_TEMP = f"max:{max_temp}"
    MIN_TEMP = f"min:{min_temp}"
    IMBALANCE = f"{imbalance:.2f}%"
    V_CELL_MIN = f"min:{v_cell_min:.1f}"
    V_CELL_MAX = f"max:{v_cell_max:.1f}"
    V_CELL_AVG = f"{v_cell_avg:.2f}"
    C1_TEMP = f"{c1_temp:.1f} {c2_temp:.1f} {c3_temp:.1f} {c4_temp:.1f} {c5_temp:.1f} {c6_temp:.1f} {c7_temp:.1f} {c8_temp:.1f}"
    SOH = f"{soh}%"
    CHARGE_MAX = f"{charging_max}A"
    DISCHARGE_MIN = f"{discharging_min}A"
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    slot_number = "S6"
    SLOT_NUMBER = f"{slot_number}"
    slot6_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot6_obj.send_data_to_frontend()
    slot_6_th = threading.Timer(4, get_slot_6_data)
    slot_6_th.start()

# Get slot 7 summary details thread routine
def get_slot_7_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_7_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc7
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_7_th,slot_number

    close_the_thread()
    thread_7_flag = True
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
    energy_slot += 0.1
    final_payment = ((soc7*cost_per_unit)+late_fees)
    V = f"{voltage:.2f}"
    SOC = f"{soc7:.2f}%"
    MAX_TEMP = f"max:{max_temp}"
    MIN_TEMP = f"min:{min_temp}"
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
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    slot_number = "S7"
    SLOT_NUMBER = f"{slot_number}"
    slot7_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot7_obj.send_data_to_frontend()
    slot_7_th = threading.Timer(4, get_slot_7_data)
    slot_7_th.start()

# Get slot 8 summary details thread routine
def get_slot_8_data():
    global voltage,min_temp, max_temp, imbalance, soh, v_cell_min, v_cell_max, v_cell_avg,charging_max
    global discharging_min,thread_8_flag,energy_slot,final_payment,late_fees,cost_per_unit,soc8
    global c1_temp,c2_temp,c3_temp,c4_temp,c5_temp,c6_temp,c7_temp,c8_temp,slot_8_th,slot_number

    close_the_thread()
    thread_8_flag = True
    voltage += 2.33
    voltage = round(voltage,2)
    min_temp += 2
    max_temp += 1
    imbalance += 1.22
    imbalance += round(imbalance/150,2)
    soh += 3.55
    soh = round(soh,2)
    v_cell_max += 1.22
    v_cell_max = round(v_cell_max,2)
    v_cell_min += 1.66
    v_cell_min = round(v_cell_min,2)
    v_cell_avg  += 1.45
    v_cell_avg = round(v_cell_avg,2)
    charging_max -= 40
    discharging_min += 5
    c1_temp = 27.8
    c2_temp = 26.6
    c3_temp = 26.1
    c4_temp = 26.9
    c5_temp = 27.4
    c6_temp = 26.7
    c7_temp = 25.9
    c8_temp = 19.5
    energy_slot += 0.1
    final_payment = ((soc8*cost_per_unit)+late_fees)
    V = f"{47.22:.2f}"
    SOC = f"{100:.2f}%"
    MAX_TEMP = f"max:{18.5}"
    MIN_TEMP = f"min:{27.8}"
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
    ENERGY = f"{energy_slot:.1f}KWh"
    FINAL_PAYMENT = f"{final_payment}"
    slot_number = "S8"
    SLOT_NUMBER = f"{slot_number}"
    slot8_obj = selected_slot_detials(SOC,V,MAX_TEMP,MIN_TEMP,IMBALANCE,SOH,V_CELL_MIN,V_CELL_MAX,
    V_CELL_AVG, CHARGE_MAX,DISCHARGE_MIN,C1_TEMP,C2_TEMP,C3_TEMP,C4_TEMP,C5_TEMP,C6_TEMP,C7_TEMP,
    C8_TEMP, ENERGY,FINAL_PAYMENT, SLOT_NUMBER)
    slot8_obj.send_data_to_frontend()
    slot_8_th = threading.Timer(4, get_slot_8_data)
    slot_8_th.start()

# Available Slots information thread routine
def get_data_thread_routine():
    global model_slot1, model_slot2, model_slot3, model_slot4,model_slot4
    global model_slot5,model_slot6,model_slot7,model_slot8,model_cost_per_unit,model_late_fees
    global model_uniqueID,cost_per_unit,late_fees
    global soc1, soc2, soc3, soc4,soc5,soc6,soc7,soc8
    global v1, v2, v3, v4, v5, v6, v7, v8

    soc1 = random.randint(0,100)
    soc2 = random.randint(0,50)
    soc3 = random.randint(0,60)
    soc4 = random.randint(0,70)
    soc5 = random.randint(0,40)
    soc6 = random.randint(0,90)
    soc7 = random.randint(0,80)
    soc8 = random.randint(0,100)
    v1, v2, v3, v4 = round((soc1/100)*5.88,2), round((soc2/100)*5.88,2), round((soc3/100)*5.88,2), round((soc4/100)*5.88,2)
    v5, v6, v7, v8 = (soc5/100)*5.88, (soc6/100)*5.88, (soc7/100)*5.88, (soc8/100)*5.88
    cost_per_unit = 50
    late_fees = 50
    SOC1 = f"SoC:{soc1:.2f}%"
    SOC2 = f"SoC:{soc2:.2f}%"
    SOC3 = f"SoC:{100:.2f}%"
    SOC4 = f"SoC:{soc4:.2f}%"
    #SOC5 = f"SoC:{soc5:.2f}%"
    SOC5 = f"SoC:---%"
    SOC6 = f"SoC:{soc6:.2f}%"
    SOC7 = f"SoC:{soc7:.2f}%"
    SOC8 = f"SoC:{100:.2f}%"
    V1 = f"         {v1:.2f}V"
    V2 = f"         {v2:.2f}V"
    V3 = f"         {4.92:.2f}V"
    V4 = f"         {v4:.2f}V"
    #V5 = f"         {v5:.2f}V"
    V5 = f"        --- V"
    V6 = f"         {v6:.2f}V"
    V7 = f"         {v7:.2f}V"
    V8 = f"         {4.94:.2f}V"
    COST = f"{cost_per_unit}"
    LATE_FEES = f"{late_fees}"
    model_slot1.setStringList([V1, SOC1])
    model_slot2.setStringList([V2, SOC2])
    model_slot3.setStringList([V3, SOC3])
    #model_slot4.setStringList([V4, SOC4])
    model_slot5.setStringList([V5, SOC5])
    model_slot6.setStringList([V6, SOC6])
    model_slot7.setStringList([V7, SOC7])
    model_slot8.setStringList([V8, SOC8])
    model_cost_per_unit.setStringList([COST])
    model_late_fees.setStringList([LATE_FEES])
    engine_py_to_qml.rootContext().setContextProperty("slotModel_1", model_slot1)
    engine_py_to_qml.rootContext().setContextProperty("slotModel_2", model_slot2)
    engine_py_to_qml.rootContext().setContextProperty("slotModel_3", model_slot3)
    #engine_py_to_qml.rootContext().setContextProperty("slotModel_4", model_slot4)
    engine_py_to_qml.rootContext().setContextProperty("slotModel_5", model_slot5)
    engine_py_to_qml.rootContext().setContextProperty("slotModel_6", model_slot6)
    engine_py_to_qml.rootContext().setContextProperty("slotModel_7", model_slot7)
    engine_py_to_qml.rootContext().setContextProperty("slotModel_8", model_slot8)
    engine_py_to_qml.rootContext().setContextProperty("model_cost_per_unit", model_cost_per_unit)
    engine_py_to_qml.rootContext().setContextProperty("model_late_fees", model_late_fees)
    threading.Timer(4, get_data_thread_routine).start()

# Slot class which launch the thread once signal emits from QMl
class catch_slot(QObject):
    @Slot(str)
    def test_slot(self, string):
        if string in "AAAA":
            print("#######You are in slot_1 catch")
            get_slot_1_data()
        elif string in "BBBB":
            print("#######You are in slot_2 catch")
            get_slot_2_data()
        elif string in "CCCC":
            print("#######You are in slot_3 catch")
            get_slot_3_data()
        elif string in "DDDD":
            print("#######You are in slot_4 catch")
            get_slot_4_data()
        elif string in "EEEE":
            print("#######You are in slot_5 catch")
            get_slot_5_data()
        elif string in "FFFF":
            print("#######You are in slot_6 catch")
            get_slot_6_data()
        elif string in "GGGG":
            print("#######You are in slot_7 catch")
            get_slot_7_data()
        elif string in "HHHH":
            print("#######You are in slot_8 catch")
            get_slot_8_data()

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine_py_to_qml = QQmlApplicationEngine()
    catchtheslot = catch_slot()
    engine_qml_to_py = QQmlApplicationEngine()
    engine_py_to_qml.load(QUrl.fromLocalFile('main.qml'))
    engine_qml_to_py.rootContext().setContextProperty("catch_slot", catch_slot)
    if not engine_py_to_qml.rootObjects():
        sys.exit(-1)
    # Below line is to connect the signal(comming from QML) to respective slot which is define in python file
    engine_py_to_qml.rootObjects()[0].test_signal.connect(catchtheslot.test_slot, type=Qt.ConnectionType.QueuedConnection)
    get_data_thread_routine()
    sys.exit(app.exec_())

