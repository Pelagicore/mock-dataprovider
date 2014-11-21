import QtQuick 2.0
import mockdata 1.0

Rectangle {
    id: root
    width: 800
    height: 400

    gradient: Gradient {
        GradientStop { position: 0.0; color: "#ff5f3b" }
        GradientStop { position: 1.0; color: "#ff2a68" }
    }

    PhotoCore {
        id: core
    }
    ListView {
        id: view
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.verticalCenter: parent.verticalCenter
        height: root.height/2
        spacing: 8

        model: core.model

        orientation: Qt.Horizontal
        delegate: Image {
            id: image
            width: height; height: view.height
            source: core.resolveUrl(model.source)
            fillMode: Image.PreserveAspectCrop
            transform: Rotation {
                id: rot
                origin {
                    x: image.width/2
                    y: image.height/2
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
        }
        layer.enabled: true
        layer.effect: ShaderEffect {
            vertexShader: "
                        uniform highp mat4 qt_Matrix;
                        attribute highp vec4 qt_Vertex;
                        attribute highp vec2 qt_MultiTexCoord0;
                        varying highp vec2 coord;
                        void main() {
                            coord = qt_MultiTexCoord0;
                            gl_Position = qt_Matrix * qt_Vertex;
                        }"
            fragmentShader: "
                        varying highp vec2 coord;
                        uniform sampler2D source;
                        uniform lowp float qt_Opacity;
                        void main() {
                            lowp vec4 tex = texture2D(source, coord);
                            gl_FragColor = vec4(vec3(dot(tex.rgb, vec3(0.344, 0.5, 0.156))), tex.a) * qt_Opacity;
                        }"
        }

    }


}
