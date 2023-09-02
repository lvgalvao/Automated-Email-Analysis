import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.config import SENDER_EMAIL, RECEIVER_EMAIL, PASSWORD  # Importar as configurações

def send_email():
    # Criar um objeto de mensagem de email multipart e definir cabeçalhos
    msg = MIMEMultipart()
    msg["From"], msg["To"], msg["Subject"] = SENDER_EMAIL, RECEIVER_EMAIL, "Análise de Manutenção de Máquinas"

    # Anexar o arquivo de log
    with open("./logs/analysis_results.txt", "r") as f:
        msg.attach(MIMEText(f.read(), "plain"))

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
