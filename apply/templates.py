def funding_message(
    header,
    name,
    company,
    email,
    phone_number,
    about_company,
    funding_plan,
    exit_strategy
):
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"{header}",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*담당자:*\n{name}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*회사:*\n{company}"
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*이메일:*\n<mailto:{email}|{email}>"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*휴대폰 번호:*\n<tel:{phone_number}|{phone_number}>"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*회사에 대해 소개해주세요*\n{about_company}"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*투자금을 어떻게 사용할지 적어주세요*\n{funding_plan}"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*생각하고 계신 회수 전략에 대해 적어주세요*\n{exit_strategy}"
            }
        }
    ]

def partnership_message(
    header,
    name,
    company,
    email,
    phone_number,
    title,
    message,
):
    return [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"{header}",
                "emoji": True
            }
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*담당자:*\n{name}"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*회사:*\n{company}"
                }
            ]
        },
        {
            "type": "section",
            "fields": [
                {
                    "type": "mrkdwn",
                    "text": f"*이메일:*\n<mailto:{email}|{email}>"
                },
                {
                    "type": "mrkdwn",
                    "text": f"*휴대폰 번호:*\n<tel:{phone_number}|{phone_number}>"
                }
            ]
        },
        {
            "type": "divider"
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"{title}",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"{message}"
            }
        },
    ]