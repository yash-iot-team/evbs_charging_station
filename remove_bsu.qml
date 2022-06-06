import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : remove_bsu
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("Remove BSU")
    property int counter:0
    Rectangle {
        id:title_for_bsu
        width: 550
        height: 90
        x:200;y:40
        color:"#020537"
        radius: 5
        Text {
            id: title_text
            x:2;y:2
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Remove BSU from Slot")
            color: "white"
            font.pixelSize: 30
            font.family: "montserrat"
            font.bold: true
        }
        TableView {
            id: tableview_booked_slot
            anchors.fill: parent
            clip: true
            anchors.topMargin: 2
            anchors.leftMargin: 360
            model : model_selected_slot
            delegate: Rectangle {
                id : slot1_delegate
                implicitHeight: 30
                implicitWidth: 30
                color: "transparent"
                x:600;y:60
                Text {
                    anchors.horizontalCenter: parent
                    font.bold: true
                    font.pixelSize: 30
                    color:"white"
                    font.family: "montserrat"
                    text: model.display
                 }
            }
        }

    }
    AnimatedImage {
        id: sprite
        source: "removebsu.gif"
        width:400
        height:250
        x:220;y:100
    }
    Rectangle {
        id:counter_to_remove_bsu
        width: 550
        height: 90
        x:370;y:370
        color:"#020537"
        radius: 5
        Text{
            id: titlecount
            x:2;y:2
            anchors.centerIn: parent.horizontalCenter
            text: counter
            color: "white"
            font.pixelSize: 30
            font.family: "montserrat"
            font.bold: true
        }
        Timer {
            interval: 800; running: true; repeat: true
            onTriggered:
            {
                counter += 1
                if (counter == 20)
                {
                    var component = Qt.createComponent("logout_page.qml")
                    var logout_page_window    = component.createObject()
                    logout_page_window.show()
                    remove_bsu.close();
                }
            }
        }
    }
}
