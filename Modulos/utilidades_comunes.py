# Crear versión corregida de utilidades_comunes.py con funciones ajustadas a rutas parametrizables
import os
import yaml
import pandas as pd
import logging
import time
from datetime import datetime

def inicializar_entorno(nombre_modulo: str, nombre_lote: str, ruta_base: str, ruta_config: str, logger=None) -> dict:
    """
    Inicializa las rutas y configuración base para un módulo de preprocesamiento.
    Incluye validación de existencia y logging informativo.
    """
    try:
        if not os.path.exists(ruta_config):
            raise FileNotFoundError(f"No se encontró el archivo de configuración: {ruta_config}")

        with open(ruta_config, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)

        ruta_modulo = os.path.join(ruta_base, nombre_modulo)
        ruta_salida = os.path.join(ruta_modulo, config["rutas"]["salida"])
        ruta_logs = os.path.join(ruta_modulo, config["rutas"]["logs"])
        ruta_ejemplos = os.path.join(ruta_modulo, config["rutas"]["ejemplos"])

        get_modulo_anterior = lambda m: f"{m.rsplit('_', 1)[0]}_{int(m.rsplit('_', 1)[1]) - 1:02d}"
        nombre_modulo_anterior = get_modulo_anterior(nombre_modulo)

        ruta_entrada = os.path.join(os.path.dirname(ruta_base), "Modulos", nombre_modulo_anterior, config["rutas"]["salida"])

        for ruta in [ruta_salida, ruta_logs, ruta_ejemplos]:
            os.makedirs(ruta, exist_ok=True)

        lote_id = nombre_lote.replace("LOTE_", "")

        if logger:
            logger.info(f"📁 Entorno inicializado para {nombre_modulo}")
            logger.info(f"📂 Ruta entrada: {ruta_entrada}")
            logger.info(f"📂 Ruta salida: {ruta_salida}")
            logger.info(f"📂 Ruta logs: {ruta_logs}")
            logger.info(f"📂 Ruta ejemplos: {ruta_ejemplos}")
            logger.info(f"🔗 Módulo anterior: {nombre_modulo_anterior}")
            logger.info(f"🆔 Lote ID: {lote_id}")

        return {
            "config": config,
            "ruta_entrada": ruta_entrada,
            "ruta_salida": ruta_salida,
            "ruta_logs": ruta_logs,
            "ruta_ejemplos": ruta_ejemplos,
            "ruta_modulo": ruta_modulo,
            "nombre_modulo_anterior": nombre_modulo_anterior,
            "lote_id": lote_id
        }

    except Exception as e:
        msg = f"❌ Error al inicializar el entorno del módulo {nombre_modulo}: {e}"
        if logger:
            logger.error(msg)
        raise RuntimeError(msg)


def cargar_dataset(path: str, logger) -> pd.DataFrame:
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"El archivo no existe: {path}")
        
        _, ext = os.path.splitext(path.lower())
        if ext in ['.csv', '.txt']:
            df = pd.read_csv(path, sep=',', encoding='utf-8', dtype=str)
        elif ext in ['.xls', '.xlsx']:
            df = pd.read_excel(path, dtype=str)
        else:
            raise ValueError(f"Formato no soportado para cargar: {ext}")

        if df.empty:
            logger.warning(f"⚠️ El archivo {path} se cargó pero está vacío. No se continuará el procesamiento.")
            return None

        logger.info(f"✅ Dataset cargado desde {path} ({df.shape[0]} filas, {df.shape[1]} columnas)")
        return df

    except Exception as e:
        logger.error(f"❌ Error técnico al cargar dataset desde {path}: {e}")
        raise RuntimeError(f"No se pudo cargar el dataset desde {path}: {e}")



def mostrar_muestra_dataset(df: pd.DataFrame, nombre_dataset: str, logger, n: int = 5):
    try:
        if df.empty:
            logger.warning(f"⚠️ El dataset '{nombre_dataset}' está vacío. No se muestra muestra ni resumen.")
            return

        # Cabecera
        logger.info(f"--- Muestra de {nombre_dataset} (primeras {n} filas) ---")
        logger.info(f"Filas totales: {df.shape[0]}, Columnas totales: {df.shape[1]}")

        # Tabla de muestra en Markdown
        tabla_md = df.head(n).to_markdown(index=False)
        logger.info("\n" + tabla_md)

        # Estadísticas básicas en Markdown
        resumen = df.describe(include='all').transpose()
        resumen_md = resumen.to_markdown()
        logger.info("\n--- Estadísticas básicas ---\n" + resumen_md)

        logger.info("-" * 60)

    except Exception as e:
        logger.error(f"❌ Error al mostrar muestra del dataset '{nombre_dataset}': {e}")
        raise RuntimeError(f"No se pudo mostrar la muestra de '{nombre_dataset}': {e}")


