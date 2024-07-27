from setuptools import setup, find_packages

# Leitura do arquivo README.md para a descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="diabetesriskprediction",  # Nome do pacote
    version="0.1.0",  # Versão inicial do pacote
    author="Brenda Sclauser e Caio França",
    author_email="brendasclauser@hotmail.com e kaio_cfs@hotmail.com",
    description="Pacote com modelo de machine learning responsável por classificar o risco a diabetes com intuito de produtizar utilizando pipeline de MLops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Foiac/diabetesriskprediction",  # URL do repositório do projeto
    packages=find_packages(where="src"),  # Localiza todos os pacotes na pasta src
    package_dir={"": "src"},  # Indica que o código está na pasta src
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Tipo de licença (exemplo: MIT)
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versão mínima do Python
    install_requires=[  # Dependências necessárias
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
    ],
    extras_require={  # Dependências opcionais
        "dev": ["pytest", "black"],
    },
    entry_points={  # Pontos de entrada para comandos de linha de comando
        "console_scripts": [
            "comando=src:main",
        ],
    },
)
