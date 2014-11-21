import QtQuick 2.0

JsonListModel {
    id: root
    source: 'http://localhost:8000/movies/' + (search?'?search='+search:'')
    query: '$.results'
    property string search
    function resolveUrl(path) {
//        return 'http://localhost:8000/browse/movies/' + path;
        return '/Users/jryannel/media/movies/' + path;
    }
}
