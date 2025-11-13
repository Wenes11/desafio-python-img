from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_system_dio",  # Mude para um nome único se for subir pro PyPI
    version="0.0.1",
    author="Seu Nome",
    author_email="seu_email@exemplo.com",
    description="Um pacote simples de processamento de imagens para o desafio da DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="link_do_seu_github",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)