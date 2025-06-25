## Patient
Creación del recurso paciente con algunos parámetros. 

## Base 
Lectura y escritura de recursos en el servidor público de HAPI FHIR. 

## Workflow
### `workflow.py` - Crear un paciente

Este archivo crea un recurso **Patient** con los siguientes parámetros:

- **family_name**: Apellido del paciente.
- **given_name**: Nombre del paciente.
- **birth_date**: Fecha de nacimiento.
- **gender**: Género.
- **phone**: Teléfono (opcional).
- **identifier**: Identificador único del paciente (por ejemplo, un número de seguro social).

Una vez creado el paciente, se envía al servidor FHIR y se obtiene el ID del paciente. 
