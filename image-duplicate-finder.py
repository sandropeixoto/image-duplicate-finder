import os
from PIL import Image
import imagehash
from collections import defaultdict
import sys

def find_duplicate_images(root_folder, auto_delete=None):
    # Dicionário para armazenar os hashes e os caminhos das imagens
    hash_dict = defaultdict(list)

    # Coleta todos os caminhos de imagens nas subpastas
    image_paths = []
    for foldername, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                image_paths.append(os.path.join(foldername, filename))

    total_images = len(image_paths)
    print(f"Total de imagens encontradas: {total_images}")

    # Processa cada imagem e calcula o hash
    for idx, filepath in enumerate(image_paths):
        try:
            # Calcula o hash perceptual da imagem
            image = Image.open(filepath)
            hash_value = imagehash.phash(image)

            # Armazena o caminho do arquivo no dicionário com o hash como chave
            hash_dict[hash_value].append(filepath)

            # Atualiza o progresso
            progress = (idx + 1) / total_images * 100
            print(f"Progresso: {progress:.2f}% - {filepath}", end='\r')
        except Exception as e:
            print(f"Erro ao processar {filepath}: {e}")

    print("\n")  # Para mover para a próxima linha após o progresso

    # Exibe as imagens duplicadas/semelehantes
    duplicates = {hash_value: paths for hash_value, paths in hash_dict.items() if len(paths) > 1}
    
    if duplicates:
        print("Imagens duplicadas ou semelhantes encontradas:")
        for hash_value, file_list in duplicates.items():
            print(f"\nHash: {hash_value}")
            for file_path in file_list:
                print(f" - {file_path}")

        # Pergunta se deseja apagar as duplicatas, caso não tenha sido especificado o parâmetro
        if auto_delete is None:
            user_input = input("\nDeseja apagar todas as imagens duplicadas encontradas? (s/n): ").strip().lower()
            if user_input == 's':
                auto_delete = True
            else:
                auto_delete = False

        # Apaga os arquivos duplicados se auto_delete for True
        if auto_delete:
            for hash_value, file_list in duplicates.items():
                # Mantém o primeiro arquivo e apaga os outros
                for file_path in file_list[1:]:
                    try:
                        os.remove(file_path)
                        print(f"Apagado: {file_path}")
                    except Exception as e:
                        print(f"Erro ao apagar {file_path}: {e}")
            print("Arquivos duplicados foram apagados.")
        else:
            print("Nenhum arquivo foi apagado.")
    else:
        print("Nenhuma imagem duplicada ou semelhante encontrada.")

if __name__ == "__main__":
    # Verifica argumentos de linha de comando para /y ou /n
    auto_delete_param = None
    if len(sys.argv) > 2:
        root_folder = sys.argv[1]
        if sys.argv[2].lower() == '/y':
            auto_delete_param = True
        elif sys.argv[2].lower() == '/n':
            auto_delete_param = False
    elif len(sys.argv) > 1:
        root_folder = sys.argv[1]
    else:
        root_folder = input("Digite o caminho para a pasta de busca: ")

    find_duplicate_images(root_folder, auto_delete=auto_delete_param)