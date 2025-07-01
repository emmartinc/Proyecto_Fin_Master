# Proyecto Fin de Máster: Análisis del Comportamiento de Cliente (NPS) usando IA

Este repositorio contiene todo el material de mi Trabajo de Fin de Máster (TFM) en Inteligencia Artificial, centrado en el análisis de sentimiento de transcripciones de llamadas de atención al cliente para una aseguradora de decesos.

---

## 📂 Estructura del repositorio

```
Proyecto_Fin_Master/
├── DATA/               # Conjuntos de datos utilizados y resultados
│   ├── dataset_reducido.csv
│   ├── dataset_completo.csv
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
    ├── TXT_A_DATASET.ipynb
    └── utilidades_comunes.py
```

---

## 🎯 Descripción general

1. **DATA**  
   Conjuntos de datos originales y versiones procesadas (CSV).

2. **Documentos**  
   - **Memoria_TFM.pdf**: Informe final del TFM.  
   - **TFM_DIAGRAMAS_PROPIOS.pptx**: Diapositivas con los diagramas y la arquitectura.

3. **Modulos**  
   Cada carpeta `MODULO_0X` incluye:
   - Un notebook `.ipynb` con el código y explicación.
   - Subcarpetas `salida/` y `ejemplos/` con CSV, logs y ficheros de muestra.

   Además:
   - **PLANTILLA_MODULO_PREPROCESAMIENTO.ipynb**: Guía de preprocesamiento.
   - **TXT_A_DATASET.ipynb**: Conversión de transcripciones a CSV.
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

## 📄 Licencia y Contacto

- **Licencia**: MIT  
- **Contacto**:  
  Eva Martín — evamartin@example.com  
  LinkedIn: https://www.linkedin.com/in/evamartin  
``` ````

---

### Paso 2: Pégalo en tu `README.md`

- Borra lo que tengas actualmente en `README.md`.
- Pega el bloque anterior completo.
- Guarda (Ctrl+S).

### Paso 3: Commit y push

En Git Bash:

```bash
git add README.md
git commit -m "Añadido README con estructura y guía de uso"
git push origin master
```
