import QtQuick 2.2
import mockdata 1.0
import QtGraphicalEffects 1.0
import QtMultimedia 5.0
import QtQuick.Layouts 1.1


Rectangle {
    id: root
    width: 800
    height: 300
    color: '#000'

    //    MusicCore {
    //        id: core
    //    }

    //    ContactCore {
    //        id: contacts
    //    }

    MovieCore {
        id: core
    }


    Video {
        id: video
        anchors.fill: parent
        anchors.topMargin: 24
        anchors.bottomMargin: 24
    }


    ListView {
        id: view
        height: 128
        width: root.width
        anchors.verticalCenter: root.verticalCenter
        model: core.model
        property string currentVideo: core.model.get(currentIndex).source
        onCurrentVideoChanged: print(currentVideo)
        orientation: Qt.Horizontal
        delegate: Item {
            property var entry: model
            width: view.width/5
            height: 128
            Image {
                id: overlay
                source: 'assets/overlay.png'
//                    anchors.horizontalCenterOffset: 4
                opacity: 0.5
                transform: Rotation {
                    id: rot
                    origin {
                        x: overlay.width/2
                        y: overlay.height/2
                    }
                    axis {
                        x: 1.0
                        y: 1.0
                        z: 1.0
                    }

                    RotationAnimation on angle {
                        loops: Animation.Infinite
                        from: 0
                        to: 360
                        duration: 2000
                    }
                }
                anchors.centerIn: parent
                antialiasing: true
                scale: 1.2
            }

            Image {
                anchors.centerIn: parent
                width: 128; height: width
                sourceSize.width: width
                sourceSize.height: height
                fillMode: Image.PreserveAspectCrop
                antialiasing: true
                source: core.resolveUrl(model.cover)
                layer.enabled: true
                layer.smooth: true
                layer.effect: OpacityMask {
                    maskSource: Image {
                        source: 'assets/mask.png'
                    }
                    Image {
                        source: 'assets/overlay.png'
                        anchors.centerIn: parent
                        antialiasing: true
                    }
                }
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    view.currentIndex = index
                    video.source = core.resolveUrl(view.currentVideo)
                    video.play()
                }
            }
        }
    }
}

