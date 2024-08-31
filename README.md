---

# Script de Inferência de Imagens com YOLOv5

Este script utiliza o modelo YOLOv5 para realizar a detecção de objetos em todas as imagens `.jpg` dentro de um diretório especificado. Os resultados são impressos no console e salvos em um diretório de saída designado.

## Pré-requisitos

Antes de executar o script, certifique-se de que você tem os seguintes requisitos instalados:

- Python 3.7 ou superior
- PyTorch
- `ultralytics/yolov5` via PyTorch Hub

Você pode instalar os pacotes necessários usando pip:

```bash
pip install torch torchvision
```

## Como Usar

1. **Prepare as Imagens:**

   Coloque todas as imagens `.jpg` que você deseja processar no diretório `yolov5/data/images/`.

2. **Execute o Script:**

   Use o seguinte comando para executar o script:

   ```bash
   python seu_script.py
   ```

3. **Resultados:**

   - O script imprimirá os resultados da inferência no console, incluindo as classes detectadas e as coordenadas dos bounding boxes.
   - As imagens com as detecções desenhadas (bounding boxes e rótulos) serão salvas no diretório `detect/exp`. Se você executar o script várias vezes, o diretório será sobrescrito para evitar a criação de múltiplas pastas (`exp2`, `exp3`, etc.).

## Funcionamento do Script

- **Carregamento do Modelo:**
  O modelo YOLOv5 é carregado utilizando o PyTorch Hub.

- **Inferência:**
  O script realiza inferência em todas as imagens `.jpg` encontradas no diretório especificado.

- **Resultados:**
  - As predições são impressas no console.
  - As imagens processadas são salvas em `detect/exp`.
  - Você pode acessar as predições em formato tensor ou em um DataFrame do Pandas.

## Exemplo de Código

```python
from pathlib import Path
import torch

pasta_imagens = Path("yolov5/data/images/")
arquivos_jpg = list(pasta_imagens.glob("*.jpg"))

# Modelo
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

# Inferência
results = model(arquivos_jpg)

# Resultados
results.print()
results.save()

results.xyxy[0] 
results.pandas().xyxy[0]
```

---
