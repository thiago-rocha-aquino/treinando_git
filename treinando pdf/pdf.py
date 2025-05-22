
from fpdf import FPDF

# Conteúdo do resumo
resumo_unidade1 = [
    "Paradigmas de Linguagens – Resumo Express",
    "",
    "1. O que é um Paradigma de Linguagem?",
    "- Paradigma = modelo ou padrão de pensamento.",
    "- Em programação, é como o desenvolvedor organiza o código para resolver problemas.",
    "- Exemplos: programação imperativa, orientada a objetos, funcional etc.",
    "",
    "2. Por que estudar Paradigmas de Linguagens?",
    "- Ajuda a escolher a melhor linguagem para cada projeto.",
    "- Aumenta a capacidade de resolver problemas com código.",
    "- Facilita aprender novas linguagens.",
    "- Dá domínio sobre recursos e limitações das LPs.",
    "",
    "3. Tipos de Tradução de Código:",
    "- Compilação: traduz tudo antes de executar (Ex: C, Ada, COBOL).",
    "- Interpretação: executa linha por linha (Ex: Python, JavaScript).",
    "- Híbrido: compila para bytecode e depois interpreta (Ex: Java).",
    "",
    "Compilado: rápido e direto, mas depende da plataforma.",
    "Interpretado: portátil e simples, mas mais lento.",
    "Híbrido: mistura portabilidade e velocidade moderada.",
    "",
    "4. Processo de Compilação:",
    "1. Analisador léxico",
    "2. Analisador sintático",
    "3. Analisador semântico",
    "4. Código intermediário",
    "5. Código de máquina",
    "",
    "5. Propriedades de uma Boa LP:",
    "- Legibilidade, simplicidade, facilidade de aprendizado.",
    "- Eficiência, reusabilidade, portabilidade.",
    "- Tratamento de exceções: Java, C#, C++.",
    "",
    "6. Escopo de Variáveis:",
    "- Estático: fixado na compilação (Ex: Java, C).",
    "- Dinâmico: muda conforme execução (Ex: Lisp, Perl).",
    "- Tipos de blocos: Monolítico, Não aninhado, Aninhado.",
    "",
    "7. Terminologia Importante:",
    "- Programa-fonte: código do dev.",
    "- Compilador: traduz código.",
    "- Interpretador: executa direto.",
    "- IDE: ambiente com ferramentas de desenvolvimento.",
    "",
    "DICA: Se perguntar sobre tradução para máquina: é Compilação.",
    "Se for sobre velocidade: Compilado. Se for portabilidade: Interpretado ou Java."
]

# Simulado com gabarito
simulado_gabarito = [
    ("1. O que é um paradigma de linguagem?", "C) Um modelo de como estruturar a programação."),
    ("2. Qual tipo de tradução é mais rápido na execução?", "A) Compilação."),
    ("3. Qual linguagem utiliza interpretação híbrida?", "C) Java."),
    ("4. O que é escopo de uma variável?", "B) O local do código onde ela pode ser acessada."),
    ("5. Qual é uma vantagem da interpretação pura?", "D) Portabilidade entre plataformas."),
    ("6. Qual das alternativas representa um bloco aninhado?", "C) Funções dentro de funções."),
    ("7. O que faz o analisador léxico?", "A) Quebra o código em tokens."),
    ("8. Qual linguagem usa indentação como delimitador de bloco?", "D) Python."),
    ("9. O que é legibilidade em uma linguagem?", "C) Facilidade de ler e entender o código."),
    ("10. O que é tratamento de exceção?", "B) Lidar com erros em tempo de execução.")
]

# Criar o PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Página do resumo
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Resumo - Paradigmas de Linguagens (Unidade I)", ln=True, align="C")
pdf.ln(5)
pdf.set_font("Arial", '', 11)
for line in resumo_unidade1:
    pdf.multi_cell(0, 8, line)

# Página do simulado
pdf.add_page()
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Simulado com Gabarito - Paradigmas de Linguagens", ln=True, align="C")
pdf.ln(5)
pdf.set_font("Arial", '', 11)
for q, a in simulado_gabarito:
    pdf.multi_cell(0, 8, q)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 8, f"→ Gabarito: {a}")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)

# Salvar o PDF
pdf_path = "/mnt/data/Resumo_Simulado_Paradigmas_Unidade1.pdf"
pdf.output(pdf_path)

pdf_path
