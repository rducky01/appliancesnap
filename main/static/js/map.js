function myMap() {
    var mapCanvas = document.getElementById("map");
    var mapOptions = {
        center: new google.maps.LatLng(38.7, -94.3),
        zoom: 9
    };
    var map = new google.maps.Map(mapCanvas, mapOptions);
}
