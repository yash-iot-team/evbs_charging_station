import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : payment_summarypage
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("Payment")
    signal test_signal(string input_string)
    Rectangle {
        width: 770
        height: 300
        x:15;y:15
        radius:5
        color: "#DDDDDD"
        Text {
            id : payment_summary
            x:15;y:15
            font.pixelSize: 30
            color:"black"
            font.family: "montserrat"
            font.bold: true
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Payment Summary")
        }
        Rectangle {
            id:total
            width:200
            height:100
            color: "#DDDDDD"
            x: 550;y:15
            Text {
                anchors.fill : horizontalAlignment
                font.family: "montserrat"
                font.bold: true
                font.pixelSize: 45
                anchors.centerIn: total.horizontalCenter
                x:55;y:2
                text: qsTr("Total")
            }
            TableView {
                id: summary_total
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.margins: 50
                anchors.leftMargin: 90
                model : model_final_payment
                delegate: Rectangle {
                    id : total_payment
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr_symbol.png"
                width:20
                height:30
                x:70;y:60
            }
        }

        Rectangle {
            id: horizontal_line_top
            x:15;y:60
            radius: 5
            visible: currentIndex == index;
            width: 400;    height: 5
            color: 'black'
        }
        Rectangle {
            id : parent_soc
            width:350
            height:50
            x:10;y:70
            color:"#DDDDDD"
            Text {
                id : soc
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("SoC")
            }
            TableView {
                id: summary_soc
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 260
                model : model_soc_summary
                delegate: Rectangle {
                    id : datasoc
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
        }
        Rectangle {
            id : parent_late_fees
            width:350
            height:50
            x:10;y:110
            color:"#DDDDDD"
            Text {
                id : late_fees
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Late Fees")
            }
            TableView {
                id: summary_latefees
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 270
                model : model_late_fees
                delegate: Rectangle {
                    id : latefees
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr_symbol.png"
                width:20
                height:30
                x:255;y:10
            }
        }
        Rectangle {
            id : parent_cost
            width:350
            height:50
            x:10;y:160
            color:"#DDDDDD"
            Text {
                id : cost_per_unit
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Cost Per Unit")
            }
            TableView {
                id: summary_cost
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 270
                model : model_cost_per_unit
                delegate: Rectangle {
                    id : cost
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr_symbol.png"
                width:20
                height:30
                x:255;y:10
            }

        }
        Rectangle {
            id: horizontal_line_bottom
            x:10;y:220
            radius: 5
            visible: currentIndex == index;
            width: 400;    height: 5
            color: 'black'
        }
        Rectangle {
            id: note
            width:750
            height:50
            x:10; y:240
            color : "#DDDDDD"
            Text {
                x:2;y:30
                font.pixelSize: 12
                color:"black"
                font.family: "montserrat"
                text: qsTr("Note:You have to return purchsed battery within choosen time frame. In case of failure to retrun late fees will be charged as per the policy ")
            }
        }
    }

    Text {
        x:15;y:340
        id: buttonLabel
        font.pixelSize: 25
        color : "white"
        font.bold : true
        font.family: "montserrat"
        text: "Payment Methods"
    }
    RoundButton {
        id : upi
        width: 125
        height: 50
        x:15;y:380
        palette {
            button: "#00bfff"
        }
        Text {
            id: upi_method
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: upi
            text: "UPI"
        }
        onClicked:{
            var component = Qt.createComponent("upi_payment.qml")
            var upi_payment_window    = component.createObject()
            upi_payment_window.show()
        }
    }
    RoundButton {
        id : crypto
        width: 125
        height: 50
        x:155;y:380
        palette {
            button: "#00bfff"
        }
        Text {
            id: crypto_method
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: crypto
            text: "Crypto"
        }
    }
    RoundButton {
        id : card
        width: 125
        height: 50
        x:295;y:380
        palette {
            button: "#00bfff"
        }
        Text {
            id: card_method
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: card
            text: "Card"
        }
    }
    RoundButton {
        id : netbanking
        width: 125
        height: 50
        x:435;y:380
        palette {
            button: "#00bfff"
        }
        Text {
            id: netbanking_method
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: netbanking
            text: "Banking"
        }
    }
}
