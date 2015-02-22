# Mailbot

To create new instance:
```
curl --user "YOUR_API_KEY:YOUR_SECRET_KEY" https://api.mailjet.com/v3/REST/parseroute -H 'Content-Type: application/json' -d '{"Url":"http://your.webhook.com/email_processor"}'
```
