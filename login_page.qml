import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id:welcome_main
    width: 800
    height: 480
    visible: true
    title: qsTr("Welcome to the station")
    property int counter:0
    property int load_main_dash_board:0
    signal test_signal(string input_string)
    Rectangle {
        id:main_frame
        width: 800
        height: 480
        color: "#020537"
        Image {
            source: "rfid.png"
            width:400
            height:250
            x:200;y:60
        }
        Text {
            id: message_Text
            x:180;y:330
            text: qsTr("Hi, Welcome Do swipe your card!!!")
            color: "white"
            font.pixelSize: 25
            font.bold: true
            font.family: "montserrat"
            anchors.horizontalCenter:  parent.Left
        }
        Timer {
            interval: 800; running: true; repeat: true
            onTriggered:
            {
                counter += 1

                if (counter == 5)
                {
                   var component = Qt.createComponent("evbs_dashboard.qml")
                   var evbs_dashboard_window    = component.createObject()
                   evbs_dashboard_window.show()
                }
            }
        }
    }

}
