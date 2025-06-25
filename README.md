# Proyecto FHIR - TP6

Este proyecto implementa el estándar **FHIR (Fast Healthcare Interoperability Resources)** para crear y gestionar recursos de salud, específicamente de **pacientes** y obtener las **Observaciones** que presentan. El objetivo es crear y gestionar los recursos **Patient** y **Observaciones**.

### Descripción de los Archivos

- **base.py**: Contiene las funciones para interactuar con el servidor FHIR (enviar recursos y obtener recursos).
- **patient.py**: Contiene la función para crear el recurso **Patient**.
- **workflow.py**: Define el flujo de trabajo para crear un paciente y enviar el recurso **Patient** al servidor.
- **observation.py**: Contiene la función que crea un recurso **Observation** a partir de parámetros clínicos como temperatura, presión, frecuencia, etc.
- **workflow_observation.py**: Define el flujo para crear una observación clínica de un paciente y enviarla al servidor FHIR.

## Requisitos

Para ejecutar este proyecto, necesitarás tener Python 3.13.5 y los siguientes paquetes instalados:

1. **fhir.resources**: Paquete para manejar recursos FHIR en Python.
    ```bash
    pip install fhir.resources
    ```

2. **requests**: Paquete para hacer solicitudes HTTP.
    ```bash
    pip install requests
    ```


## Workflow
### `workflow.py` - Crear un paciente

Este archivo crea un recurso **Patient** con los siguientes parámetros:

- **family_name**: Apellido del paciente.
- **given_name**: Nombre del paciente.
- **birth_date**: Fecha de nacimiento.
- **gender**: Género.
- **phone**: Teléfono (opcional).
- **identifier**: Identificador único del paciente (SSN).

Una vez creado el paciente, se envía al servidor FHIR y se obtiene el ID del paciente. 

### `workflow_observation.py` - Crea una observación clínica vinculada a un paciente

Este archivo crea un recurso **FHIR Observation** y lo asocia a un paciente previamente registrado. Los parámetros utilizados permiten registrar signos vitales u otras observaciones clínicas relevantes. Incluye:

- **patient_id**: ID del paciente al que se le realiza la observación.
- **observation_code**: Código estandarizado (por ejemplo, LOINC) que identifica el tipo de observación (ej. temperatura, presión arterial).
- **observation_display**: Descripción legible del tipo de observación (ej. Body Temperature).
- **value**: Valor numérico registrado en la observación (ej. 37.5).
- **unit**: Unidad del valor (ej. Celsius)
- **unit_code**: Código de la unidad (ej. Cel para grados Celsius).
- **status**: Estado de la observación (por defecto, final).
- **category_code**: Categoría de la observación (por defecto, vital-signs).
- **category_display**: Nombre de la categoría (por ejemplo, Signos Vitales).
- **effective_datetime**: Fecha y hora en la que se realizó la observación (formato ISO 8601, ej. 2025-06-25T14:30:00Z).

Una vez creado el recurso **Observation**, este se envía al servidor FHIR mediante el método `send_resource_to_hapi_fhir`, y se obtiene como respuesta el ID único de la observación creada.

## Archivos Relevantes del Proyecto

### `base.py` - Funciones para interactuar con el servidor FHIR

Este archivo contiene las funciones necesarias para enviar y recuperar recursos FHIR desde el servidor público de FHIR. Se usan dos funciones principales:

- `send_resource_to_hapi_fhir`: Envía un recurso FHIR al servidor.
- `get_resource_from_hapi_fhir`: Recupera un recurso FHIR desde el servidor usando su ID.

### `patient.py` - Crear un paciente

Este archivo contiene la función para crear un recurso **Patient**. Los parámetros utilizados incluyen el nombre, la fecha de nacimiento, el género y el identificador del paciente (SSN).

### `observation.py` - Crear una observación clínica

Este archivo contiene la función para crear el recurso **Observation**. Se asocia a un paciente y permite registrar signos vitales u otras observaciones clínicas, utilizando códigos estandarizados como LOINC.

---

## Uso

1. **Crear un paciente**: Para crear un paciente, simplemente ejecuta `workflow.py`. Este archivo generará el recurso **Patient** con los datos proporcionados (por ejemplo, nombre, fecha de nacimiento, etc.) y lo enviará al servidor FHIR.
   
2. **Crear una observación clínica**: Una vez que el paciente haya sido creado, puedes ejecutar `workflow_observation.py` para crear un recurso **Observation**. Este recurso se asociará con el ID del paciente y registrará información clínica relevante, como el valor de temperatura corporal, la unidad de medida, la fecha y hora de la observación, entre otros parámetros.



