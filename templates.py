templates = [
'''\
Subject: Python 101 - Spam Warning

Dear {} {},

you are receiving this message because you have
purchased a ticket to the Python 101 KCL Robotics
event on Eventbrite. You will receive a couple more
"spam" messages, just like this one, as we are trying
to demonstrate some simple ways of using Python (like
sending out emails to mailing lists).

If you ended up not taking part at the workshop, just
ignore/delete the emails you receive from this address.
Also feel free to block this address as it is just a throwaway.

Best regards,
KCL Robotics Society
''',
'''\
Subject: Totally not spam.

Hi there {} {}!
This message is totally not a spam message.
Just saying.
You might want to check out this links though:
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://www.youtube.com/watch?v=I_izvAbhExY
https://www.youtube.com/watch?v=I_2D8Eo15wE
https://www.youtube.com/watch?v=oavMtUWDBTM

Best regards,
your friendly Python Spambot
''',
'''\
Subject: Even moar spam!!!

Hello and welcome {} {}!
Do you want to become better at <insert generic skill here> in just two hours?
Then check out this website and I'm sure you'll find what you are looking for!

https://www.kclrobotics.com/

Best regards,
your friendly Python Spambot
''',
'''\
Subject: {} {}, we have some more spam for you

Glad to see you are still reading this random spam I am writing right now.
It's honestly quite boring and pointless but I'm trying to make it seem like I still
care about what I'm writing. I actually don't. It literally just white noise.

Anyways, check this out, blah, blah:

https://www.eventbrite.co.uk/e/halloween-robotics-weekender-tickets-74979386363?aff=FacebookLink&fbclid=IwAR0QJz7JMp0F1CMGlWX9oFLYlGm3C63id76APN336LZOnzgErAZKmkjo-BE

Best regards,
your friendly Python Spambot
'''
]

def get_templates():
    return templates
