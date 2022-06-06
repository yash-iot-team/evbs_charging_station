import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : selected_slot_summarypage
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("Battery and BMS Details")
    Rectangle {
        width: 655
        height: 450
        x:15;y:15
        radius:5
        color: "#DDDDDD"
        Rectangle {
            id : bsudetails
            width: 320
            height:440
            x:5;y:5
            radius:5
            color: "#DDDDDD"
            Rectangle {
                width:320
                height:30
                color:"#00bfff"
                Text
                {
                    id:bdetials
                    x:5
                    font.pixelSize:18
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "BSU Details"
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#29293d"
                y:40
                Text
                {
                    id:bsumanname
                    x:5
                    font.pixelSize:16
                    color:"white"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Alias Name"
                }
                TableView {
                    id: manname
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_bsu_man_name
                    delegate: Rectangle {
                        id : bsu_man_name
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }

            Rectangle {
                width:320
                height:30
                color:"#DDDDDD"
                y:80
                Text
                {
                    id:bsuid
                    x:5
                    font.pixelSize:16
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "BSU ID"
                }
                TableView {
                    id: bsu_id
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_bsu_id
                    delegate: Rectangle {
                        id : displaybsuid
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:2
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"black"
                             text: model.display
                         }
                    }
                }
            }

            Rectangle {
                width:320
                height:30
                color:"#29293d"
                y:120
                Text
                {
                    id:slotno
                    x:5
                    font.pixelSize:16
                    color:"white"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Slot Number"
                }
                TableView {
                    id: slot_no
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_selected_slot
                    delegate: Rectangle {
                        id : displayslotno
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:2
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#DDDDDD"
                y:160
                Text
                {
                    id:bsustate
                    x:5
                    font.pixelSize:16
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "BSU Status"
                }
                TableView {
                    id: bsustatus
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_bsu_state
                    delegate: Rectangle {
                        id : displaybsustatus
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:2
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"black"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#29293d"
                y:200
                Text
                {
                    id:bsu_mode
                    x:5
                    font.pixelSize:16
                    color:"white"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "BSU Mode"
                }
                TableView {
                    id: bsumode
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_bsu_mode
                    delegate: Rectangle {
                        id : displaybsumode
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:2
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#DDDDDD"
                y:240
                Text
                {
                    id:orderstatus
                    x:5
                    font.pixelSize:16
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: orderdetials
                    text: "Order Status"
                }
                TableView {
                    id: order_status
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_order_status
                    delegate: Rectangle {
                        id : orderstatusdetais
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:2
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"black"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#29293d"
                y:280
                Text
                {
                    id:inservice
                    x:5
                    font.pixelSize:16
                    color:"white"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Service Hrs"
                }
                TableView {
                    id: inservicehrs
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_inservice_hrs
                    delegate: Rectangle {
                        id : inserve_hrs
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:2
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#DDDDDD"
                y:320
                Text
                {
                    id:packid
                    x:5
                    font.pixelSize:16
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "PackID"
                }
                TableView {
                    id: batterypackid
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_batterypack_id
                    delegate: Rectangle {
                        id : battery_pid
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:2
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"black"
                             text: model.display
                         }
                    }
                }
            }
        }
        Rectangle {
            id : bmsdetials
            width: 320
            height:440
            x:330;y:5
            radius:5
            color: "#DDDDDD"
            Rectangle {
                width:320
                height:30
                color:"#00bfff"
                Text
                {
                    id:badetials
                    x:5;y:2
                    font.pixelSize:18
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: badetials
                    text: "Battery Details"
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#29293d"
                y:40
                Text
                {
                    id:manufacturername
                    x:5
                    font.pixelSize:16
                    color:"white"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Manufacturer"
                }
                TableView {
                    id: manufacturer
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_battery_man_name
                    delegate: Rectangle {
                        id : battery_man_name
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#DDDDDD"
                y:80
                Text
                {
                    id:packcapacity
                    x:5
                    font.pixelSize:16
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Pack Capacity"
                }
                TableView {
                    id: bpackcapacity
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_battery_capacity
                    delegate: Rectangle {
                        id : bpack_capacity
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"black"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#29293d"
                y:120
                Text
                {
                    id:packchemistry
                    x:5
                    font.pixelSize:16
                    color:"white"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Chemistry"
                }
                TableView {
                    id: chemistry
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_battery_chemistry
                    delegate: Rectangle {
                        id : pack_chemistry
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#DDDDDD"
                y:160
                Text
                {
                    id:packconfig
                    x:5
                    font.pixelSize:16
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Configuration"
                }
                TableView {
                    id: packConfiguration
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_battery_config
                    delegate: Rectangle {
                        id : bpack_configuration
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"black"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#29293d"
                y:200
                Text
                {
                    id:cells
                    x:5
                    font.pixelSize:16
                    color:"white"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Cells"
                }
                TableView {
                    id: noofcells
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_battery_cells
                    delegate: Rectangle {
                        id : no_cells
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                width:320
                height:30
                color:"#DDDDDD"
                y:240
                Text
                {
                    id:modelno
                    x:5
                    font.pixelSize:16
                    color:"black"
                    font.family: "montserrat"
                    font.bold:true
                    anchors.centerIn: bdetials
                    text: "Model Number"
                }
                TableView {
                    id: modelnumber
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_battery_model
                    delegate: Rectangle {
                        id : model_no
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30
                        Text {
                             anchors.fill: parent
                             font.pixelSize: 16
                             color:"black"
                             text: model.display
                         }
                    }
                }
            }
        }
    }
    RoundButton {
        id : back
        width: 120
        height: 50
        x:675;y:15
        palette {
            button: "#00bfff"
        }
        Text {
            id: buttonLabel
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: back
            text: "Back"
        }
        MouseArea {
            anchors.fill: parent
            onClicked: selected_slot_summarypage.close();
        }
    }
    /*RoundButton {
        id : trend
        width: 120
        height: 50
        x:675;y:80
        palette {
            button: "#00bfff"
        }
        Text {
            id: next_page
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: trend
            text: "Trend"
        }
    }*/
}
