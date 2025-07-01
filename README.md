# Proyecto Fin de Máster: Análisis del Comportamiento de Cliente (NPS) usando IA

Este repositorio contiene todo el material de mi Trabajo de Fin de Máster (TFM) en Inteligencia Artificial, centrado en el análisis de sentimiento de transcripciones de llamadas de atención al cliente para una aseguradora de decesos.

---

## 📂 Estructura del repositorio

```
Proyecto_Fin_Master/
├── DATA/               # Conjuntos de datos utilizados. Son carpetas que contienen las transcripciones de las llamadas que son documentos de texto planos
│   ├── LOTE_202050605
│   ├── LOTE_AAAAMMDD
│   └── ...
├── Documentos/         # Documentación principal y soporte
│   ├── Memoria_TFM.pdf           # Documento final de la memoria
│   ├── TFM_DIAGRAMAS_PROPIOS.pptx # Diapositivas con diagramas propios
│   └── ...
└── Modulos/            # Código y notebooks por módulos
    ├── MODULO_01/
    ├── MODULO_02/
    ├── MODULO_03/
    ├── MODULO_04/
    ├── MODULO_05/
    ├── MODULO_06/
    ├── MODULO_07/
    ├── PLANTILLA_MODULO_PREPROCESAMIENTO.ipynb
    ├── config.Yaml
    └── utilidades_comunes.py
```

## 🎯 Descripción general

1. **DATA**  
   Conjuntos de datos originales.
   Se pueden ir creando nuevas carpetas con transcripciones para procesar, dichas carpetas tienen una nomenclatura especifica 
   que luego utilizan los módulos del proceso. Se nombran como LOTES, así: LOTE_aaaammdd

2. **Documentos**  
   - **Memoria_TFM.pdf**: Informe final del TFM.  
   - **TFM_DIAGRAMAS_PROPIOS.pptx**: Diapositivas con los diagramas y la arquitectura.

3. **Modulos**  
   Cada carpeta `MODULO_0X` incluye:
   - Un notebook `.ipynb` con el código y explicación.
   - Subcarpetas `salida/` 'logs/' y `ejemplos/` con CSV, logs y ficheros de muestra.

   Además:
   - **PLANTILLA_MODULO_PREPROCESAMIENTO.ipynb**: es la plantilla de pasos básicos que tienen que tener todos los módulos.
   - **config.Yaml**: fichero de configuracion
   - **utilidades_comunes.py**: Funciones de uso recurrente.

---

## 🚀 Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/emmartinc/Proyecto_Fin_Master.git
   cd Proyecto_Fin_Master
   ```

2. Crea un entorno de Python e instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Define tu token de Hugging Face en un archivo local `.env` (no subido):
   ```
   HUGGINGFACE_TOKEN=hf_xxx...
   ```

4. Abre los notebooks en orden (01 → 07) y ejecútalos para replicar el flujo completo.

---
Aunque el proceso está pensado para ejecutarse secuencialmente, es lo suficientemente flexible para que se puedan ejecutar los módulos de forma independiente
