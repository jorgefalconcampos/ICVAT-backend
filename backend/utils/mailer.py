from django.core import mail #EmailMessage lives here
from django.utils.text import format_lazy as fl
from django.conf import settings as conf_settings
from django.template.loader import render_to_string
# from django.utils.translation import ugettext_lazy as _
from django.core.mail.backends.smtp import EmailBackend
from django.core.mail import send_mail, get_connection, send_mass_mail


class BaseMailer():
    def __init__(self, message_to, context, subject, template, sndr_host, sndr_username, sndr_pass, sndr_port, sndr_tls, **substitutions):

        self.con = mail.get_connection()

        self.message_to = message_to
        self.subject = subject
        self.body_msg = render_to_string(template, context)
        
        self.sndr_host = sndr_host
        self.sndr_port = sndr_port
        self.sndr_username = sndr_username
        self.sndr_pass = sndr_pass
        self.sndr_tls = sndr_tls

        self.substitutions = {}

        for key in substitutions:
            self.substitutions.update({key:substitutions[key]})


    def create_email(self):
        # creating connection
        self.con.open()

        #filling the connection (EmailBackend) object
        self.mail_obj = EmailBackend(
            host=self.sndr_host, 
            port=self.sndr_port,
            username=self.sndr_username,
            password=self.sndr_pass,
            use_tls=self.sndr_tls
            )

        # filling the EmailMessage object
        self.mail = mail.EmailMessage(
            subject=self.subject, 
            body=self.body_msg, 
            from_email=self.sndr_username,
            to=[self.message_to],
            connection=self.con
            )
  

    def send_email(self):
        self.create_email()
        try:
            self.mail.content_subtype = 'html'
            # self.con.send_messages([self.mail]) #sending email with the current connection, this is intended to send messages to multiple mails w/ the same conn
            # self.mail.send(self.mail) #sending email with the EmailMessage object
            self.mail_obj.send_messages([self.mail]) #sending email with EmailBackend
            self.con.close()
            return True
        except Exception as e:
            print(f'\n\n# --- PY: Error sending email: --- #\n{e}')
            return False



class SendResetPasswordMail(BaseMailer):
    def __init__(self, message_to, context, **substitutions):
        super().__init__(
            message_to, 
            context, 
            subject = fl("ICVAT | Recuperación de contraseña para {}", substitutions["username"]), 
            template = "users/pwd/password-reset.html", 
            sndr_host = conf_settings.EMAIL_HOST, 
            sndr_username = conf_settings.EMAIL_HOST_USER, 
            sndr_pass = conf_settings.EMAIL_HOST_PASSWORD, 
            sndr_port = conf_settings.EMAIL_PORT,
            sndr_tls = conf_settings.EMAIL_USE_TLS,
            **substitutions
        )
