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
    property int counter:0
    property int index:0
    property bool timer_flag:True
    Rectangle {
        id:payment
        width: 650
        height: 450
        x:15;y:15
        radius:5
        color: "#DDDDDD"
        AnimatedImage {
            id: sprite
            width:160;height:150
            x:250;y:300
            source: "load.gif"
        }
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
            source: "qr.png"
            width:200
            height:200
            x:230;y:90
        }
        Timer {
            interval: 800; running: true; repeat: true
            onTriggered:
            {
                counter += 1
                if (counter == 10)
                {

                    var component = Qt.createComponent("remove_bsu.qml")
                    var remove_bsu_window    = component.createObject()
                    remove_bsu_window.show()
                    upi_payment.close();
                    payment_summarypage.close();
                    book_summarypage.close()
                    test_signal("proceed")
                    if(slot_1.slot_1_flag){
                        slot_1.isGreen = !slot_1.isGreen ;
                        slot_1.slot_1_flag=0
                    }
                    if(slot_2.slot_2_flag){
                        slot_2.isGreensl2 = !slot_2.isGreensl2;
                        slot_2.slot_2_flag=0
                    }
                }
            }
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
