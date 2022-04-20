import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id:access_granted
    width: 800
    height: 480
    visible: true
    title: qsTr("Access Granted")
    property int counter:0
    signal test_signal(string input_string)
    Rectangle {
        id:main_frame
        width: 800
        height: 480
        color: "#020537"
        AnimatedImage {
            id: sprite
            anchors.centerIn: parent
            source: "yes.gif"
            width:800
            height:480
        }
        Timer {
            interval: 800; running: true; repeat: true
            onTriggered:
            {
                counter += 1

                if (counter == 1)
                {
                    stackview.push("evbs_main_dashboard.qml")
                    access_granted.close()
                }
            }
        }
    }
}
