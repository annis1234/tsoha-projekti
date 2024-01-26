
function setUp () {
    const map = L.map('map').setView([60.1676, 24.94327], 13)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map)

        map.on('click', function(e) {
            const lat = e.latlng.lat
            const lng = e.latlng.lng
            
            const point = L.circle([lat, lng], {
                color:'red',
                fillColor: '#f03',
                fillOpacity: 0.5,
                radius:20
            }).addTo(map)

        })
        return map
    }

export {setUp}