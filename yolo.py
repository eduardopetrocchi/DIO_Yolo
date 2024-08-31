from pathlib import Path
import torch

pasta_imagens = Path("yolov5/data/images/")
arquivos_jpg = list(pasta_imagens.glob("*.jpg"))

#Model
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

# Inference
results = model(arquivos_jpg)

# Results
results.print()
results.save()

results.xyxy[0] 
results.pandas().xyxy[0] 