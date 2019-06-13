# finance-manager

A python script aimed at making managing finances in an organized manner simple. The script parses gmail inboxes
using the gmail API to find deposit alerts and then generates a pie chart showing your personalized budget breakdown 
which is saved to a desired location for future use.

## Usage

In your google account privacy settings, you will need to allow access for less secure apps in order for the
script to have access to your email account inbox.

You will also need to turn on deposit email notifications in your PNC account.

Update the following variables to match your account/preferences:

```python
# email info
EMAIL_ADR = 'YOUR EMAIL HERE'
EMAIL_PWD = 'YOUR PASSWORD HERE'

# default time period set to 2 weeks
days_to_check = 14

# categories can be changed/added/deleted as long as values add up to 1.0.
# for each category added/deleted, you must also add/delete a color
# for the pie chart
savings_categories = {'College Funds': .75, 'Savings': .2, 'Spending': .05}

# saving pie chart to entered filepath as pdf
plt.savefig("ENTER DESIRED FILE LOCATION" + datetime.date.today().strftime("%b%d") + ".pdf", bbox_inches="tight"
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Example changes:
* Add functionality for other email providers
* Add functionality for other banks/finance apps (Paypal, CashApp, etc)
* Update README.md
* Code clean up/review

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
