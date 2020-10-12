function myMap() {
    var mapCanvas = document.getElementById("map");
    var mapOptions = {
        center: new google.maps.LatLng(39.099724, -94.578331),
        zoom: 9
    };
    var map = new google.maps.Map(mapCanvas, mapOptions);
}
