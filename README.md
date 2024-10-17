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

## Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/image-duplicate-finder.git

2. Acesse o diretório do projeto:
   ```bash
   cd image-duplicate-finder

3. Instale as dependências necessárias:
   ```bash
   pip install Pillow imagehash

4. Execute o script:
   ```bash
    python find_duplicate_images.py <caminho_da_pasta> [/y | /n]

<caminho_da_pasta>: Caminho para a pasta onde as imagens serão analisadas.
/y: (Opcional) Apaga automaticamente as duplicatas encontradas.
/n: (Opcional) Não apaga as duplicatas.
Se nenhum argumento /y ou /n for fornecido, o script perguntará ao usuário se deseja apagar as duplicatas encontradas.

