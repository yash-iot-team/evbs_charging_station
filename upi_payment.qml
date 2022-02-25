import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : upi_payment
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("UPI Payment")
    Rectangle {
        width: 650
        height: 450
        x:15;y:15
        radius:5
        color: "#DDDDDD"
        Rectangle {
            id:text_to_instruct
            width:300
            height:70
            x:180;y:10
            color: "#DDDDDD"
            Text {
                x:55;y:5
                id: text1
                font.pixelSize: 20
                font.family: "montserrat"
                text: "Scan this QR code"
            }
            Text {
                x:30;y:35
                id: text2
                font.pixelSize: 20
                font.family: "montserrat"
                text: "UPI ID: helloworld@okicici"
            }
        }
        Image {
            source: "qr_code.png"
            width:200
            height:200
            x:230;y:100
        }
    }
    RoundButton {
        id : back
        width: 125
        height: 50
        x:670;y:15
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
            onClicked: upi_payment.close();
        }
    }
}
