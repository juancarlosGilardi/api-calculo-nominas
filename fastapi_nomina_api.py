from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NominaParametros(BaseModel):
    DNI: str
    Codigo_Basico: str
    Sueldo_Base: float
    Horas_Base: float
    Horas_trabajadas: float
    Concepto_Previsional: str
    Porcentaje_previsional: float
    Concepto_Salud: str
    Porcentaje_Salud: float

@app.post("/calcular_conceptos/")
async def calcular_conceptos(parametros: NominaParametros):
    # Cálculo del sueldo proporcional
    sueldo_proporcional = (parametros.Sueldo_Base / parametros.Horas_Base) * parametros.Horas_trabajadas

    # Cálculo del concepto previsional
    valor_previsional = sueldo_proporcional * parametros.Porcentaje_previsional

    # Cálculo del concepto de salud
    valor_salud = sueldo_proporcional * parametros.Porcentaje_Salud

    # Retornar los resultados en el formato requerido
    return {
        "Codigo_Basico": round(sueldo_proporcional, 2),
        "Concepto_Previsional": round(valor_previsional, 2),
        "Concepto_Salud": round(valor_salud, 2)
    }
