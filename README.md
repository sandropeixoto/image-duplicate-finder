# Image Duplicate Finder

Este projeto é um script em Python que permite encontrar imagens duplicadas ou semelhantes em uma pasta. Ele utiliza a biblioteca `imagehash` para calcular o hash perceptual das imagens e identificar arquivos duplicados.

## Funcionalidades

- Detecta imagens duplicadas ou semelhantes em uma pasta.
- Opcionalmente, apaga automaticamente as duplicatas encontradas.
- Suporta vários formatos de imagem, incluindo `.png`, `.jpg`, `.jpeg`, `.bmp`, `.gif` e `.tiff`.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `Pillow`
  - `imagehash`

Para instalar as bibliotecas necessárias, execute:
```bash
pip install Pillow imagehash
