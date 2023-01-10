import os
import smtplib
import ssl
from email.mime import multipart, text
from email.utils import formataddr
from typing import Optional, List, Union
import pydantic
from backend.lib.mail import exception
from backend.lib.mail import template_finder
from backend.core.config import settings


class Mailer(template_finder.MailTemplate):
    def __init__(
            self,
            subject: str,
            sender_email: Optional[pydantic.EmailStr] = None,
            sender_password: Optional[str] = None,
            email_server: Optional[str] = None,
            email_server_port: Optional[int] = None,
            template_folder: Optional[pydantic.DirectoryPath] = settings.TEMPLATE_DIR,
            website_name: str = settings.PROJECT_NAME,
            use_google: Optional[bool] = True,
            body: Optional[str] = None,
            template_name: Optional[str] = None,
            context=None,
    ) -> None:
        super().__init__(template_folder)
        if context is None:
            context = {}
        self.admin_email = sender_email
        self.admin_password = sender_password
        self.template_name = template_name
        self.email_server = email_server
        self.email_server_port = email_server_port
        self.use_google = use_google
        self.website_name = website_name
        self.body = body
        self.context = context
        self.subject = subject

    def __check_credential(self) -> None:
        if not self.admin_email:
            _check_email = settings.ADMIN_EMAIL
            if not _check_email:
                raise exception.InvalidCredentialError(
                    "Sender email can not be empty, either set 'ADMIN_EMAIL' in your envionment, or provide one"
                )
            self.admin_email = settings.ADMIN_EMAIL

        if not self.admin_password:
            _check_password = settings.ADMIN_PASSWORD
            if not _check_password:
                raise exception.InvalidCredentialError(
                    "Sender password can not be empty, either set 'ADMIN_PASSWORD' in your envionment, or provide one"
                )
            self.admin_password = settings.ADMIN_PASSWORD

        if not self.email_server:
            if not self.use_google:
                raise exception.InvalidCredentialError(
                    "email server  can not be empty, either set 'EMAIL_SERVER' in your envionment, or 'use_google' to "
                    "true"
                )
            self.email_server = settings.EMAIL_SERVER

        if not self.email_server_port:
            if not self.use_google:
                raise exception.InvalidCredentialError(
                    "email server port  can not be empty, either set 'EMAIL_SERVER_PORT' in your envionment, "
                    "or 'use_google' to true"
                )
            self.email_server_port = settings.EMAIL_SERVER_PORT

        if self.template_folder:
            if not os.path.isdir(self.template_folder):
                raise exception.TemplateFolderNotFoundError(
                    f"Please provide a valid directory or create a template folder in {settings.TEMPLATE_DIR}"
                )

        if self.template_name:
            if not os.path.isfile(
                    os.path.join(self.template_folder, self.template_name)
            ):
                raise exception.TemplateFolderNotFoundError(
                    f"template with name '{self.template_name}', can not be found in {self.template_folder}"
                )

    def send_mail(self, email: Union[List[pydantic.EmailStr], pydantic.EmailStr]):
        self.__check_credential()
        message = multipart.MIMEMultipart()
        if isinstance(email, list):
            message["To"] = ', '.join(email)
        if isinstance(email, str):
            message["To"] = email
        from_email = self.admin_email
        subject: str = self.subject
        message['Subject'] = subject
        message['From'] = formataddr((self.website_name, from_email))

        if self.template_name and self.template_folder:
            body_content = self.render(self.template_name, self.context)
            message.attach(text.MIMEText(body_content, 'html'))
        elif self.body:
            body_content = self.body
            message.attach(text.MIMEText(body_content, 'plain'))
        else:
            raise exception.InvalidEmailContentError("Email body content is required")
        with smtplib.SMTP(self.email_server, self.email_server_port) as smtp:
            context = ssl.create_default_context()
            smtp.starttls(context=context)
            smtp.login(user=self.admin_email, password=self.admin_password)
            smtp.sendmail(from_email, email, message.as_string())
