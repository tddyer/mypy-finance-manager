# Note: this script is specific to PNC alert emails
# and gmail, other combinations of banks and email
# will most likely need modification

import smtplib
import datetime
import imaplib
import email
import matplotlib.pyplot as plt


# EMAIL PARSING

# email info
EMAIL_ADR = 'YOUR EMAIL HERE'
EMAIL_PWD = 'YOUR PASSWORD HERE'
INCOMING_SERVER = 'imap.gmail.com'


# email login
mail = imaplib.IMAP4_SSL(INCOMING_SERVER)
mail.login(EMAIL_ADR, EMAIL_PWD)
mail.select('inbox')

# default time period set to 2 weeks
days_to_check = 14
stop_date = (datetime.date.today() - datetime.timedelta(days_to_check)).strftime("%d-%b-%Y")

# selecting only emails from the Primary inbox from current date through the stop date
type, data = mail.search(None, 'SINCE ' + stop_date + ' X-GM-RAW "Category:Primary"')
email_ids = data[0]
ids = email_ids.split()

# getting range of all emails in the inbox
first_email = int(ids[0])
latest_email = int(ids[-1])

deposits = []

# parsing emails
for i in range(latest_email, first_email, -1):
    # For each email:
    #  check simply returns OK if email can be retrieved.
    #  data is the actual email data in the email format RFC822
    check, data = mail.fetch(str(i).encode(), '(RFC822)')

    if check != 'OK':
        print('Failed to retrieve messsage')
    else:
        for resp in data:
            if isinstance(resp, tuple):
                # to get email as string, we decode from RFC822 to UTF-8
                msg = email.message_from_string(resp[1].decode("utf-8"))
                # selecting only emails that specify a depost was made by looking at email subject
                if "Direct Deposit Greater Than $1.00 Credited To Your Checking Account" in msg['Subject']:
                    # getting date of deposit
                    email_date = msg['Date']
                    email_date = email_date[:email_date.find(':')-3]

                    # obtaining amount of deposit and converting to a float value
                    msg_as_string = msg.get_payload()[0].as_string()

                    start = msg_as_string.find('Amount')
                    amount_str = msg_as_string[start:start+17]
                    amount_str = amount_str.rstrip().strip('Amount: $')
                    amount = float(amount_str)
                    deposits.append(amount)

                    print('${} was deposited to your bank account on {}!'.format(amount_str, email_date))


# PIE CHART GENERATION

# categories can be changed/added/deleted as long as values add up to 1.0.
# for each category added/deleted, you must also add/delete a color
# for the pie chart
savings_categories = {'College Funds': .75, 'Savings': .2, 'Spending': .05}

total_income = 0
for deposit in deposits:
    total_income += deposit

budget_breakdown = {}
legend_values = []
for category, portion in savings_categories.items():
    budget_breakdown[category] = total_income*portion
    legend_values.append('${:.2f}'.format(total_income*portion))

# graph info
colors = ['#ff9999', '#66b3ff', '#99ff99']
explode = []
for x in range(len(budget_breakdown.keys())):
    explode.append(0.05)

# creating pie chart
plt.pie(budget_breakdown.values(), labels=budget_breakdown.keys(), colors=colors, startangle=90, pctdistance=0.85, autopct='%1.0f%%', explode=explode)
stop_date_graph = (datetime.date.today() - datetime.timedelta(days_to_check)).strftime("%b %d")
plt.title('Budget Breakdown: {}-{}'.format(stop_date_graph, datetime.date.today().strftime("%b %d")))
plt.legend(legend_values, loc=4)

# draw inner circle
center_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

# equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')
plt.tight_layout()

# saving pie chart to entered filepath as pdf
plt.savefig("ENTER DESIRED FILE LOCATION" + datetime.date.today().strftime("%b%d") + ".pdf", bbox_inches="tight")
plt.show()
