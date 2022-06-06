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
    property int access_flag:1
    signal test_signal(string input_string)
    signal test_customsignal(string hrs_str,string  min_str)
    signal test_retension_timeline(int hrs)

    StackView {
        id: stackview
        initialItem: welcome_main
    }
    Rectangle {
        id:main_frame
        width: 800
        height: 480
        color: "#020537"
        AnimatedImage {
            id: sprite
            anchors.centerIn: parent
            source: "rfid.gif"
            width:800
            height:480
        }
        Timer {
            interval: 800; running: true; repeat: true
            onTriggered:
            {
                counter += 1

                if (counter == 2)
                {
                    if (access_flag)
                    {
                        var component = Qt.createComponent("accessgranted.qml")
                        var access_window    = component.createObject()
                        access_window.show()
                    }
                    else
                    {
                        var component1 = Qt.createComponent("accessdenied.qml")
                        var accessdenied_window    = component1.createObject()
                        accessdenied_window.show()
                    }
                }
            }
        }
    }
}
