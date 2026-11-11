
loader = HFDatasetLoader("scikit-learn/iris", split="train")
df = loader.load()

print("Dimensiones originales:", df.shape)
display(df.head())

df_transformado = df.rename(
    columns={"SepalLengthCm": "longitud_sepalo"}
)

print("Transformación: renombré SepalLengthCm a longitud_sepalo.")
display(df_transformado.head())




class HFDatasetLoader:
    def __init__(self, dataset_name, split="train", config=None):
        self.dataset_name = dataset_name
        self.split = split
        self.config = config

    def load(self):
        dataset = load_dataset(
            self.dataset_name,
            name=self.config,
            split=self.split
        )

        dataframe = dataset.to_pandas()
        return dataframe
