# 🏦 Sistema Bancário V3


> Este projeto é um desafio disponibilizado pela plataforma **[DIO](https://www.dio.me/)** e faz parte do bootcamp **Vivo - Python AI Backend Developer**.

O objetivo desse projeto foi **remodelar** o [Sistema Bancário V2](https://github.com/KbeloN/Sistema-bancarioV2) para seguir os **paradigimas de Programação Orientada a Objetos (POO)** em Python.

## ✨ Evoluções e Principais Diferênças (V2 para V3)

 - **Refeito em POO:** Conversão completa de funções procedurais para **Classes** e **Objetos**.
 - **Modularizado:** As funcionalidades foram estruturadas em **métodos**, o que melhora a manutenibilidade do código e promove o **reúso**.
 - **Encapsulamento:** Os atributos foram encapsulados para garantir a segurança e **integridade** dos dados bancários.
 - **Herança e Polimorfismo:** 
    - **Herança:** Foi aplicada na classe `Fisica` (Herdada de `Cliente`), `Deposito` e `Saque` (Ambas de `Transacao`).
    - **Polimorfismo:** Usado no método **construtor** (`__init__`) da classe `Fisica` e no **registro de transações** em `Transacoes`.

## 📌 Funcionalidades

- **Menu Inicial**
    * Criar novo usuário
    * Entrar no usuário
    * ~~Listar usuários no sistema~~ (Removida por não ser necessária no contexto do sistema)
    * Sair do sistema
- **Menu do Usuário**
    * Depositar
    * Sacar
    * Exibir Histórico (De cada conta individual)
    * Criar nova conta
    * Listar contas
    * Voltar ao menu inicial

## ⚙️ Requisitos:
- **Python 3**
