import QtQuick 2.0

JsonListModel {
    id: root
    source: 'http://localhost:8000/photos/' + (search?'?search='+search:'')
    query: '$.results'
    property string search
    function resolveUrl(path) {
        return 'http://localhost:8000/browse/photos/' + path;
    }
}
