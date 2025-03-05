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
