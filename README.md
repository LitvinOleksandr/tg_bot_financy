# Budget Management Bot

This is a Telegram bot that helps you manage your household budget.

### How it works:
- You can log your purchases by sending the command:
  <pre>add &lt;store name&gt; &lt;amount&gt;</pre>
  For example, if you made a purchase at a store named "SuperMarket" for 50 (UAH, EURO, Dollars), you would send:
  <pre>add SuperMarket 50</pre>

- The bot will then save the information into a database.

- You can check your spending for any given month by sending the command:
  <pre>shop info &lt;month number&gt;</pre>
  For example, to view the spending report for January, you would send:
  <pre>shop info 1</pre>

- The bot will provide a list of stores you have spent money at and the total amount spent in that month.

- At the end of the report, you will see a summary showing the total amount spent during the specified period.

### Project Overview

This project is designed for learning Python, as well as being a project that interests me. 

To run the application, you need to create a database file on your computer and two additional files: one with the Telegram bot token and another with the ID numbers of users who can add and request information. You can find your ID by sending any message to the bot and using the command:
  <pre>print(message.chat.id)</pre>
This will display your ID number. 

In the future, I plan to add a script that will automatically set up these files for a quicker setup.
