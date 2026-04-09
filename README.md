# 📱 Sistema de Contatos em Python (CLI)

## 📌 Descrição

Este projeto é um sistema simples de gerenciamento de contatos desenvolvido em Python.

O sistema permite adicionar, listar e armazenar contatos em um arquivo `.txt`, garantindo validação de dados e evitando duplicações.

---

## 🚀 Funcionalidades

* ✅ Adicionar contatos
* ✅ Listar contatos
* ✅ Validação de nome (não permite números)
* ✅ Validação de telefone (apenas números e 11 dígitos)
* ✅ Padronização automática de nomes
* ✅ Formatação de telefone na exibição
* ✅ Verificação de contatos duplicados
* ✅ Salvamento em arquivo `.txt`

---

## 🛠 Tecnologias utilizadas

* Python 3.13

---

## ▶️ Como executar o projeto

1. Clone o repositório:

```
git clone https://github.com/AxelOliveira/sistema_de_contatos_version_2.git
```

2. Acesse a pasta do projeto:

```
cd sistema_de_contatos_version_2
```

3. Execute o arquivo:

```
python main.py
```

---

## 💻 Exemplo de uso

```
Comandos: adicionar, listar, sair
Digite um comando: adicionar

Digite o nome do contato: joao silva
Digite o número do contato: 62999999999

Contato adicionado com sucesso!

Comandos: adicionar, listar, sair
Digite um comando: listar

João Silva - (62) 9 9999-9999
```

---

## 📂 Estrutura do projeto

* `main.py` → código principal
* `contatos.txt` → arquivo onde os contatos são salvos

---

## ⚠️ Observações

* Os telefones são armazenados sem formatação para facilitar validações
* O telefone deve conter exatamente 11 dígitos
* A formatação `(XX) X XXXX-XXXX` é aplicada apenas na exibição

---

## 📌 Melhorias futuras

* 🔄 Editar contatos
* 🔍 Buscar contatos
* ❌ Remover contatos com seleção
* 📊 Interface gráfica

---

## 👨‍💻 Autor

Desenvolvido por Axel Oliveira
Projeto com foco em aprendizado de lógica de programação e Python.
