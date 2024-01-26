 function setUp () {
    const map = L.map('map').setView([60.1676, 24.94327], 13)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map)

        fetch('/get_points')
        .then(response => response.json())
        .then(data => {
            const pointsData = data.points

        pointsData.forEach(function(p){
            const point = L.circle([p.latitude, p.longitude], {
                color: 'red',
                fillColor: '#f03',
                fillOpacity: 0.5,
                radius: 30
            }).addTo(map)

            const id = p.id
            point.on('click', function(){
                window.location.href ='point/' + id
            })
        })
        })

        map.on('click', function(e) {
            const lat = e.latlng.lat
            const lng = e.latlng.lng
            
            const point = L.circle([lat, lng], {
                color:'red',
                fillColor: '#f03',
                fillOpacity: 0.5,
                radius:30
            }).addTo(map)
            
            fetch('/create_point', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({latitude: lat, longitude: lng})
            })
            .then(response => response.json())
            .then(data => {
                const id = data.id
                point.on('click', function() {
                    window.location.href='point/' + id

                })
            })

        })
        return map
    }

export {setUp}