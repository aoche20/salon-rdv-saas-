def send_whatsapp_message(phone_number: str, message: str):
    """
    MVP: simulation d'envoi WhatsApp
    En production : brancher WhatsApp Business API
    """
    print(f"[WHATSAPP] → {phone_number}")
    print(message)
