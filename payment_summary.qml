import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.1
import QtQuick.Controls.Styles 1.2

Window {
    id : payment_summarypage
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
            width: 270
            height:200
            x:380;y:170
            radius:5
            color: "transparent"
            Column{
                anchors.horizontalCenter: parent.horizontalCenter
                id:optionsColumn
                spacing: 5
                anchors.fill : parent
                anchors.margins: 50
                anchors.leftMargin :10
                RoundButton{
                    id: sl
                    width: 100
                    height: 40
                    anchors.margins: parent
                    anchors.leftMargin: 10
                    x:2;y:2
                    palette {
                        button: "#29293d"
                    }
                    Text {
                        id: select
                        font.pixelSize: 14
                        color : "white"
                        font.family: "montserrat"
                        anchors.centerIn: sl
                        text: "Select"
                    }
                    onClicked: {
                      scaletext.text = scale.currentText;
                      timeline = scaletext.text
                    }
                }
                ComboBox {
                    id: scale
                    width: 100
                    height:40
                    x: 5; y:2
                    editable: true
                    background: Rectangle {
                        color: "#00bfff"
                        radius: 5
                    }
                    delegate: ItemDelegate {
                        id:itemDlgt
                        width: equipmentList.width
                        height:50
                        contentItem: Rectangle{
                            id:rectDlgt
                            width:30
                            height:50
                            radius: 3
                            color:itemDlgt.hovered?"#020537":"#DDDDDD";
                            Text {
                                id:textItem
                                text: modelData
                                color: hovered?"#DDDDDD":"#020537"
                                font: equipmentList.font
                                elide: Text.ElideRight
                                verticalAlignment: Text.AlignVCenter
                                horizontalAlignment: Text.AlignLeft
                            }
                         }
                     }
                    inputMethodHints: Qt.ImhDigitsOnly
                    currentIndex: 1
                    model: ListModel {
                        id: model
                        ListElement { text: "Days" }
                        ListElement { text: "Hours" }
                    }
                    onAccepted: {
                        id:maccepted
                        if (find(editText) === -1)
                            model.append({text: editText})
                    }
                    popup: Popup {
                          id:comboPopup
                          y: scale.height - 1
                          width: scale.width
                          height:contentItem.implicitHeight
                          padding: 1
                          ScrollView {
                              width: 100
                              height: 60
                              clip: true
                              ScrollBar.horizontal.interactive: true
                              ScrollBar.vertical.interactive: true
                              contentItem: ListView {
                                id:listView
                                implicitHeight: contentHeight
                                model: scale.popup.visible ? scale.delegateModel : null
                                ScrollIndicator.vertical: ScrollIndicator { }
                            }

                            background: Rectangle {
                               radius: 20
                               border.width: 2
                               color : "#DDDDDD"
                               border.color:"#95A4A8"
                            }
                          }
                      }
                }
                TextField{
                    id:scaletext
                    anchors.horizontalCenter: parent.horizontalCenter
                    readOnly: true
                    visible: false
                }
            }
            Column{
                anchors.horizontalCenter: parent.horizontalCenter
                id:optionsColumn1
                spacing: 5
                anchors.fill : parent
                anchors.margins: 50
                anchors.leftMargin :150
                RoundButton{
                    id: sl1
                    width: 100
                    height: 40
                    anchors.margins: parent
                    anchors.leftMargin: 10
                    x:2;y:2
                    palette {
                        button: "#29293d"
                    }
                    Text {
                        id: select1
                        font.pixelSize: 14
                        color : "white"
                        font.family: "montserrat"
                        anchors.centerIn: sl1
                        text: "Select"
                    }
                    onClicked: {
                      scaletext.text = scale1.currentText;
                      timeline_numeric = scaletext.text
                    }
                }
                ComboBox {
                    id: scale1
                    width: 100
                    height:40
                    x: 5; y:2
                    editable: true
                    background: Rectangle {
                        color: "#00bfff"
                        radius: 5
                    }
                    delegate: ItemDelegate {
                        id:itemDlgt1
                        width: equipmentList.width
                        height:50
                        contentItem: Rectangle{
                            id:rectDlgt1
                            width:30
                            height:50
                            radius: 3
                            color:itemDlgt1.hovered?"#020537":"#DDDDDD";
                            Text {
                                id:textItem1
                                text: modelData
                                color: hovered?"#DDDDDD":"#020537"
                                font: equipmentList.font
                                elide: Text.ElideRight
                                verticalAlignment: Text.AlignVCenter
                                horizontalAlignment: Text.AlignLeft
                            }
                         }
                     }
                    inputMethodHints: Qt.ImhDigitsOnly
                    currentIndex: 1
                    model: ListModel {
                        id: model1
                        ListElement { text: "01" } ListElement { text: "02" } ListElement { text: "03" }
                        ListElement { text: "04" } ListElement { text: "05" } ListElement { text: "06" }
                        ListElement { text: "07" } ListElement { text: "08" } ListElement { text: "09" }
                        ListElement { text: "10" } ListElement { text: "11" } ListElement { text: "12" }
                        ListElement { text: "13" } ListElement { text: "14" } ListElement { text: "15" }
                        ListElement { text: "17" } ListElement { text: "18" } ListElement { text: "19" }
                        ListElement { text: "20" } ListElement { text: "21" } ListElement { text: "22" }
                        ListElement { text: "23" } ListElement { text: "24" } ListElement { text: "25" }
                        ListElement { text: "26" } ListElement { text: "27" } ListElement { text: "28" }
                        ListElement { text: "29" } ListElement { text: "30" } ListElement { text: "31" }
                    }
                    onAccepted: {
                        id:maccepted
                        if (find(editText) === -1)
                            model1.append({text: editText})
                    }
                    popup: Popup {
                          id:comboPopup1
                          y: scale1.height - 1
                          width: scale1.width
                          height:contentItem.implicitHeight
                          padding: 1
                          ScrollView {
                              width: 100
                              height: 60
                              clip: true
                              ScrollBar.horizontal.interactive: true
                              ScrollBar.vertical.interactive: true
                              contentItem: ListView {
                                id:listView1
                                implicitHeight: contentHeight
                                model: scale1.popup.visible ? scale1.delegateModel : null
                                ScrollIndicator.vertical: ScrollIndicator { }
                            }
                            background: Rectangle {
                               radius: 20
                               border.width: 2
                               color : "#DDDDDD"
                               border.color:"#95A4A8"
                            }
                          }
                      }

                }
                TextField{
                    id:scaletext1
                    anchors.horizontalCenter: parent.horizontalCenter
                    readOnly: true
                    visible: false
                }
            }
        }
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

        Rectangle {
            id : estimation
            width: 240
            height:100
            x:400;y:10
            radius:5
            color: "transparent"
            Text {
                x:30;y:10
                font.pixelSize: 25
                color:"black"
                font.family: "montserrat"
                font.bold: true
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Approx Estimate")
            }
            Image {
                source: "inr_symbol.png"
                width:20
                height:30
                x:100;y:50
            }
            Text {
                x:125;y:50
                font.pixelSize: 25
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("600")
                font.bold: true
            }

        }

        Text {
            id : summary
            x:10;y:110
            font.pixelSize: 30
            color:"black"
            font.family: "montserrat"
            font.bold: true
            anchors.centerIn: parent.horizontalCenter
            text: qsTr("Summary")
        }
        Rectangle {
            id: horizontal_line_top
            x:10;y:150
            radius: 5
            visible: currentIndex == index;
            width: 350;    height: 5
            color: 'black'
        }
        Rectangle {
            id : parent_soc
            width:350
            height:50
            x:10;y:160
            color:"#DDDDDD"
            Text {
                id : soc
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("SoC")
            }
            TableView {
                id: summary_soc
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 260
                model : model_soc_summary
                delegate: Rectangle {
                    id : datasoc
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
        }
        Rectangle {
            id : parent_cost
            width:350
            height:50
            x:10;y:210
            color:"#DDDDDD"
            Text {
                id : cost_per_unit
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Cost Per Unit")
            }
            TableView {
                id: summary_cost
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 270
                model : model_cost_per_unit
                delegate: Rectangle {
                    id : cost
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr_symbol.png"
                width:20
                height:30
                x:260;y:10
            }

        }
        Rectangle {
            id : parent_energy
            width:350
            height:50
            x:10;y:260
            color:"#DDDDDD"
            Text {
                id : energy_consmed
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Energy Consumed")
            }
            TableView {
                id: summary_energy
                anchors.fill: parent
                topMargin: header.implicitHeight
                anchors.leftMargin: 265
                model : model_slot_energy
                delegate: Rectangle {
                    id : energy
                    implicitHeight: 50
                    implicitWidth: 50
                    color: "transparent"
                    x:30;y:20
                    Text {
                         anchors.centerIn: parent
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
        }
        Rectangle {
            id : parent_late_fees
            width:350
            height:50
            x:10;y:320
            color:"#DDDDDD"
            Text {
                id : late_fees
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Late Fees")
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
                         font.pixelSize: 20
                         color:"black"
                         text: model.display
                     }
                }
            }
            Image {
                source: "inr_symbol.png"
                width:20
                height:30
                x:255;y:10
            }
        }
        Rectangle {
            id : timeline_to_return
            width:350
            height:50
            x:10;y:370
            color:"#DDDDDD"
            Text {
                id : timeline_choosen
                x:2;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                anchors.centerIn: parent.horizontalCenter
                text: qsTr("Timeline")
            }
            Text {
                id:hours_days
                x:250;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                text: qsTr(payment_summarypage.timeline_numeric)
            }
            Text {
                id:numbers
                x:280;y:10
                font.pixelSize: 20
                color:"black"
                font.family: "montserrat"
                text: qsTr(payment_summarypage.timeline)
            }
        }

        Rectangle {
            id: horizontal_line_bottom
            x:10;y:430
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
            onClicked: payment_summarypage.close();
        }
    }
    RoundButton {
        id : next
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
