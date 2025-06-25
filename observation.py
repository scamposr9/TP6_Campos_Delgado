"""
Módulo para criar um recurso FHIR Observation.
"""

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
    effective_datetime: Optional[str] = None
) -> Observation:
    """
    Cria um recurso FHIR Observation com os parâmetros fornecidos.

    :param patient_id: ID do paciente relacionado à observação.
    :param observation_code: Código da observação (ex: LOINC).
    :param observation_display: Descrição do tipo de observação.
    :param observation_system: Sistema de codificação (ex: http://loinc.org).
    :param value: Valor numérico da observação.
    :param unit: Unidade do valor (ex: °C, mmHg).
    :param unit_system: Sistema da unidade (ex: http://unitsofmeasure.org).
    :param unit_code: Código da unidade (ex: "Cel", "mm[Hg]").
    :param status: Status da observação (ex: final).
    :param category_code: Código da categoria (ex: vital-signs).
    :param category_display: Nome legível da categoria.
    :param effective_datetime: Data/hora da observação (formato ISO 8601).
    :return: Recurso FHIR Observation.
    """
    # Categoria da observação (ex: sinais vitais)
    category = CodeableConcept(
        coding=[Coding(
            system="http://terminology.hl7.org/CodeSystem/observation-category",
            code=category_code,
            display=category_display
        )]
    )

    # Tipo de observação
    code = CodeableConcept(
        coding=[Coding(
            system=observation_system,
            code=observation_code,
            display=observation_display
        )]
    )

    # Referência ao paciente
    subject = Reference(reference=f"Patient/{patient_id}")

    # Criar o recurso Observation
    observation = Observation(
        status=status,
        category=[category],
        code=code,
        subject=subject
    )

    # Valor da observação (quantitativo)
    if value is not None and unit and unit_code:
        observation.valueQuantity = Quantity(
            value=value,
            unit=unit,
            system=unit_system,
            code=unit_code
        )

    # Data/hora da observação
    if effective_datetime:
        observation.effectiveDateTime = effective_datetime

    return observation

