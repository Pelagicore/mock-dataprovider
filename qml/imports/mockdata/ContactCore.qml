import QtQuick 2.0

JsonListModel {
    id: root
    source: 'http://localhost:8000/contacts/' + (search?'?search='+search:'')
    query: '$.results'
    property string search
    function randomFace() {
        return 'http://localhost:8000/browse/faces/' + Math.floor(Math.random()*1368) + ".jpg"
    }
}
