# Proyecto FHIR - TP6

Este proyecto implementa el estándar **FHIR (Fast Healthcare Interoperability Resources)** para crear y gestionar recursos de salud, específicamente de **pacientes** y obtener las **Observaciones** que presentan. El objetivo es crear y gestionar los recursos **Patient** y **Observaciones**.

### Descripción de los Archivos

- **base.py**: Contiene las funciones para interactuar con el servidor FHIR (enviar recursos y obtener recursos).
- **patient.py**: Contiene la función para crear el recurso **Patient**.
- **workflow.py**: Define el flujo de trabajo para crear un paciente y enviar el recurso **Patient** al servidor.
- **Observation.py**: 
- **Test.py**:

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
