import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : logout_page
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
        x:100;y:170
        color:"#020537"
        radius: 5
        Text {
            id: title_text
            x:2;y:2
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Do You Wants To Make Another Order?")
            color: "white"
            font.pixelSize: 30
            font.family: "montserrat"
            font.bold: true
        }
    }
    RoundButton {
        id : yes
        width: 125
        height: 50
        x:240;y:240
        palette {
            button: "#00bfff"
        }
        Text {
            id: yeslabel
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: yes
            text: "Yes"
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                logout_page.close();
            }
        }
    }
    RoundButton {
        id : no
        width: 125
        height: 50
        x:400;y:240
        palette {
            button: "#00bfff"
        }
        Text {
            id: nolabel
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: no
            text: "No"
        }
        MouseArea {
            anchors.fill: parent
            onClicked: {
                var component = Qt.createComponent("user_logout.qml")
                var user_logout_window    = component.createObject()
                user_logout_window.show()
            }
        }
    }
}
