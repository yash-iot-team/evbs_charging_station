import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : selected_slot_summarypage
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("Payment Summary")
    property string timeline: ""
    property string timeline_numeric: ""
    Rectangle {
        width: 650
        height: 450
        x:15;y:15
        radius:5
        color: "#DDDDDD"
        Rectangle {
            id : choosen_slot
            width: 80
            height:80
            x:10;y:10
            radius:5
            color: "#00bfff"
            TableView {
                id: choosen_slot_view
                anchors.fill: parent
                anchors.margins: 15
                anchors.leftMargin: 15
                model : model_selected_slot
                delegate: Rectangle {
                    id : selected_slot_delegate
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                        anchors.centerIn: parent
                        font.bold: true
                        font.pixelSize: 30
                        font.family: "montserrat"
                        color:"black"
                        text: model.display
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
            onClicked: selected_slot_summarypage.close();
        }
    }
    RoundButton {
        id : trend
        width: 125
        height: 50
        x:670;y:80
        palette {
            button: "#00bfff"
        }
        Text {
            id: next_page
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: trend
            text: "Trend"
        }
    }
}
