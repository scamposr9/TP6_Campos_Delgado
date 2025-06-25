from typing import Optional
from fhir.resources.observation import Observation
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from fhir.resources.quantity import Quantity

def create_observation_resource(
    patient_id: str,
    observation_code: str,
    observation_display: str,
    observation_system: str = "http://loinc.org",
    value: Optional[float] = None,
    unit: Optional[str] = None,
    unit_system: Optional[str] = "http://unitsofmeasure.org",
    unit_code: Optional[str] = None,
    status: str = "final",
    category_code: Optional[str] = "vital-signs",
    category_display: Optional[str] = "Signos Vitales",
    effective_datetime: Optional[str] = None,
    encounter_id: Optional[str] = None  # Permite vincular a um Encounter
) -> Observation:
     # Criar a categoria da observação (ex: sinais vitais, laboratório)
    category = CodeableConcept(
        coding=[Coding(
            system="http://terminology.hl7.org/CodeSystem/observation-category",
            code=category_code,
            display=category_display
        )]
    )

    # Criar o código da observação (ex: temperatura corporal, pressão arterial)
    code = CodeableConcept(
        coding=[Coding(
            system=observation_system,
            code=observation_code,
            display=observation_display
        )]
    )

    # Criar a referência ao paciente
    subject = Reference(reference=f"Patient/{patient_id}")

    # Criar o recurso Observation
    observation = Observation(
        status=status,
        category=[category],
        code=code,
        subject=subject
    )

    # Adicionar valor quantitativo, se fornecido
    if value is not None and unit and unit_code:
        observation.valueQuantity = Quantity(
            value=value,
            unit=unit,
            system=unit_system,
            code=unit_code
        )

    # Adicionar data/hora da observação, se fornecida
    if effective_datetime:
        observation.effectiveDateTime = effective_datetime

    # Adicionar vínculo com Encounter, se fornecido
    if encounter_id:
        observation.encounter = Reference(reference=f"Encounter/{encounter_id}")

    return observation
