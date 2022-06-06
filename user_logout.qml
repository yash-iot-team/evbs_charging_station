import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : user_logout_page
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("User Logout")
    property int counter:15
    Rectangle {
        id:logout
        width: 550
        height: 90
        x:100;y:170
        color:"#020537"
        radius: 5
        Text {
            id: title_text
            x:2;y:2
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Sucessfully Logging Out... Please wait")
            color: "white"
            font.pixelSize: 30
            font.family: "montserrat"
            font.bold: true
        }
        ProgressBar {
            id: pb1
            value: 0.5
            padding: 2
            x:120;y:340
            width:400;height:30
            indeterminate: true
            background: Rectangle{
                color: "white"
            }
            visible: simpletimer.running
        }
    }
    Rectangle {
        id:counter_to_remove_bsu
        width: 550
        height: 90
        x:370;y:220
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
                counter -= 5
                if (counter <= 0)
                {
                    user_logout_page.close();
                    logout_page.close();
                    evbs_dashboard.close();
                }
            }
        }
    }
}
