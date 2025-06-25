from observation import create_observation_resource
from base import send_resource_to_hapi_fhir

# Substitua com o ID real do paciente criado
patient_id = "48029210"

observation = create_observation_resource(
    patient_id=patient_id,
    observation_code="8310-5",  # Código LOINC para temperatura corporal
    observation_display="Body Temperature",
    value=37.5,
    unit="Celsius",
    unit_code="Cel",
    effective_datetime="2025-06-25T14:30:00Z"
)

# Envia para o servidor FHIR
observation_id = send_resource_to_hapi_fhir(observation, 'Observation')

print("ID da Observation criada:", observation_id)