def guardar_muestra_dataset(df: pd.DataFrame, nombre_base: str, ruta_ejemplos: str, logger, n: int = 5):
    try:
        if df.empty:
            logger.warning(f"⚠️ No se ha guardado muestra '{nombre_base}' porque el DataFrame está vacío.")
            return

        os.makedirs(ruta_ejemplos, exist_ok=True)
        nombre_archivo = os.path.join(ruta_ejemplos, f"muestra_{nombre_base}.csv")
        df.head(n).to_csv(nombre_archivo, index=False, encoding="utf-8")
        logger.info(f"💾 Muestra guardada en {nombre_archivo} ({min(n, df.shape[0])} filas)")

    except Exception as e:
        logger.error(f"❌ Error al guardar muestra '{nombre_base}': {e}")
        raise RuntimeError(f"No se pudo guardar la muestra '{nombre_base}': {e}")


def configurar_logger(nombre_modulo: str, ruta_logs: str = "logs") -> logging.Logger:
    os.makedirs(ruta_logs, exist_ok=True)
    logger = logging.getLogger(nombre_modulo)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(fmt)
        logger.addHandler(ch)

        fh = logging.FileHandler(os.path.join(ruta_logs, f"{nombre_modulo}.log"), mode='a', encoding='utf-8')
        fh.setLevel(logging.INFO)
        fh.setFormatter(fmt)
        logger.addHandler(fh)

    return logger

def guardar_dataset(df: pd.DataFrame, nombre_salida: str, logger):
    try:
        if df.empty:
            logger.warning(f"⚠️ No se ha guardado el dataset porque está vacío: {nombre_salida}")
            return

        os.makedirs(os.path.dirname(nombre_salida), exist_ok=True)
        df.to_csv(nombre_salida, index=False, encoding='utf-8')
        logger.info(f"📦 Dataset guardado en: {nombre_salida} ({df.shape[0]} filas, {df.shape[1]} columnas)")
    except Exception as e:
        logger.error(f"❌ Error al guardar el dataset en {nombre_salida}: {e}")
        raise RuntimeError(f"No se pudo guardar el dataset en {nombre_salida}: {e}")


def comparar_datasets(df_entrada: pd.DataFrame, df_salida: pd.DataFrame, logger):
    try:
        if df_entrada.empty:
            logger.warning("⚠️ El dataset de entrada está vacío.")
        if df_salida.empty:
            logger.warning("⚠️ El dataset de salida está vacío.")

        filas_entrada, cols_entrada = df_entrada.shape
        filas_salida, cols_salida = df_salida.shape

        logger.info(f"📊 Filas entrada: {filas_entrada}, Filas salida: {filas_salida}")
        logger.info(f"📊 Columnas entrada: {cols_entrada}, Columnas salida: {cols_salida}")

        nulls_entrada = df_entrada.isna().sum().sum()
        nulls_salida = df_salida.isna().sum().sum()
        logger.info(f"🕳️ Valores nulos totales - entrada: {nulls_entrada}, salida: {nulls_salida}")

    except Exception as e:
        logger.error(f"❌ Error al comparar los datasets: {e}")
        raise RuntimeError(f"No se pudo comparar los datasets: {e}")


def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        try:
            resultado = func(*args, **kwargs)
            duracion = fin = time.time() - inicio
            logger = kwargs.get("logger", None)
            msg = f"⏱️ '{func.__name__}' completado en {duracion:.2f} s."
            if logger:
                logger.info(msg)
            else:
                print(msg)
            return resultado
        except Exception as e:
            logger = kwargs.get("logger", None)
            msg = f"❌ Error en '{func.__name__}': {e}"
            if logger:
                logger.error(msg)
            else:
                print(msg)
            raise
    return wrapper


def validar_integridad(df: pd.DataFrame, logger):
    try:
        logger.info("🔍 Validando integridad del dataset...")

        if df.empty:
            logger.error("❌ El DataFrame está vacío.")
            raise ValueError("El DataFrame está vacío.")

        # Validar presencia de columnas obligatorias
        columnas_obligatorias = ["nomfichero", "etiqueta", "transcripcion"]
        for col in columnas_obligatorias:
            if col not in df.columns:
                logger.error(f"❌ Falta la columna obligatoria: {col}")
                raise ValueError(f"Falta la columna obligatoria: {col}")
        logger.info(f"✅ Columnas requeridas presentes: {columnas_obligatorias}")
        logger.info(f"📐 Dimensiones del dataset: {df.shape[0]} filas, {df.shape[1]} columnas")

        # Validación de nulos en las columnas obligatorias
        nulos = df[columnas_obligatorias].isna().sum()
        for col, count in nulos.items():
            if count > 0:
                logger.warning(f"⚠️ La columna '{col}' tiene {count} valores nulos")

        # Validar longitud mínima del texto
        textos_invalidos = df["transcripcion"].apply(lambda x: not isinstance(x, str) or len(x.strip()) < 10).sum()
        if textos_invalidos > 0:
            logger.warning(f"⚠️ Se encontraron {textos_invalidos} entradas en 'Texto' vacías o muy cortas")

        logger.info("✅ Validación de integridad completada correctamente.")

    except Exception as e:
        logger.error(f"❌ Error en la validación del dataset: {e}")
        raise RuntimeError(f"No se pudo validar el dataset: {e}")

