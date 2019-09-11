# finance-manager

A Python script aimed at making the process of managing finances simple. The script parses gmail inboxes
using Python's gmail API to find deposit alerts and then generates a pie chart showing your personalized budget breakdown
which is saved to a desired file location for future reference.

## Setup
  - You will need to allow access to your google account for less secure apps so the parser can have access to your gmail inbox
    - Navigate to Google account settings (not gmail settings) -> Security -> less secure apps access (shown below)
![less_secure_apps](https://user-images.githubusercontent.com/39466067/64708301-049ce300-d47a-11e9-9d99-4f9ec244e142.png)

  - Within your PNC bank account, turn on deposit email notifications
    - Navigate to Alerts -> Alerts Profile -> turn on "Direct deposit greater than $1.00" email notifications

  - Update the following variables to match your account/preferences:

  ```python
  # email info
  EMAIL_ADR = 'YOUR EMAIL HERE'
  EMAIL_PWD = 'YOUR PASSWORD HERE'

  # categories can be changed/added/deleted as long as values add up to 1.0.
  # for each category added/deleted, you must also add/delete a color located
  # under graph info
  savings_categories = {'College Funds': .75, 'Savings': .2, 'Spending': .05}
  
  # graph info
  colors = ['#ff9999', '#66b3ff', '#99ff99']
  
  # saving pie chart to entered filepath as pdf named as the current date (Ex: Jul05.pdf)
  # example file location: 'home/your/directory/'
  plt.savefig("ENTER DESIRED FILE LOCATION" + datetime.date.today().strftime("%b%d") + ".pdf", bbox_inches="tight"
  ```

## License
[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
