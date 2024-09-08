// Iniciar o mapa com coordenadas do ponto A (Anápolis)
let coordDiesel = [-16.3232, -48.9543];  
let coordUser = [];

// Armazenar uma referência ao marcador do ônibus
let busMarker;

// Inicializa o mapa
const map = L.map('map').setView(coordDiesel, 15);
const tileLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);

// Personalizar Ponto no mapa com imagem do diesel
const dieselIcon = L.icon({
  className: "diesel-pointers",
  iconUrl: 'https://cdn-icons-png.flaticon.com/512/9249/9249336.png',
  iconSize: [45, 45]
});
busMarker = L.marker(coordDiesel, { icon: dieselIcon }).addTo(map);

function startService() {
  // Identifica a melhor rota para iniciar a viagem
  const control = L.Routing.control({
      waypoints: [
          L.latLng(coordDiesel[0], coordDiesel[1]),
          L.latLng(coordUser[0], coordUser[1])
      ],
      routeWhileDragging: true // Atualiza a rota enquanto arrasta os pontos no mapa
  }).on('routesfound', function (e) {
      const route = e.routes[0];
      const coordinates = route.coordinates;
      followRoute(coordinates);
  }).addTo(map);
}

function followRoute(coordinates) {
  let index = 0;
  const interval = setInterval(() => {
      if (index >= coordinates.length) {
          clearInterval(interval);
          return;
      }
      const coordinate = coordinates[index];
      busMarker.setLatLng([coordinate.lat, coordinate.lng]);
      map.panTo([coordinate.lat, coordinate.lng]);
      index++;
  }, 1000); // Change this interval according to your preference
}

// Adicione um evento de mudança para o seletor suspenso de rotas
document.getElementById('route-select').addEventListener('change', function() {
  var selectedRoute = this.value;
  map.eachLayer(function(layer) {
      if (layer !== tileLayer && layer !== busMarker) {
          map.removeLayer(layer);
      }
  });
  switch (selectedRoute) {
      case 'rota1':
          coordDiesel = [-16.3232, -48.9543]; // Ponto de partida
          coordUser = [-16.29424570841718, -48.94567732194342]; // Destino
          break;
      case 'rota2':
          coordDiesel = [-16.3232, -48.9543];
          coordUser = [-16.33663814007476, -48.94059804741932];
          break;
      case 'rota3':
          coordDiesel = [-16.3232, -48.9543];
          coordUser = [-16.32416342943865, -48.94802209124979];
          break;
      default:
          return;
  }
});

// Adicione um evento de clique para o botão "Confirmar Rota"
document.getElementById('confirm-route-btn').addEventListener('click', function() {
  if (coordDiesel && coordUser.length > 0) {
      startService();
  } else {
      alert("Por favor, selecione uma rota antes de confirmar.");
  }
});