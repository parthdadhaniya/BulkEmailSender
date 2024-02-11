# this function will returns email list


def email_lists(email_list):
    emails = email_list.split(",")
    to_emails = [email.strip() for email in emails]
    return to_emails
