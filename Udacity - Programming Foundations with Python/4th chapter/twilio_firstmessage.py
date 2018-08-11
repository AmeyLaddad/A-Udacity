from twilio.rest import TwilioRestClient


accounnt_sid = "AC21a8ff39c0ee655cafa8ab6cfab255d0"

auth_token = "9252bae242f90f225a1fe28056b4637e"

client = TwilioRestClient(accounnt_sid,auth_token)

message = client.sms.messages.create(
    body = "Hello Amey",
    to = "+919881945550",
    from_ = "+14159914690")

print message.sid
    

