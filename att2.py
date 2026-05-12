from flask import Flask, render_template_string

app = Flask(__name__)

# Template HTML centralizado em uma única variável
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - {{ nome }}</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 40px auto; padding: 20px; background-color: #f4f4f4; }
        .container { background: white; padding: 40px; border-top: 8px solid #b71c1c; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
        h1 { color: #b71c1c; margin-bottom: 5px; text-transform: uppercase; text-align: center; }
        h2 { border-bottom: 2px solid #b71c1c; color: #b71c1c; padding-bottom: 5px; margin-top: 30px; text-transform: uppercase; font-size: 1.2em; }
        .info { text-align: center; margin-bottom: 30px; font-size: 0.9em; color: #666; }
        ul { list-style-type: none; padding: 0; }
        li { margin-bottom: 8px; }
        li:before { content: "• "; color: #b71c1c; font-weight: bold; }
        .data { font-weight: bold; color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ nome }}</h1>
        <div class="info">
            <p>{{ idade }} ANOS</p>
            <p>{{ endereco }}</p>
            <p>Telefone: {{ telefone }} | Email: {{ email }}</p>
        </div>

        <h2>Objetivos</h2>
        <ul>
            <li>Aprimorar o conhecimento na utilização do sistema operacional Windows</li>
            <li>Aperfeiçoar habilidades com aplicativos Windows</li>
            <li>Busco qualificação na área de informática para aperfeiçoamento do curso técnico</li>
        </ul>

        <h2>Formação</h2>
        <ul>
            <li><span class="data">2023:</span> Colégio Santa Maria - Ensino Fundamental II (Pampulha)</li>
            <li><span class="data">2024:</span> COTEMIG - Técnico em Informática (1ª série - Floresta)</li>
            <li><span class="data">2025:</span> COTEMIG - Técnico em Informática (2ª série - Em andamento)</li>
        </ul>

        <h2>Habilidades</h2>
        <ul>
            <li>Operar e configurar sistemas Windows e Linux</li>
            <li>Domínio de Pacote Office e Google Workspace</li>
            <li>Montagem e manutenção de computadores</li>
        </ul>

        <h2>Qualificações</h2>
        <ul>
            <li>Wizard: Inglês Intermediário Nível 2</li>
            <li>Menor Aprendiz Administrativo (2022)</li>
            <li>MCC - Montagem e Configuração de Computadores (2024)</li>
            <li>Robótica (2024)</li>
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    # Dados extraídos do seu PDF
    dados = {
        "nome": "SARAH BEATRIZ SILVEIRA CAMPOS",
        "idade": 19,
        "endereco": "Avenida General Olímpio Mourão Filho 676, Ap1001 – Planalto /Itapuã – BH/MG",
        "telefone": "(31) 98462-5376",
        "email": "sarahbscampos@gmail.com"
    }
    return render_template_string(HTML_TEMPLATE, **dados)

if __name__ == '__main__':
    app.run(debug=True)