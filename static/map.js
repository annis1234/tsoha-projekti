
function setUp () {
    const map = L.map('map').setView([60.1676, 24.94327], 13)
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
        }).addTo(map)
        return map
    }

export {setUp}