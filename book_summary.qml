import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.4

Window {
    id : book_summarypage
    width: 800
    height: 480
    visible: true
    color : "#020537"
    title: qsTr("Booking Summary")
    Rectangle {
        width: 650
        height: 455
        x:15;y:15
        radius:5
        color: "#DDDDDD"
        Rectangle {
            id : choosen_slot
            width: 110
            height:80
            x:10;y:10
            radius:5
            color: "#00bfff"
            TableView {
                id: choosen_slot_view
                anchors.fill: parent
                anchors.margins: 15
                anchors.leftMargin: 25
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
                        font.pixelSize: 40
                        font.family: "montserrat"
                        color:"black"
                        text: model.display
                     }
                }
            }
        }
        Text {
            id : summary
            x:140;y:50
            font.pixelSize: 35
            color:"black"
            font.family: "montserrat"
            font.bold: true
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Summary")
        }
        Text {
            id : booking_retention
            x:400;y:95
            font.pixelSize: 20
            color:"black"
            font.family: "montserrat"
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Rental")
        }
        Text {
            id : retention
            x:400;y:120
            font.pixelSize: 20
            color:"black"
            font.family: "montserrat"
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Booking Retention")
        }
        Rectangle {
            id: horizontal_line_top
            x:10;y:100
            radius: 5
            visible: currentIndex == index;
            width: 350;    height: 5
            color: 'black'
        }
        Rectangle {
            id : four_hrs
            width: 110
            height: 50
            x:400;y:160
            border.color: "black"
            property bool isGreen: true
            color: isGreen ? "#99e401" : "#145214"
            Text {
                id: four_hrs_text
                font.pixelSize: 18
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: four_hrs
                text: "4 HRS"
                color:"white"
            }
            MouseArea {
                id:mouseArea
                anchors.fill: parent
                onClicked: {
                    test_retension_timeline(4)
                    four_hrs.isGreen = !four_hrs.isGreen
                }
            }
            states: State {
                name: "brighter"; when: mouseArea.pressed
                PropertyChanges { target: four_hrs; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id : eight_hrs
            width: 110
            height: 50
            x:530;y:160
            border.color: "black"
            property bool isGreen: true
            color: isGreen ? "#99e401" : "#145214"
            Text {
                id: eight_hrs_text
                font.pixelSize: 18
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: eight_hrs
                text: "8 HRS"
                color:"white"
            }
            MouseArea {
                id:mouseArea_8
                anchors.fill: parent
                onClicked: {
                    test_retension_timeline(8)
                    eight_hrs.isGreen = !eight_hrs.isGreen
                }
            }
            states: State {
                name: "brighter"; when: mouseArea_8.pressed
                PropertyChanges { target: eight_hrs; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id : twelve_hrs
            width: 110
            height: 50
            x:400;y:220
            border.color: "black"
            property bool isGreen: true
            color: isGreen ? "#99e401" : "#145214"
            Text {
                id: twelve_hrs_text
                font.pixelSize: 18
                font.family: "montserrat"
                font.bold: true
                anchors.centerIn: twelve_hrs
                text: "12 HRS"
                color:"white"
            }
            MouseArea {
                id:mouseArea_12
                anchors.fill: parent
                onClicked: {
                    test_retension_timeline(12)
                    twelve_hrs.isGreen = !twelve_hrs.isGreen
                }
            }
            states: State {
                name: "brighter"; when: mouseArea_12.pressed
                PropertyChanges { target: twelve_hrs; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
           id : sixteen_hrs
           width: 110
           height: 50
           border.color: "black"
           x:530;y:220
           property bool isGreen: true
           color: isGreen ? "#99e401" : "#145214"
           Text {
                id: sixteen_hrs_text
                font.pixelSize: 18
                font.family: "montserrat"
                font.bold: true
                anchors.centerIn: sixteen_hrs
                text: "16 HRS"
                color:"white"
            }
            MouseArea {
                id:mouseArea_16
                anchors.fill: parent
                onClicked: {
                    test_retension_timeline(16)
                    sixteen_hrs.isGreen = !sixteen_hrs.isGreen
                }
            }
            states: State {
                name: "brighter"; when: mouseArea_16.pressed
                PropertyChanges { target: sixteen_hrs; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }

        }
        Rectangle {
            id : twenty_hrs
            width: 110
            height: 50
            x:400;y:280
            border.color: "black"
            property bool isGreen: true
            color: isGreen ? "#99e401" : "#145214"
            Text {
                id: twenty_hrs_text
                font.pixelSize: 18
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: twenty_hrs
                text: "20 HRS"
                color:"white"
            }
            MouseArea {
                id:mouseArea_20
                anchors.fill: parent
                onClicked: {
                    test_retension_timeline(20)
                    twenty_hrs.isGreen = !twenty_hrs.isGreen
                }
            }
            states: State {
                name: "brighter"; when: mouseArea_20.pressed
                PropertyChanges { target: twenty_hrs; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id : twentyfour_hrs
            width: 110
            height: 50
            x:530;y:280
            border.color: "black"
            property bool isGreen: true
            color: isGreen ? "#99e401" : "#145214"
            Text {
                id: twentyfour_hrs_text
                font.pixelSize: 18
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: twentyfour_hrs
                text: "24 HRS"
                color:"white"
            }
            MouseArea {
                id:mouseArea_24
                anchors.fill: parent
                onClicked: {
                    test_retension_timeline(24)
                    twentyfour_hrs.isGreen = !twentyfour_hrs.isGreen
                }
            }
            states: State {
                name: "brighter"; when: mouseArea_24.pressed
                PropertyChanges { target: twentyfour_hrs; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }
        Rectangle {
            id : custom
            width: 110
            height: 50
            x:400;y:340
            border.color: "black"
            property bool isGreen: true
            color: isGreen ? "#99e401" : "#145214"
            Text {
                id: custom_rental
                font.pixelSize: 18
                font.bold: true
                font.family: "montserrat"
                anchors.centerIn: custom
                text: "Custom"
                color:"white"
            }
            MouseArea {
                id:mouseArea_cust
                anchors.fill: parent
                onClicked: {
                    custom.isGreen = !custom.isGreen
                    var component = Qt.createComponent("custom_rental.qml")
                    var custom_rental_window    = component.createObject()
                    custom_rental_window.show()
                }
            }
            states: State {
                name: "brighter"; when: mouseArea_cust.pressed
                PropertyChanges { target: custom; color: "steelblue" }
            }
            transitions: Transition {
                ColorAnimation { duration: 500 }
            }
        }

        Rectangle {
            id : parent_soc
            width:350
            height:50
            x:10;y:110
            color:"#DDDDDD"
            Text {
                id : soc
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("State of Charge SoC")
            }
            TableView {
                id: summary_soc
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 265
                model : model_booked_slot_soc
                delegate: Rectangle {
                    id : datasoc
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 18
                         color:"black"
                         text: model.display
                     }
                }
            }
        }
        Rectangle {
            id : parent_timetaken
            width:350
            height:50
            x:10;y:150
            color:"#DDDDDD"
            Text {
                id : timetaken
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Time taken to Charge")
            }
            TableView {
                id: summary_timetaken
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 285
                model : model_time_taken_to_charge
                delegate: Rectangle {
                    id : timetaken_charge
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 18
                         color:"black"
                         text: model.display+ " HH:MM"
                     }
                }
            }
        }
        Rectangle {
            id : parent_energy
            width:350
            height:50
            x:10;y:190
            color:"#DDDDDD"
            Text {
                id : energy_consmed
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Energy Stored")
            }
            TableView {
                id: summary_energy
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 260
                model : model_slot_energy
                delegate: Rectangle {
                    id : energy
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 18
                         color:"black"
                         text: model.display
                     }
                }
            }
        }
        Rectangle {
            id : cost_per_unit
            width:350
            height:50
            x:10;y:230
            color:"#DDDDDD"
            Text {
                id : costperunit
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Cost Per Unit")
            }
            TableView {
                id: cost_per
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 267
                model : model_cost_per_unit
                delegate: Rectangle {
                    id : cost
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 18
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr.png"
                width:20
                height:30
                x:255;y:10
            }
        }
        Rectangle {
            id : parent_retention
            width:350
            height:50
            x:10;y:270
            color:"#DDDDDD"
            Text {
                id : retention_cost
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Rental Cost")
            }
            TableView {
                id: summary_retension
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 270
                model : model_retension_cost
                delegate: Rectangle {
                    id : retensioncost
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 18
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr.png"
                width:20
                height:30
                x:255;y:10
            }
        }
        Rectangle {
            id : parent_late_fees
            width:350
            height:50
            x:10;y:310
            color:"#DDDDDD"
            Text {
                id : late_fees
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Late Fees (Carried Over)")
            }
            TableView {
                id: summary_latefees
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 270
                model : model_late_fees
                delegate: Rectangle {
                    id : latefees
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 18
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr.png"
                width:20
                height:30
                x:255;y:10
            }
        }
        Rectangle {
            id : tax_gst
            width:350
            height:50
            x:10;y:350
            color:"#DDDDDD"
            Text {
                id : taxgst
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Taxes GST (18%)")
            }
            TableView {
                id: taxes
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 285
                model : model_taxes
                delegate: Rectangle {
                    id : tax
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 18
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr.png"
                width:20
                height:30
                x:255;y:10
            }
        }
        Rectangle {
            id : total_Estimated
            width:350
            height:40
            x:10;y:405
            color:"#DDDDDD"
            Text {
                id : timeline_choosen
                x:2;y:10
                font.pixelSize: 18
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Total (Estimated)")
            }
            TableView {
                id: summary_total
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 290
                model : model_estimated_payment
                delegate: Rectangle {
                    id : total
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 22
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr.png"
                width:20
                height:30
                x:255;y:8
            }
        }

        Rectangle {
            id: horizontal_line_bottom
            x:10;y:400
            radius: 5
            visible: currentIndex == index;
            width: 350;    height: 5
            color: 'black'
        }
    }
    RoundButton {
        id : back
        width: 125
        height: 50
        x:670;y:340
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
            onClicked: book_summarypage.close();
        }
    }
    RoundButton {
        id : next
        width: 125
        height: 50
        x:670;y:410
        palette {
            button: "#00bfff"
        }
        Text {
            id: next_page
            font.pixelSize: 20
            font.family: "montserrat"
            anchors.centerIn: next
            text: "Next"
        }
        onClicked:{
            var component = Qt.createComponent("final_payment.qml")
            var final_payment_window    = component.createObject()
            final_payment_window.show()
        }
    }
}
