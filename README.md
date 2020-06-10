# attendance_bot
A script that scrapes live chat from youtube and messages you when a link is posted.

With the entire country of India (and most of the world) being under lockdown due to Covid-19, universities have had to resort to online classes to complete the syllabus. After trying (and miserably failing) to use platforms like Zoom and Skype, my particular uni decided to settle on YT Live as the perfect platform for conducting these classes, and attendance is to be marked by filling in a Google form within 3 minutes of it being posted in the live chat. 

Under these trying circumstances, the semester exams are at risk of being cancelled, and as a result, attendance is more important than ever. 

We engineers live for attendance, but who has the time to attend five hours of classes a day when we've got much more important things to do? (Read: gaming)

This script, given a YouTube Live link, gets the source of the iframe in which the YT Live chat is hidden, then scrapes it and looks for a link. When a link is found, it uses notify.run and Twilio for Python to both send push notifications through a browser as well as a Whatsapp message.

Automating the process of filling in the form would be a piece of cake as well using Requests/Selenium, but I've chosen not to do that, since 
a) The format of the forms we get changes everyday for some reason, and
b) The forms we get are designed such that you need to be logged into your Google account in order to fill them.

Dependencies:

  Requests
  
  Twilio
