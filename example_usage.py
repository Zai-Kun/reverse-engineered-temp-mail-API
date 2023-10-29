import asyncio

from bs4 import BeautifulSoup
from temp_mail import AsyncTempMail

fetched_email_ids = []


def filter_emails(all_emails):
    filtered_emails = []
    for email in all_emails:
        if email["_id"] not in fetched_email_ids:
            fetched_email_ids.append(email["_id"])
            filtered_emails.append(email)

    return filtered_emails


def print_email(email):
    print(f"\nFrom: {email.sender}")
    print(f"Subject: {email.subject}")
    print(f"Attachments: {email.attachments['count']}")
    print(f"\nBody: \n{email.text_body}")

    print(email.attachments)


async def main():
    async with AsyncTempMail() as temp_mail:
        response_json = await temp_mail.fetch_new_email_adress()
        email_adress, token = response_json["mailbox"], response_json["token"]

        print(f"Temp email adress: {email_adress}\nTemp email adress token: {token}\n")

        # async for chunch in email.attachments["files"][0].download():
        #     print(chunch.decode())

        # while True:
        #     input("Press Enter to check for new emails: ")
        #     filtered_emails = filter_emails(await temp_mail.fetch_all_emails(token))

        #     if len(filtered_emails) > 0:
        #         print(f"You have {len(filtered_emails)} new email(s)!")
        #         for email in filtered_emails:
        #             complete_email = await temp_mail.fetch_email(
        #                 token, email["_id"]
        #             )  # you need to use the 'fetch_email' function to retrieve all details of the email
        #             print_email(complete_email)
        #     else:
        #         print("You do not have any new emails. :(\n")


if __name__ == "__main__":
    asyncio.run(main())
