import requests

def crear_observacion(patient_id):
    url = "https://hapi.fhir.org/baseR4/Observation"
    headers = {"Content-Type": "application/fhir+json"}

    data = {
        "resourceType": "Observation",
        "status": "final",
        "category": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                "code": "vital-signs",
                "display": "Vital Signs"
            }]
        }],
        "code": {
            "coding": [{
                "system": "http://loinc.org",
                "code": "85354-9",
                "display": "Blood pressure panel with all children optional"
            }]
        },
        "subject": {
            "reference": f"Patient/{patient_id}"
        },
        "encounter": {
            "reference": "Encounter/example"
        },
        "effectiveDateTime": "2025-06-18T12:00:00+00:00",
        "valueQuantity": {
            "value": 120,
            "unit": "mmHg",
            "system": "http://unitsofmeasure.org",
            "code": "mm[Hg]"
        },
        "interpretation": [{
            "coding": [{
                "system": "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation",
                "code": "H",
                "display": "High"
            }]
        }],
        "note": [{
            "text": "Paciente con presión alta registrada durante el chequeo de rutina."
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.json())
