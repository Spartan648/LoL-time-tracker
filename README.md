LoL-time-tracker
Repositorio con un script en Python que extrae tu historial de partidas de League of Legends y calcula las horas totales jugadas.

Contenido
- Descripción
- Requisitos
- Instalación
- Configuración
- Uso
- Estructura del proyecto
- Mejoras futuras
- Licencia

Descripción
Este proyecto ofrece un script sencillo (calculo_http.py) que:
- Se conecta a la Riot API mediante HTTP directo.
- Obtiene el PUUID de tu cuenta (región LAN).
- Lista todos los IDs de partidas jugadas.
- Suma la duración de cada partida y expresa el total en horas.
Ideal para conocer tu tiempo invertido en League of Legends de forma rápida y sin depender de librerías externas.

Requisitos
- Python 3.6 o superior
- Paquetes de Python:
- requests
- (opcional) time (incluido en la librería estándar)

Instalación
- Clona el repositorio o descarga el ZIP:
git clone https://github.com/Spartan648/LoL-Time-Tracker.git
cd LoL-Time-Tracker
- Crea y activa un entorno virtual (opcional pero recomendado):
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
- Instala las dependencias:
pip install requests



Configuración
Antes de ejecutar, edita calculo_http.py y reemplaza:
- API_KEY con tu Dev o Production Key de Riot.
- SUMMONER.
API_KEY  = "RGAPI-28808d43-ccd3-48d0-bc5b-d6ddfef4d9c7"
SUMMONER = "Spartan648"



Uso
Ejecuta el script para calcular tus horas jugadas:
python calculo_http.py


Salida esperada:
Summoner endpoint: 200 OK
Batch 0 status: 200
…
Horas aproximadas jugadas: 712.34


El número que aparece al final es tu tiempo total en horas.

Estructura del proyecto
- calculo_http.py
Script principal que realiza todas las llamadas a la Riot API.
- README.md
Documentación y guía rápida de instalación y uso.

Mejoras futuras
- Implementar cache local (SQLite) para no repetir peticiones.
- Filtrar por tipo de cola (clasificatorias, ARAM, normales).
- Generar gráficas mensuales de tiempo jugado (usando matplotlib).
- Añadir validación de tasas de petición para evitar 429.

Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
