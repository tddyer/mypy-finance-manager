# finance-manager

A Python script aimed at making the process of managing finances simple. The script parses gmail inboxes
using Python's gmail API to find deposit alerts and then generates a pie chart showing your personalized budget breakdown
which is saved to a desired file location for future reference.

## Setup
![less_secure_apps](https://user-images.githubusercontent.com/39466067/64708301-049ce300-d47a-11e9-9d99-4f9ec244e142.png)

## Usage

In your google account privacy settings, you will need to allow access for less secure apps in order for the
script to have access to your email account inbox.

You will also need to turn on deposit email notifications in your PNC account.

Update the following variables to match your account/preferences:

```python
# email info
EMAIL_ADR = 'YOUR EMAIL HERE'
EMAIL_PWD = 'YOUR PASSWORD HERE'

# categories can be changed/added/deleted as long as values add up to 1.0.
# for each category added/deleted, you must also add/delete a color
# for the pie chart
savings_categories = {'College Funds': .75, 'Savings': .2, 'Spending': .05}

# saving pie chart to entered filepath as pdf
plt.savefig("ENTER DESIRED FILE LOCATION" + datetime.date.today().strftime("%b%d") + ".pdf", bbox_inches="tight"
```

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
