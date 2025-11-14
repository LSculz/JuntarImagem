# 🖼️ Combinação de Imagens Lado a Lado (Pillow/PIL)

Este é um script em Python que utiliza a biblioteca **Pillow (PIL)** para combinar duas imagens, lado a lado, em um único arquivo. O script é inteligente o suficiente para **ajustar automaticamente a altura** da segunda imagem (mantendo sua proporção) para que ela corresponda à altura da primeira imagem antes da combinação, garantindo um resultado visualmente coeso.

---

## ✨ Funcionalidades

* **Combinação Simples:** Junta `imagem1.jpg` e `imagem2.jpg` horizontalmente.
* **Ajuste Automático de Altura:** Redimensiona a segunda imagem se as alturas forem diferentes para evitar desalinhamentos.
* **Qualidade:** Utiliza o filtro `Image.LANCZOS` para um redimensionamento de alta qualidade.
* **Saída PNG:** Salva o arquivo final como `imagem_combinada.png`.

---

## 🛠️ Pré-requisitos

Para executar este script, você precisará ter o Python instalado e a biblioteca `Pillow`.

### Instalação da Pillow

```bash
pip install Pillow


```
## 🚀 Como Usar
Prepare os Arquivos:

Certifique-se de que o seu script Python e as duas imagens que deseja combinar (imagem1.jpg e imagem2.jpg) estejam no mesmo diretório.
Observação: Se suas imagens tiverem nomes diferentes, ajuste as chamadas Image.open() no script.

Execute o Script:
Abra o terminal ou prompt de comando no diretório do script e execute:
````
Bash

python seu_script_aqui.py
(Substitua seu_script_aqui.py pelo nome do seu arquivo Python.)

````
Resultado:

Uma nova imagem chamada imagem_combinada.png será criada no mesmo diretório.
