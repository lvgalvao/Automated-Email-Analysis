# Projeto de Automatização de Análise e E-mail

## Case

Link: [Consolidador de arquivos](https://www.linkedin.com/posts/lucianovasconcelosf_j%C3%A1-imaginou-ter-que-combinar-mais-de-100-activity-7097904543446839296-CFIp?utm_source=share&utm_medium=member_desktop)

## Descrição

Automatize suas análises e comunicações por e-mail em um piscar de olhos. Economize até 3 horas semanais com apenas três scripts Python. Este projeto oferece uma solução completa para análise de manutenção de máquinas e envio automatizado de relatórios via e-mail.

## Requisitos

* Python 3.x
* Pandas
* smtplib
* email

## Instalação

Clone este repositório e instale as dependências:

```bash
git clone https://github.com/lvgalvao/Automated-Email-Analysis.git
cd automated-Email-Analysis
pip install -r requirements.txt
```

## Uso

1. Configure as informações de e-mail em `config.py`.
2. Coloque o seu dataset CSV na pasta `data`.
3. Execute `data_analysis.py` para realizar as análises.
4. Execute `email_automation.py` para enviar o e-mail.

## Scripts

### Data Analysis (`data_analysis.py`)

Utiliza a biblioteca Pandas para automatizar a análise de dados sobre a manutenção de máquinas. Calcula médias, identifica máquinas que precisam de manutenção e registra códigos de erro.

### Email Automation (`email_automation.py`)

Automatiza o envio de relatórios de análise usando as bibliotecas `smtplib` e `email`. Lê os resultados das análises e os envia via Gmail para o destinatário especificado.

## Conclusão

Combinando análise de dados e comunicação automatizada, este projeto torna possível economizar até três horas por semana, permitindo um foco maior em tarefas críticas.
