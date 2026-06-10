class EmailService:
    def send_new_message_email(
        self,
        receiver_email: str,
        sender_name: str,
        message_content: str
    ):
        print("========== EMAIL NOTIFICATION ==========")
        print(f"To: {receiver_email}")
        print("Subject: You received a new message")
        print(f"Body: {sender_name} sent you a message:")
        print(message_content)
        print("========================================")