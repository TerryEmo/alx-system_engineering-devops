0x19. Postmortem

Issue Summary: Duration: February 15, 2024, 16:00 AM — February 15, 2024, 16:30 AM (UTC-5) Impact: The user-facing website experienced intermittent downtime, resulting in a degraded user experience. Approximately 20% of users were affected, encountering slow page loading and occasional error

Timeline
17:10 AM : push updates
17:15 AM : Ckecking problem
17:15 AM : Processing the both front end and backend teams
17:20 AM : Successful change
17:24 AM : Server Restarts begin
17:27 AM : 100% of traffic back online
17:30 AM : start debugging the push with the problem
17:50 AM : Probelm fixed and pushed the changes
17:55 AM : Server restart begins
18:00 AM : 100% traffic back online with the new updates
Root cause and resolution
After rolling back changes we knew that the changes were made by the front end team so we took the broken changes and run them on a test server which replicated same problem, our server uses apache2 and apache2 error logs didn't give enought infomation about the problem so we traced the apache2 process using strace and when a request is sent strace tool catchs a lot of error and after some scaning fo these errors we found the error wich is a typo in page file extention >

.phpp

instead of

.php

and to fix that we just search in our main directory using grep for that typo

grep -inR ".phpp" .

after fixing the error we pushed back the changes and restarted the servers

10:00 AM : 100% of trafic back online with the new updates
Corrective and preventative measures
To prevent similar problems from happening again we will

Create an automated test pipeline for every update push
Add a monitoring software to our servers which will monitor lot of things and one of them Network Traffic resquests and responses and configure it to make an lert to the teams when too much non desired responses were sent like 404
Create a tests for every new update and the teams shouuld not push until those tests pass
