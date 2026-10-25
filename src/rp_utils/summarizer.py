
from pathlib import Path


class DatasetSummarizer:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def generar_resumen(self, filename):
        df = self.dataframe

        lineas = [
            "RESUMEN DEL DATASET",
            "=" * 40,
            f"Cantidad de filas: {df.shape[0]}",
            f"Cantidad de columnas: {df.shape[1]}",
            "",
            "NOMBRES Y TIPOS DE DATOS",
            "-" * 40,
            df.dtypes.to_string(),
            "",
            "VALORES NULOS POR COLUMNA",
            "-" * 40,
            df.isnull().sum().to_string(),
            "",
            "ESTADISTICAS DESCRIPTIVAS",
            "-" * 40,
            df.describe(include="all").to_string()
        ]

        ruta = Path(filename)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text("\n".join(lineas), encoding="utf-8")

        print(f"Resumen guardado en: {ruta.resolve()}")
