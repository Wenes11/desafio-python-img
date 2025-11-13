# Desafio de Projeto: Pacote de Processamento de Imagens

Este repositório contém a resolução do desafio de projeto **"Criando um Pacote de Processamento de Imagens com Python"**, proposto pela [Digital Innovation One (DIO)](https://web.dio.me/).

O objetivo principal é criar um pacote Python robusto para processamento de imagens e publicá-lo (ou simular a publicação), aprendendo sobre a estrutura de empacotamento no Python (`setup.py`, `twine`, etc).

## 📋 Funcionalidades

O pacote oferece funcionalidades modulares para:

- **Processing:**
  - Redimensionamento de imagens.
  - Conversão de cores (ex: RGB para escala de cinza).
- **Utils:**
  - Leitura de imagens.
  - Salvamento de imagens.
  - Plotagem de imagens (visualização).

## 🔧 Instalação

Você pode instalar este pacote localmente clonando o repositório e executando o pip:

```bash
# Clone o repositório
git clone [https://github.com/Wenes11/desafio-python-img.git](https://github.com/Wenes11/desafio-python-img.git)

# Entre na pasta
cd desafio-python-img

# Instale as dependências e o pacote
pip install .
# Importe os módulos (substitua 'nome_do_pacote' pelo nome real da sua pasta)
from nome_do_pacote.utils import read_image, plot_image, save_image
from nome_do_pacote.processing import resize_image, to_gray

# 1. Ler uma imagem
image = read_image("caminho/para/sua/imagem.jpg")

# 2. Processar a imagem (Redimensionar para 50%)
resized_image = resize_image(image, 0.5)

# 3. Converter para escala de cinza
gray_image = to_gray(image)

# 4. Salvar a nova imagem
save_image(gray_image, "imagem_processada.jpg")

# 5. Visualizar o resultado
plot_image(gray_image)
