import time
import requests

API_KEY      = "RGAPI-28808d43-ccd3-48d0-bc5b-d6ddfef4d9c7"      # copia tu dev key EXACTA
REGION       = "la1"                      # Latin America North
MATCH_REGION = "americas"                 # routing regional para match-v5
SUMMONER     = "Spartan648"

# Pon la clave siempre en este header, nunca en params
HEADERS = {"X-Riot-Token": API_KEY}

# 1) Obtenemos el puuid
url_summ = (
    f"https://{REGION}.api.riotgames.com"
    f"/lol/summoner/v4/summoners/by-name/{SUMMONER}"
)
r = requests.get(url_summ, headers=HEADERS)
print("Summoner endpoint:", r.status_code, r.text)  # chequeo rápido
r.raise_for_status()
puuid = r.json()["puuid"]

# 2) Traemos todos los match IDs
match_ids = []
start = 0
while True:
    url_list = (
        f"https://{MATCH_REGION}.api.riotgames.com"
        f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
    )
    r = requests.get(url_list, headers=HEADERS,
                     params={"start": start, "count": 100})
    print(f"Batch {start} status:", r.status_code)
    r.raise_for_status()
    batch = r.json()
    if not batch:
        break
    match_ids.extend(batch)
    start += 100
    time.sleep(1)

# 3) Sumamos las duraciones
total_seconds = 0
for m_id in match_ids:
    url_match = (
        f"https://{MATCH_REGION}.api.riotgames.com"
        f"/lol/match/v5/matches/{m_id}"
    )
    r = requests.get(url_match, headers=HEADERS)
    print(f"Match {m_id[:8]} status:", r.status_code)
    r.raise_for_status()
    total_seconds += r.json()["info"]["gameDuration"]
    time.sleep(1)

# 4) Imprimimos el resultado en horas
print(f"\nHoras aproximadas jugadas: {total_seconds/3600:.2f}")