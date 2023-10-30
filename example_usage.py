import asyncio

from bs4 import BeautifulSoup
from temp_mail import AsyncTempMail

fetched_email_ids = []


def filter_emails(all_emails):
    filtered_emails = []
    for email in all_emails:
        if email.email_id not in fetched_email_ids:
            fetched_email_ids.append(email.email_id)
            filtered_emails.append(email)

    return filtered_emails


async def print_email(email):
    print(f"\nFrom: {email.sender}")
    print(f"Subject: {email.subject}")
    print(f"Attachments count: {email.attachments['count']}")
    print(f"\nBody: \n{email.text_body}")

    if email.attachments["count"] > 0:
        print("Attachments content:\n")
        for file in email.attachments["files"]:
            print(f"\nFilename: {file.filename}")
            print(f"File size: {file.size}")
            print(f"File mimetype: {file.mimetype}")
            print("File content: ")
            if file.mimetype == "text/plain":
                async for chunk in file.download():  # use this to download any attachment
                    print(chunk.decode())
                print()
                continue

            print("Mimetype not 'text/plain'... skipping")


async def main():
    async with AsyncTempMail() as temp_mail:
        response_json = await temp_mail.fetch_new_email_adress()

        email_adress = response_json["mailbox"]
        token = response_json[
            "token"  # use this token later to access emails associated with the email address
        ]

        print(f"Temp email adress: {email_adress}\nTemp email adress token: {token}\n")
        while True:
            input("Press Enter to check for new emails: ")
            filtered_emails = filter_emails(
                await temp_mail.fetch_all_emails(token)
            )  # filter emails to avoid displaying the same ones next time

            if len(filtered_emails) > 0:
                print(f"You have {len(filtered_emails)} new email(s)!")
                for email in filtered_emails:
                    detailed_email = (
                        await email.fetch_detailed_email()
                    )  # you need to use the 'fetch_detailed_email' function to retrieve the details of the email
                    await print_email(detailed_email)
                continue

            print("You do not have any new emails. :(\n")


if __name__ == "__main__":
    asyncio.run(main())
