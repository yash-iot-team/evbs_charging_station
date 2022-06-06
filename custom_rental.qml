import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.4

Window {
    id : custom_rentalboook
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("Custom Rental")
    Rectangle {
        width: 650
        height: 450
        x:15;y:15
        radius:5
        color: "#DDDDDD"
        Rectangle {
            id : cutom_retension
            width:240
            height:100
            x:20;y:50
            property string custom_retension_cost : ""
            property string custom_retension_hrs : ""
            property string custom_retension_min : ""
            color:"#DDDDDD"
            Text {
                x:2;y:2
                id: hours_cust
                font.pixelSize: 20
                font.bold:true
                font.family: "montserrat"
                anchors.centerIn: hours_cust
                text: "Hours"
            }
            SpinBox {
                id: control
                value: 0
                editable: true
                x:2;y:30
                background: Rectangle {
                    implicitWidth: 180
                    implicitHeight: 50
                    color: "#99e401"
                    border.color: "black"
                }
                contentItem: TextInput  {
                    text: control.textFromValue(control.value, control.locale)
                    color: "white"
                    font.bold: true
                    selectedTextColor: "#ffffff"
                    horizontalAlignment: Qt.AlignHCenter
                    verticalAlignment: Qt.AlignVCenter
                    readOnly: !control.editable
                    validator: control.validator
                    inputMethodHints: Qt.ImhFormattedNumbersOnly
                    onTextChanged: {
                        cutom_retension.custom_retension_min = text
                    }
                }
                up.indicator: Rectangle {
                    x: control.mirrored ? 0 : parent.width - width
                    height: parent.height
                    implicitWidth: 40
                    implicitHeight: 40
                    color: "#29293d"
                    border.color: "black"
                    Text {
                        text: "+"
                        font.pixelSize: control.font.pixelSize * 2
                        color: "white"
                        anchors.fill: parent
                        fontSizeMode: Text.Fit
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
                down.indicator: Rectangle {
                    x: control.mirrored ? parent.width - width : 0
                    height: parent.height
                    implicitWidth: 40
                    implicitHeight: 40
                    color: "#29293d"
                    border.color: "black"
                    Text {
                        text: "-"
                        font.pixelSize: control.font.pixelSize * 2
                        color: "white"
                        anchors.fill: parent
                        fontSizeMode: Text.Fit
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }
        }
        Rectangle {
            id : cutom_days
            width:240
            height:100
            x:20;y:160
            color:"#DDDDDD"
            Text {
                x:2;y:2
                id: days_cust
                font.pixelSize: 20
                font.bold:true
                font.family: "montserrat"
                anchors.centerIn: days_cust
                text: "Days"
            }
            SpinBox {
                id: control_days
                value: 0
                editable: true
                x:2;y:30
                background: Rectangle {
                    implicitWidth: 180
                    implicitHeight: 50
                    color: "#99e401"
                    border.color: "black"
                }
                contentItem: TextInput  {
                    text: control_days.textFromValue(control_days.value, control_days.locale)
                    color: "white"
                    font.bold: true
                    selectedTextColor: "#ffffff"
                    horizontalAlignment: Qt.AlignHCenter
                    verticalAlignment: Qt.AlignVCenter
                    readOnly: !control.editable
                    validator: control.validator
                    inputMethodHints: Qt.ImhFormattedNumbersOnly
                    onTextChanged: {
                        cutom_retension.custom_retension_hrs = text
                    }
                }
                up.indicator: Rectangle {
                    x: control.mirrored ? 0 : parent.width - width
                    height: parent.height
                    implicitWidth: 40
                    implicitHeight: 40
                    color: "#29293d"
                    border.color: "black"
                    Text {
                        text: "+"
                        font.pixelSize: control.font.pixelSize * 2
                        color: "white"
                        anchors.fill: parent
                        fontSizeMode: Text.Fit
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
                down.indicator: Rectangle {
                    x: control_days.mirrored ? parent.width - width : 0
                    height: parent.height
                    implicitWidth: 40
                    implicitHeight: 40
                    color: "#29293d"
                    border.color: "black"
                    Text {
                        text: "-"
                        font.pixelSize: control_days.font.pixelSize * 2
                        color: "white"
                        anchors.fill: parent
                        fontSizeMode: Text.Fit
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }
        }
        RoundButton {
            id : back
            width: 125
            height: 50
            x:655;y:5
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
                onClicked: custom_rentalboook.close();
            }
        }
        RoundButton {
            id : confirm
            width: 125
            height: 50
            x:655;y:70
            palette {
                button: "#00bfff"
            }
            Text {
                id: timelineconfirm
                font.pixelSize: 20
                font.family: "montserrat"
                anchors.centerIn: confirm
                text: "Confirm"
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    test_customsignal(cutom_retension.custom_retension_hrs,cutom_retension.custom_retension_min)
                }
            }
        }
    }
}
