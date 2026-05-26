import math
from flask import render_template, request

def calcular():
    try:
        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]
    except (KeyError, ValueError):
        return render_template(
            "calculadora.html",
            etapas="Erro: Dados inválidos informados.",
            resultados=""
        )

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√({num1}) = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro: menor ou igual a zero"
            etapas = f"Não existe logaritmo real para {num1}."
        else:
            resultado = math.log(num1)
            etapas = f"ln({num1}) = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="",
        )
    
    try:
        num2 = float(num2_valor)
    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Erro: Segundo número inválido.",
            resultados=""
        )

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            resultado = "Erro: Divisão por zero"
            etapas = f"Não é possível dividir {num1} por zero."
        else:
            resultado = num1 / num2
            etapas = f"{num1} ÷ {num2} = {resultado}"
    elif operacao == "**":
        resultado = num1 ** num2
        etapas = f"{num1} ^ {num2} = {resultado}"
    else:
        resultado = "Erro"
        etapas = "Operação inválida selecionada."

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)
