import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1

Window {
    id:evbs_dashboard
    width: 800
    height: 480
    visible: true
    title: qsTr("EVBS Dashboard")
    Rectangle {
        id:main_frame
        width: 800
        height: 480
        color: "#020537"

        Rectangle {
            id:slot_1
            width: 190
            height: 90
            x:3;y:280
            radius: 5
            property int slot_1_flag: 0
            border.color: "black"
            border.width: 2
            property string s1_status
            state: slot_1.s1_status

            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_1; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_1; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_1; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_1; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_1; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_1; color: "orange"}
                }
            ]
            Text {
                id: slot_1_Text
                x:10;y:20
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("S1")
                color: "white"
                font.pixelSize: 25
                font.family: "montserrat"
                font.bold: true
            }
            TableView {
                id: tableview
                anchors.fill: parent
                clip: true
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_1
                delegate: Rectangle {
                    id : slot1_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.horizontalCenter: parent
                        font.bold: true
                        font.pixelSize: 14
                        color:"white"
                        font.family: "montserrat"
                        text: model.display

                     }
                }
            }
            TableView {
                id: slot_status
                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 90
                model : model_slot1_status
                delegate: Rectangle {
                    id : slot1_status_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:5
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 16
                        color:"white"
                        font.family: "montserrat"
                        text: slot_1.s1_status
                        Component.onCompleted: {
                            slot_1.s1_status = model.display
                        }
                     }
                }
            }
            MouseArea {
                id:mouseArea
                anchors.fill: parent

                onClicked: {
                    slot_1.slot_1_flag=1;
                    test_signal("AAAA")
                }
            }
            transitions: Transition {
                ColorAnimation { duration: 300 }
            }
        }
        Rectangle {
            id:slot_2
            width: 190
            height: 90
            x:205;y:280
            radius: 5
            property int slot_2_flag: 0
            border.color: "black"
            border.width: 2
            property string s2_status
            state: slot_2.s2_status
            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_2; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_2; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_2; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_2; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_2; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_2; color: "orange"}
                }
            ]
            Text {
                id: slot_2_Text
                x:10;y:20
                text: qsTr("S2")
                color: "white"
                font.pixelSize: 25
                font.bold: true
                font.family: "montserrat"
                anchors.horizontalCenter:  parent.Left
            }
            TableView {
                id: view_2
                anchors.fill: parent
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_2
                delegate: Rectangle {
                    id : slot2_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 14
                        color:"white"
                        font.family: "montserrat"
                        text: model.display
                     }
                   }
                }
                TableView {
                    id: slot_2_status
                    anchors.fill: parent
                    anchors.topMargin: 10
                    anchors.leftMargin: 90
                    model : model_slot2_status
                    delegate: Rectangle {
                        id : slot2_status_delegate
                        implicitHeight: 30
                        implicitWidth: 30
                        color: "transparent"
                        x:30;y:5
                        Text {
                            anchors.fill: parent
                            font.bold: true
                            font.pixelSize: 16
                            color:"white"
                            font.family: "montserrat"
                            text: slot_2.s2_status
                            Component.onCompleted: {
                                slot_2.s2_status = model.display
                            }
                         }
                    }
                }
                MouseArea {
                    id:mouseArea_slot_2
                    anchors.fill: parent
                    onClicked: {
                        slot_2.slot_2_flag=1;
                        test_signal("BBBB")
                    }
                }
                transitions: Transition {
                    ColorAnimation { duration: 300 }
                }
        }
        Rectangle {
            id:slot_3
            width: 190
            height: 90
            x:405;y:280
            radius: 5
            border.color: "black"
            border.width: 2
            property int slot_3_flag: 0
            property string s3_status
            state: slot_3.s3_status
            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_3; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_3; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_3; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_3; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_3; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_3; color: "orange"}
                }
            ]
            Text {
                id: slot_3_Text
                x:10;y:20
                text: qsTr("S3")
                color: "white"
                font.pixelSize: 25
                font.bold: true
                font.family: "montserrat"
                anchors.horizontalCenter:  parent.Left
            }
            TableView {
                id: view_3
                anchors.fill: parent
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_3
                delegate: Rectangle {
                    id : slot3_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.horizontalCenter: parent
                        font.bold: true
                        font.pixelSize: 14
                        font.family: "montserrat"
                        color:"white"
                        text: model.display
                     }
                   }
                }
            TableView {
                id: slot_3_status
                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 90
                model : model_slot3_status
                delegate: Rectangle {
                    id : slot3_status_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:5
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 16
                        color:"white"
                        font.family: "montserrat"
                        text: slot_3.s3_status
                        Component.onCompleted: {
                            slot_3.s3_status = model.display
                        }
                     }
                }
            }
            MouseArea {
                id:mouseArea_slot_3
                anchors.fill: parent
                onClicked: {
                    slot_3.slot_3_flag=1
                    test_signal("CCCC")
                }
            }
            transitions: Transition {
                ColorAnimation { duration: 300 }
            }
        }
        Rectangle {
            id:slot_4
            width: 190
            height: 90
            x:605;y:280
            radius: 5
            border.color: "black"
            border.width: 2
            property string s4_status
            property int slot_4_flag: 0
            state: slot_4.s4_status
            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_4; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_4; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_4; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_4; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_4; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_4; color: "orange"}
                }
            ]
            Text {
                id: slot_4_Text
                x:10;y:20
                text: qsTr("S4")
                color: "white"
                font.pixelSize: 25
                font.family: "montserrat"
                font.bold: true
                 anchors.horizontalCenter:  parent.Left
            }
            TableView {
                id: view_4
                anchors.fill: parent
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_4
                delegate: Rectangle {
                    id : slot4_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.horizontalCenter: parent
                        font.bold: true
                        font.pixelSize: 14
                        font.family: "montserrat"
                        color:"white"
                        text: model.display
                     }
                }
            }
            TableView {
                id: slot_4_status
                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 90
                model : model_slot4_status
                delegate: Rectangle {
                    id : slot4_status_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:5
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 16
                        color:"white"
                        font.family: "montserrat"
                        text: slot_4.s4_status
                        Component.onCompleted: {
                            slot_4.s4_status = model.display
                        }
                    }
                }
            }
            MouseArea {
                id:mouseArea_slot_4
                anchors.fill: parent
                onClicked: {
                    slot_4.slot_4_flag=1
                    test_signal("DDDD")
                }
            }
            transitions: Transition {
                ColorAnimation { duration: 300 }
            }
        }
        Rectangle {
            id:slot_5
            width: 190
            height: 90
            x:5;y:380
            radius: 5
            border.color: "black"
            border.width: 2
            property string s5_status
            property int slot_5_flag: 0
            state: slot_5.s5_status
            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_5; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_5; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_5; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_5; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_5; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_5; color: "orange"}
                }
            ]

            Text {
                id: slot_5_Text
                x:10;y:20
                text: qsTr("S5")
                color: "white"
                font.pixelSize: 25
                font.family: "montserrat"
                font.bold: true
                 anchors.horizontalCenter:  parent.Left
            }
            TableView {
                id: view_5
                anchors.fill: parent
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_5
                delegate: Rectangle {
                    id : slot5_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.horizontalCenter: parent
                        font.bold: true
                        font.pixelSize: 14
                        font.family: "montserrat"
                        color:"white"
                        text: model.display
                     }
                }
            }
            TableView {
                id: slot_5_status
                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 90
                model : model_slot5_status
                delegate: Rectangle {
                    id : slot5_status_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:5
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 16
                        color:"white"
                        font.family: "montserrat"
                        text: slot_5.s5_status
                        Component.onCompleted: {
                            slot_5.s5_status = model.display
                        }
                    }
                }
            }
            MouseArea {
                id:mouseArea_slot_5
                anchors.fill: parent
                onClicked: {
                    slot_5.slot_5_flag =1
                    test_signal("EEEE")
                }
            }
            transitions: Transition {
                ColorAnimation { duration: 300 }
            }
        }
        Rectangle {
            id:slot_6
            width: 190
            height: 90
            x:205;y:380
            radius: 5
            border.color: "black"
            border.width: 2
            property string s6_status
            property int slot_6_flag: 0
            state: slot_6.s6_status
            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_6; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_6; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_6; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_6; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_6; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_6; color: "orange"}
                }
            ]

            Text {
                id: slot_6_Text
                x:10;y:20
                text: qsTr("S6")
                color: "white"
                font.pixelSize: 25
                font.family: "montserrat"
                font.bold: true
                 anchors.horizontalCenter:  parent.Left
            }
            TableView {
                id: view_6
                anchors.fill: parent
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_6
                delegate: Rectangle {
                    id : slot6_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.horizontalCenter: parent
                        font.bold: true
                        font.pixelSize: 14
                        font.family: "montserrat"
                        color:"white"
                        text: model.display
                     }
                }
            }
            TableView {
                id: slot_6_status
                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 90
                model : model_slot6_status
                delegate: Rectangle {
                    id : slot6_status_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:5
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 16
                        color:"white"
                        font.family: "montserrat"
                        text: slot_6.s6_status
                        Component.onCompleted: {
                            slot_6.s6_status = model.display
                        }
                    }
                }
            }
            MouseArea {
                id:mouseArea_slot_6
                anchors.fill: parent
                propagateComposedEvents : False
                onClicked: {
                    slot_6.slot_6_flag=1
                    test_signal("FFFF")
                }
            }
            transitions: Transition {
                ColorAnimation { duration: 300 }
            }
        }
        Rectangle {
            id:slot_7
            width: 190
            height: 90
            x:405;y:380
            radius: 5
            border.color: "black"
            border.width: 2
            property string s7_status
            property int slot_7_flag: 0
            state: slot_7.s7_status
            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_7; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_7; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_7; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_7; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_7; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_7; color: "orange"}
                }
            ]

            Text {
                id: slot_7_Text
                x:10;y:20
                text: qsTr("S7")
                color: "white"
                font.pixelSize: 25
                font.family: "montserrat"
                font.bold: true
                 anchors.horizontalCenter:  parent.Left
            }
            TableView {
                id: view_7
                anchors.fill: parent
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_7
                delegate: Rectangle {
                    id : slot7_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 14
                        font.family: "montserrat"
                        color:"white"
                        text: model.display
                     }
                }
            }
            TableView {
                id: slot_7_status
                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 90
                model : model_slot7_status
                delegate: Rectangle {
                    id : slot7_status_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:5
                    Text {
                        anchors.horizontalCenter: parent
                        font.bold: true
                        font.pixelSize: 16
                        color:"white"
                        font.family: "montserrat"
                        text: slot_7.s7_status
                        Component.onCompleted: {
                            slot_7.s7_status = model.display
                        }                     }
                }
            }
            MouseArea {
                id:mouseArea_slot_7
                anchors.fill: parent
                onClicked: {
                    slot_7.slot_7_flag=1
                    test_signal("GGGG")
                }
            }
            transitions: Transition {
                ColorAnimation { duration: 300 }
            }
        }
        Rectangle {
            id:slot_8
            width: 190
            height: 90
            x:605;y:380
            radius: 5
            border.color: "black"
            border.width: 2
            property string s8_status
            property int slot_8_flag: 0
            state: slot_8.s8_status
            states: [
                State {
                    name: "Empty"
                    PropertyChanges { target: slot_8; color: "#29293d"}
                },
                State {
                    name: "Charging"
                    PropertyChanges { target: slot_8; color: "#99e401"}
                },
                State {
                    name: "Fault"
                    PropertyChanges { target: slot_8; color: "red"}
                },
                State {
                    name: "Prebooked"
                    PropertyChanges { target: slot_8; color: "grey"}
                },
                State {
                    name: "Available"
                    PropertyChanges { target: slot_8; color: "#004d00"}
                },
                State {
                    name: "Discharging"
                    PropertyChanges { target: slot_8; color: "orange"}
                }
            ]

            Text {
                id: slot_8_Text
                x:10;y:20
                text: qsTr("S8")
                color: "white"
                font.pixelSize: 25
                font.bold: true
                 anchors.horizontalCenter:  parent.Left
            }
            TableView {
                id: view_8

                anchors.fill: parent
                anchors.topMargin: 38
                anchors.leftMargin: 80
                model : slotModel_8
                delegate: Rectangle {
                    id : slot8_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.horizontalCenter: parent
                        font.bold: true
                        font.pixelSize: 14
                        color:"white"
                        text: model.display
                     }
                }
            }
            TableView {
                id: slot_8_status
                anchors.fill: parent
                anchors.topMargin: 10
                anchors.leftMargin: 90
                model : model_slot8_status
                delegate: Rectangle {
                    id : slot8_status_delegate
                    implicitHeight: 30
                    implicitWidth: 30
                    color: "transparent"
                    x:30;y:5
                    Text {
                        anchors.fill: parent
                        font.bold: true
                        font.pixelSize: 16
                        color:"white"
                        font.family: "montserrat"
                        text: slot_8.s8_status
                        Component.onCompleted: {
                            slot_8.s8_status = model.display
                        }
                    }
                }
            }
            MouseArea {
                id:mouseArea_slot_8
                anchors.fill: parent
                onClicked: {
                    slot_8.slot_8_flag=1
                    test_signal("HHHH")
                }
            }
            transitions: Transition {
                ColorAnimation { duration: 300 }
            }
        }

        Rectangle {
            id:slot_summmary
            width: 790
            height: 270
            x:5;y:10
            color: "#020537"
            RoundButton  {
                id: book
                width: 225
                height: 50
                x:5;y:140
                radius: 5
                palette {
                    button: "#00bfff"
                }
                Text {
                    id: buttonLabel
                    font.pixelSize: 15
                    font.family: "montserrat"
                    anchors.centerIn: book
                    text: "Book"
                }
                onClicked:{
                   var component1 = Qt.createComponent("book_summary.qml")
                   var book_summary_window    = component1.createObject()
                   book_summary_window.show()
                }
            }
            RoundButton  {
                id: slot_details
                width: 225
                height: 50
                radius: 5
                palette {
                    button: "#00bfff"
                }
                x:5;y:205
                Text {
                    id: slot_details_lable
                    font.pixelSize: 15
                    font.family: "montserrat"
                    anchors.centerIn: slot_details
                    text: "Details"
                }
                onClicked:{
                    var component = Qt.createComponent("selected_slot_details.qml")
                    var slot_detial_window    = component.createObject()
                    slot_detial_window.show()
                }
            }
            Rectangle {
                id:customer
                width:800
                height:25
                x:5;y:0
                radius: 5
                color: "#020537"
                Image {
                    source: "wifi.png"
                    width:30
                    height:30
                    x:740;y:1
                }
                Text {
                    x:2;y:1
                    id: welcome
                    anchors.centerIn: parent.verticalCenter
                    font.family: "montserrat"
                    font.bold: true
                    text: qsTr("Welcome")
                    color: "white"
                    font.pixelSize: 20
                }
                TableView {
                    id: customer_name_get
                    anchors.fill: parent
                    anchors.leftMargin: 140
                    model : model_customer_name
                    delegate: Rectangle {
                        id : cust_name
                        implicitHeight: 25
                        implicitWidth: 25
                        color: "transparent"
                        Text {
                            anchors.centerIn: parent
                            font.bold: true
                            font.pixelSize: 20
                            font.family: "montserrat"
                            color:"white"
                            text: model.display
                         }
                    }
                }
            }

            Rectangle {
                id : selected_slot
                width:110
                height:90
                x:5;y:35
                color: "#00bfff"
                radius: 5
                TableView {
                    id: selected_slot_view
                    anchors.fill: parent
                    anchors.margins: 15
                    anchors.leftMargin: 30
                    model : model_selected_slot
                    delegate: Rectangle {
                        id : selected_slot_delegate
                        implicitHeight: 50
                        implicitWidth: 50
                        color: "transparent"
                        x:30;y:20
                        Text {
                            anchors.centerIn: parent
                            font.bold: true
                            font.pixelSize: 40
                            font.family: "montserrat"
                            color:"black"
                            text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_voltage
                width:100
                height:90
                x:130;y:35
                color: "#29293d"
                radius:5
                Text {
                    id: voltage
                    x:45;y:8
                    anchors.centerIn: parent.verticalCenter
                    text: qsTr("V")
                    color: "white"
                    font.family: "montserrat"
                    font.pixelSize: 16
                }
                TableView {
                    id: summary_voltage
                    anchors.fill: parent
                    topMargin: header.implicitHeight
                    anchors.margins: 45
                    anchors.leftMargin: 22
                    model : model_voltage_summary
                    delegate: Rectangle {
                        id : datavoltage
                        implicitHeight: 50
                        implicitWidth: 50
                        color: "transparent"
                        x:30;y:20
                        Text {
                             anchors.centerIn: parent
                             font.bold: true
                             font.pixelSize: 18
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_soc
                width:100
                height:90
                x:240;y:35
                color: "#29293d"
                radius:5
                Text {
                    id: soc
                    x:35;y:8
                    anchors.centerIn: parent.verticalCenter
                    text: qsTr("SoC")
                    color: "white"
                    font.family: "montserrat"
                    font.pixelSize: 16
                }
                TableView {
                    id: summary_soc
                    anchors.fill: parent
                    topMargin: header.implicitHeight
                    anchors.margins: 45
                    anchors.leftMargin: 25
                    model : model_soc_summary
                    delegate: Rectangle {
                        id : datasoc
                        implicitHeight: 50
                        implicitWidth: 50
                        color: "transparent"
                        x:30;y:20
                        Text {
                             anchors.centerIn: parent
                             font.bold: true
                             font.pixelSize: 18
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_Temp
                width:100
                height:90
                x:350;y:35
                color: "#29293d"
                radius:5
                Text {
                    id: temp
                    x:25;y:8
                    anchors.centerIn: parent.verticalCenter
                    font.family: "montserrat"
                    text: qsTr("Temp")
                    color: "white"
                    font.pixelSize: 14
                }
                TableView {
                    id: summary_temp
                    anchors.fill: parent
                    anchors.margins: 30
                    anchors.leftMargin: 35
                    model : model_temp_summary
                    delegate: Rectangle {
                        id : datatemp
                        implicitHeight: 25
                        implicitWidth: 25
                        color: "transparent"
                        x:30;y:20
                        Text {
                             anchors.centerIn: parent
                             font.pixelSize: 14
                             font.bold: true
                             font.family: "montserrat"
                             color:"white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_imbalance
                width:100
                height:90
                x:460;y:35
                color: "#29293d"
                radius: 5
                Text {
                    id: imbalance
                    x:20;y:8
                    anchors.centerIn: parent.verticalCenter
                    font.family: "montserrat"
                    text: qsTr("Imbalance")
                    color: "white"
                    font.pixelSize: 14
                }
                TableView {
                    id: summary_imbalance
                    anchors.fill: parent
                    anchors.margins: 45
                    anchors.leftMargin: 25
                    model : model_imbalance_summary
                    delegate: Rectangle {
                        id : dataimbalance
                        implicitHeight: 50
                        implicitWidth: 50
                        color: "transparent"
                        x:30;y:20
                        Text {
                             anchors.centerIn: parent
                             font.bold: true
                             font.pixelSize: 14
                             font.family: "montserrat"
                             color: "white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_charging_max
                width:100
                height:90
                x:570;y:35
                color: "#29293d"
                radius: 5
                Text {
                    id: chargemax
                    x:15;y:8
                    anchors.centerIn: parent.verticalCenter
                    text: qsTr("Charge Max")
                    color: "white"
                    font.family: "montserrat"
                    font.pixelSize: 14
                }
                TableView {
                    id: summary_chargingmax
                    anchors.fill: parent
                    anchors.margins: 45
                    anchors.leftMargin:20
                    model : model_charging_max
                    rowSpacing: 1
                    columnSpacing: 1
                    delegate: Rectangle {
                        id : datafrompy
                        implicitHeight: 50
                        implicitWidth: 50
                        color: "transparent"
                        x:30;y:20
                        Text {
                             anchors.centerIn: parent
                             font.bold: true
                             font.pixelSize: 14
                             font.family: "montserrat"
                             color: "white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_discharging_min
                width:100
                height:90
                x:680;y:35
                color: "#29293d"
                radius: 5
                Text {
                    id: dischargemin
                    x:7;y:8
                    text: qsTr("Discharge Max")
                    color: "white"
                    font.family: "montserrat"
                    font.pixelSize: 14
                }
                TableView {
                    id: summary_dischargingmax
                    anchors.fill: parent
                    anchors.margins: 45
                    anchors.leftMargin:20
                    model : model_discharging_min
                    rowSpacing: 1
                    columnSpacing: 1
                    delegate: Rectangle {
                        id : dischargemax
                        implicitHeight: 50
                        implicitWidth: 50
                        color: "transparent"
                        x:30;y:20
                        Text {
                             anchors.centerIn: parent
                             font.bold: true
                             font.pixelSize: 14
                             font.family: "montserrat"
                             color: "white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_soh
                width:100
                height:120
                x:240;y:140
                color: "#29293d"
                radius: 5
                Text {
                    id: soh
                    x:25;y:8
                    anchors.centerIn: parent.verticalCenter
                    text: qsTr("  SoH")
                    color: "white"
                    font.pixelSize: 16
                    font.family: "montserrat"
                }
                TableView {
                    id: summary_soh
                    anchors.fill: parent
                    anchors.margins: 70
                    anchors.leftMargin: 25
                    model : model_soh_summary
                    delegate: Rectangle {
                        id : dissoh
                        implicitHeight: 50
                        implicitWidth: 50
                        color: "transparent"
                        Text {
                             anchors.centerIn: parent
                             font.bold: true
                             font.pixelSize: 18
                             font.family: "montserrat"
                             color: "white"
                             text: model.display
                         }
                    }
                }
            }
            Rectangle {
                id: slot_v_cell
                width:100
                height:120
                x:350;y:140
                color: "#29293d"
                radius: 5
                Text {
                    id: vcell
                    x:30;y:8
                    anchors.centerIn: parent.verticalCenter
                    text: qsTr("   V\n CELL")
                    color: "white"
                    font.family: "montserrat"
                    font.pixelSize: 14
                }
                TableView {
                    id: summary_v_cell
                    anchors.fill: parent
                    anchors.margins: 46
                    anchors.leftMargin: 35
                    rowSpacing: 2
                    columnSpacing: 2
                    model : model_v_cell_summary
                    delegate: Rectangle {
                        id : datavcell
                        implicitHeight: 25
                        implicitWidth: 25
                        color: "transparent"
                        x:30;y:20
                        Text {
                             anchors.centerIn: parent
                             font.pixelSize: 14
                             font.bold: true
                             font.family: "montserrat"
                             color: "white"
                             text: model.display
                         }
                    }

                }
            }
            Rectangle {
                id: slot_v_cell_avg
                width:100
                height:120
                x:460;y:140
                color: "#29293d"
                radius: 5
                Text {
                    id: vcellavg
                    x:15;y:8
                    anchors.centerIn: parent.verticalCenter
                    text: qsTr("       V \n CELL AVG")
                    color: "white"
                    font.pixelSize: 14
                    font.family: "montserrat"
                }
                TableView {
                    id: summary_v_cell_avg
                    anchors.fill: parent
                    anchors.margins: 80
                    anchors.leftMargin: 35
                    anchors.centerIn: parent.verticalCenter
                    model : model_v_cell_avg_summary
                    delegate: Rectangle {
                        id : v_Cel_avg
                        implicitHeight: 35
                        implicitWidth: 35
                        color: "transparent"
                       Text {
                            anchors.centerIn: parent
                            font.bold: true
                            font.pixelSize: 18
                            color: "white"
                            text: model.display
                        }
                    }
                }
            }

            Rectangle {
                id: slot_v_m_temp_sensor
                width:210
                height:120
                x:570;y:140
                color: "#020537"
                Text {
                    id: module_temp
                    x:30;y:8
                    anchors.centerIn: parent.verticalCenter
                    text: qsTr("Module Temp Sensor")
                    color: "white"
                    font.pixelSize: 16
                }
                TableView {
                    id: summary_mod_tem_sensor_1
                    anchors.fill: parent
                    anchors.margins: 40
                    anchors.leftMargin: 5
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell1_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module
                        color: "#e62e00"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
                TableView {
                    id: summary_mod_tem_sensor_2
                    anchors.fill: parent
                    anchors.margins: 40
                    anchors.leftMargin: 55
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell2_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module_2
                        color: "#29293d"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
                TableView {
                    id: summary_mod_tem_sensor_3
                    anchors.fill: parent
                    anchors.margins: 40
                    anchors.leftMargin: 105
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell3_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module_3
                        color: "#29293d"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
                TableView {
                    id: summary_mod_tem_sensor_4
                    anchors.fill: parent
                    anchors.margins: 40
                    anchors.leftMargin: 155
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell4_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module_4
                        color: "#29293d"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
                TableView {
                    id: summary_mod_tem_sensor_5
                    anchors.fill: parent
                    anchors.margins: 80
                    anchors.leftMargin: 5
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell5_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module_5
                        color: "#29293d"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
                TableView {
                    id: summary_mod_tem_sensor_6
                    anchors.fill: parent
                    anchors.margins: 80
                    anchors.leftMargin: 55
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell6_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module_6
                        color: "#29293d"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
                TableView {
                    id: summary_mod_tem_sensor_7
                    anchors.fill: parent
                    anchors.margins: 80
                    anchors.leftMargin: 105
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell7_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module_7
                        color: "#29293d"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
                TableView {
                    id: summary_mod_tem_sensor_8
                    anchors.fill: parent
                    anchors.margins: 80
                    anchors.leftMargin: 155
                    anchors.centerIn: parent.horizontalCenter
                    model : model_cell8_temp_sensor
                    delegate: Rectangle {
                        id : temp_send_module_8
                        color: "#29293d"
                        radius : 5
                        implicitHeight: 30
                        implicitWidth: 45
                        Text {
                            anchors.centerIn: parent
                            font.pixelSize: 12
                            font.bold: true
                            color: "white"
                            text: model.display
                       }
                    }
                }
            }
        }
    }
}
