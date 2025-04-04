import os
import zipfile
from pathlib import Path  # added for cog
import cog  # added for cog
from rfdetr import RFDETRBase

def unzip_dataset(zip_path, extract_to):
    if os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Dataset unzipped to {extract_to}")
    else:
        print("Zip file does not exist.")
        exit(1)
    return extract_to

def train_model(dataset_dir):
    model = RFDETRBase()
    model.train(dataset_dir=dataset_dir, epochs=100, batch_size=2, grad_accum_steps=4, lr=1e-4)
    weights_file = 'rf_detr_weights.pt'
    model.save(weights_file)
    zip_filename = 'rf_detr_weights.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        zipf.write(weights_file)
    print(f"Weights saved and zipped as {zip_filename}")
    return zip_filename

class Predictor(cog.Predictor):
    def setup(self):
        pass

    @cog.input("dataset", type=Path, help="Path to the COCO formatted dataset zip file")
    def predict(self, dataset: Path) -> Path:
        dataset_zip = str(dataset)
        dataset_dir = os.path.splitext(dataset_zip)[0]
        dataset_dir = unzip_dataset(dataset_zip, dataset_dir)
        weights_zip = train_model(dataset_dir)
        return Path(weights_zip)
