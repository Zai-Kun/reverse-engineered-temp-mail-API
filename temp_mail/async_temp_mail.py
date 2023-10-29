import asyncio

from bs4 import BeautifulSoup
from curl_cffi.requests import AsyncSession

BASE_API_URL = "https://web2.temp-mail.org"


class Email:
    def __init__(self, email_data):
        self.email_id = email_data["_id"]
        self.sender = email_data["from"]
        self.subject = email_data["subject"]
        self.html_body = email_data["bodyHtml"]
        self.text_body = self.html_to_text(self.html_body)
        self.preview = email_data["bodyPreview"]
        self.attachments = {
            "count": email_data["attachmentsCount"],
            "files": email_data["attachments"],
        }

    @staticmethod
    def html_to_text(html_body):
        plain_text = html_body.replace("<br>", "\n")
        soup = BeautifulSoup(plain_text, "html.parser")
        return soup.get_text()


class AsyncTempMail:
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

    def __init__(self, user_agent=None):
        self.user_agent = self.USER_AGENT if not user_agent else user_agent

    async def __aenter__(self):
        self.session = AsyncSession(impersonate="chrome110", timeout=99999)
        return self

    async def __aexit__(self, *args):
        self.session.close()

    async def fetch_new_email_adress(self):
        url = f"{BASE_API_URL}/mailbox"
        headers = {"User-Agent": self.user_agent}

        response = await self.session.post(url, headers=headers)
        response_json = response.json()

        return response_json

    async def fetch_all_emails(self, token):
        url = f"{BASE_API_URL}/messages"
        headers = {"User-Agent": self.user_agent, "Authorization": token}

        response = await self.session.get(url, headers=headers)
        response_json = response.json()

        return response_json["messages"]

    async def fetch_email(self, token, message_id):
        url = f"{BASE_API_URL}/messages/{message_id}"
        headers = {"User-Agent": self.user_agent, "Authorization": token}

        response = await self.session.get(url, headers=headers)
        response_json = response.json()

        return Email(response_json)

    async def fetch_attachment(self, token, message_id, attachment_id):
        url = f"{BASE_API_URL}/messages/{message_id}/attachment/{attachment_id}"
        headers = {"User-Agent": self.user_agent, "Authorization": token}
        response_queue = asyncio.Queue()

        async def perform_request():
            def content_callback(chunk):
                response_queue.put_nowait(chunk)

            response = await self.session.get(
                url=url, headers=headers, content_callback=content_callback
            )
            await response_queue.put(None)

        stream_task = asyncio.create_task(perform_request())

        while True:
            chunk = await response_queue.get()
            if chunk is None:
                break
            yield chunk
