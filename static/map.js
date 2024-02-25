var lat = 0
var lng = 0

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
        map.on('click', function(e) {
            lat = e.latlng.lat
            lng = e.latlng.lng
    
            const form = document.getElementById("pointForm")
            if (form.style.display === "none") {
                form.style.display = "block"
            }
            
            const point = L.circle([lat, lng], {
                color:'red',
                fillColor: '#f03',
                fillOpacity: 0.5,
                radius:30
            }).addTo(map)
          })
        })
        .catch(error => console.error('Error:', error))

        return map

        }


function addPoint () {
    const title = document.getElementById("name").value
    const description = document.getElementById("description").value

    fetch('/create_point', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({latitude: lat, longitude: lng, title:title, description:description})
    })
    .then(response => response.json())
    .then(data => {
        const id = data.id
        point.on('click', function() {
            window.location.href='point/' + id
        })
    })
    .catch(error => console.error('Error:', error))

    
}

export {setUp, addPoint}