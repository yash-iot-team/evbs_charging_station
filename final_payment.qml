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
    Rectangle {
        id:total
        width:160
        height:100
        radius:4
        color: "#99e401"
        x: 630;y:10
        Text {
            anchors.fill : horizontalAlignment
            font.family: "montserrat"
            font.bold: true
            font.pixelSize: 35
            anchors.centerIn: total.horizontalCenter
            x:35;y:2
            text: qsTr("Total")
        }
        TableView {
            id: summary_total
            anchors.fill: parent
            topMargin: header.implicitHeight
            anchors.margins: 50
            anchors.leftMargin: 68
            model : model_final_payment
            delegate: Rectangle {
                id : total_payment
                implicitHeight: 50
                implicitWidth: 50
                color: "transparent"
                x:30;y:20
                Text {
                     anchors.centerIn: parent
                     font.pixelSize: 23
                     text: model.display
                 }
            }
        }
        Image {
            source: "inr1.png"
            width:25
            height:30
            x:20;y:60
        }
    }
    Rectangle {
        width: 200
        height:100
        color:"transparent"
        x:5;y:15
        Text {
            anchors.fill : horizontalAlignment
            font.family: "montserrat"
            font.bold: true
            font.pixelSize: 35
            anchors.centerIn: total.horizontalCenter
            x:5;y:2
            color:"white"
            text: qsTr("Payment Methods")
        }
    }
    Rectangle {
        id:upi_payment_methods
        width:650
        height:170
        x:5;y:120
        color:"transparent"
        Text {
            x:2;y:2
            color:"white"
            font.bold: true
            text: qsTr("UPI Methods")
            font.pixelSize: 25
        }
        Rectangle {
            id:google_pay
            x:2;y:40
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: gpay
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: google_pay
                text: "Google Pay"
                color:"white"
            }
            MouseArea {
                id:gpay_mousearea
                anchors.fill: parent
                onClicked: {
                    google_pay.isGreen = !google_pay.isGreen
                    test_signal("googlepay")
                }
            }
            states: State {
                name: "brighter"; when: gpay_mousearea.pressed
                PropertyChanges { target: google_pay; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id:amazon_pay
            x:160;y:40
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: apay
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: amazon_pay
                text: "Amazon Pay"
                color:"white"
            }
            MouseArea {
                id:amazonpay_mousearea
                anchors.fill: parent
                onClicked: {
                    amazon_pay.isGreen = !amazon_pay.isGreen
                    test_signal("amazonpay")
                }
            }
            states: State {
                name: "brighter"; when: amazonpay_mousearea.pressed
                PropertyChanges { target: amazon_pay; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id:bharat_pay
            x:320;y:40
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: bpay
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: bharat_pay
                text: "Bharat Pay"
                color:"white"
            }
            MouseArea {
                id:bharatpay_mousearea
                anchors.fill: parent
                onClicked: {
                    bharat_pay.isGreen = !bharat_pay.isGreen
                    test_signal("bharatpay")
                }
            }
            states: State {
                name: "brighter"; when: bharatpay_mousearea.pressed
                PropertyChanges { target: bharat_pay; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id:bhim_upi
            x:480;y:40
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: bhimupi
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: bhim_upi
                text: "BHIM UPI"
                color:"white"
            }
            MouseArea {
                id:bhimpay_mousearea
                anchors.fill: parent
                onClicked: {
                    bhim_upi.isGreen = !bhim_upi.isGreen
                }
            }
            states: State {
                name: "brighter"; when: bhimpay_mousearea.pressed
                PropertyChanges { target: bhim_upi; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id:paytm_pay
            x:2;y:110
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: ppay
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: paytm_pay
                text: "Paytm"
                color:"white"
            }
            MouseArea {
                id:paytmpay_mousearea
                anchors.fill: parent
                onClicked: {
                    paytm_pay.isGreen = !paytm_pay.isGreen
                }
            }
            states: State {
                name: "brighter"; when: paytmpay_mousearea.pressed
                PropertyChanges { target: paytm_pay; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id:airtel_pay
            x:160;y:110
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: airtelpay
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: airtel_pay
                text: "Airtel"
                color:"white"
            }
            MouseArea {
                id:airtelpay_mousearea
                anchors.fill: parent
                onClicked: {
                    airtel_pay.isGreen = !airtel_pay.isGreen
                }
            }
            states: State {
                name: "brighter"; when: airtelpay_mousearea.pressed
                PropertyChanges { target: airtel_pay; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id:cred_pay
            x:320;y:110
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: cpay
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: cred_pay
                text: "Cred"
                color:"white"
            }
            MouseArea {
                id:credpay_mousearea
                anchors.fill: parent
                onClicked: {
                    cred_pay.isGreen = !cred_pay.isGreen
                }
            }
            states: State {
                name: "brighter"; when: credpay_mousearea.pressed
                PropertyChanges { target: cred_pay; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id:phone_pay
            x:480;y:110
            width:150
            height:50
            radius:5
            property bool isGreen: true
            color: isGreen ? "#00bfff" : "#145214"
            Text {
                id: phonepay
                font.pixelSize: 20
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: phone_pay
                text: "Phone Pay"
                color:"white"
            }
            MouseArea {
                id:phonepay_mousearea
                anchors.fill: parent
                onClicked: {
                    phone_pay.isGreen = !phone_pay.isGreen
                }
            }
            states: State {
                name: "brighter"; when: phonepay_mousearea.pressed
                PropertyChanges { target: phone_pay; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }

    }
    RoundButton {
        id : proceed
        width: 125
        height: 50
        x:10;y:330
        palette {
            button: "#00bfff"
        }
        Text {
            id: next_page
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: proceed
            text: "Proceed"
        }
        onClicked:{
            var component = Qt.createComponent("upi_payment.qml")
            var upi_payment_window    = component.createObject()
            upi_payment_window.show()

        }
    }
    RoundButton {
        id : back
        width: 125
        height: 50
        x:150;y:330
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
            onClicked: payment_summarypage.close();
        }
    }
}
