import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from config.config import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD  # Importar as configurações

def send_email():
    # Criar um objeto de mensagem de email multipart e definir cabeçalhos
    msg = MIMEMultipart()
    msg["From"], msg["To"], msg["Subject"] = SENDER_EMAIL, RECEIVER_EMAIL, "Análise de Manutenção de Máquinas"

    # Anexar o arquivo de log
    with open("./logs/analysis_results.txt", "r") as f:
        msg.attach(MIMEText(f.read(), "plain"))

    # Anexar o arquivo de log como anexo
    filename = "analysis_results.txt"
    attachment = open("./logs/analysis_results.txt", "rb")
    base = MIMEBase("application", "octet-stream")
    base.set_payload(attachment.read())
    encoders.encode_base64(base)
    base.add_header("Content-Disposition", f"attachment; filename={filename}")
    msg.attach(base)

    # Conectar ao servidor e enviar o email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("Email enviado com sucesso.")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

if __name__ == "__main__":
    send_email()
