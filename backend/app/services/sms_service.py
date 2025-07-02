import os
import random

def generate_sms_code(length: int = 6) -> str:
    """Gera um código numérico aleatório para verificação por SMS."""
    return "".join([str(random.randint(0, 9)) for _ in range(length)])

async def send_sms(phone_number: str, message: str) -> bool:
    """
    Simula o envio de um SMS para o número de telefone fornecido.
    Em produção, integraria com um gateway de SMS real.
    """
    # Exemplo com Twilio (requer TWILIO_ACCOUNT_SID e TWILIO_AUTH_TOKEN nas variáveis de ambiente)
    # from twilio.rest import Client
    # account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    # auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    # twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
    #
    # if not all([account_sid, auth_token, twilio_phone_number]):
    #     print("ATENÇÃO: Credenciais Twilio não configuradas. SMS não será enviado.")
    #     return False
    #
    # client = Client(account_sid, auth_token)
    # try:
    #     message = client.messages.create(
    #         to=phone_number,
    #         from_=twilio_phone_number,
    #         body=message
    #     )
    #     print(f"SMS enviado para {phone_number} com SID: {message.sid}")
    #     return True
    # except Exception as e:
    #     print(f"Erro ao enviar SMS para {phone_number}: {e}")
    #     return False

    # Simulação para desenvolvimento
    print(f"SIMULANDO ENVIO DE SMS:")
    print(f"Para: {phone_number}")
    print(f"Mensagem: {message}")
    return True