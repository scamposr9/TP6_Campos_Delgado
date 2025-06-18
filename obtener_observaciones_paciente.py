import requests

def obtener_observaciones(patient_id):
    url = f"https://hapi.fhir.org/baseR4/Observation?patient={patient_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for entry in data.get("entry", []):
            obs = entry["resource"]
            tipo = obs.get("code", {}).get("coding", [{}])[0].get("display", "Desconocido")
            valor = obs.get("valueQuantity", {}).get("value", "Sin valor")
            unidad = obs.get("valueQuantity", {}).get("unit", "")
            interpretacion = obs.get("interpretation", [{}])[0].get("coding", [{}])[0].get("display", "")
            print(f"Tipo: {tipo}, Valor: {valor} {unidad}, Interpretación: {interpretacion}")
    else:
        print("Error al obtener las observaciones")
