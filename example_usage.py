import asyncio

from bs4 import BeautifulSoup
from temp_mail import AsyncTempMail

fetched_emails = []


def print_new_email(all_emails):  # function will not work for now, made some changes
    for email in all_emails:
        if email[_id] not in fetch_email:
            print(f"From {email['from']}")
            print(f"Subject: {email['subject']}")
            print(f"\nBody: {email['bodyHtml']}")


async def main():
    async with AsyncTempMail() as temp_mail:
        response = await temp_mail.fetch_email(token, message_id)
        html = response["bodyHtml"]

        # print(temp_mail.html_to_text(html))
        response_json = await temp_mail.fetch_new_email()
        email, token = response_json["mailbox"], response_json["token"]

        print(f"Temp email: {email}\nTemp email token: {token}\n")

        while True:
            input("Press Enter to check for new emails: ")
            all_emails = await temp_mail.fetch_all_emails(token)


if __name__ == "__main__":
    asyncio.run(main())
