# Exploratory Data Analysis Report:

Prepare a report summarizing the findings from your exploratory data analysis. Include visualizations and insights that help understand the dataset.


### Fees:

The table for fees contains 21061 rows and 13 columns.

RangeIndex: 21061 entries, 0 to 21060
Data columns (total 13 columns):
    Column           Non-Null Count  Dtype  
    ---  ------           --------------  -----  
    0   id               21061 non-null  int64  
    1   cash_request_id  21057 non-null  float64
    2   type             21061 non-null  object 
    3   status           21061 non-null  object 
    4   category         2196 non-null   object 
    5   total_amount     21061 non-null  float64
    6   reason           21061 non-null  object 
    7   created_at       21061 non-null  object 
    8   updated_at       21061 non-null  object 
    9   paid_at          15531 non-null  object 
    10  from_date        7766 non-null   object 
    11  to_date          7766 non-null   object 
    12  charge_moment    21061 non-null  object 
    dtypes: float64(2), int64(1), object(10)

Every single charged fee has its own ID and is linked to a cash request ID, which marks the common denominator 
between the fee and the cash Request table.

It types each fee into either 'instant_payment', 'incident' or 'postpone'.

The status of the fees can be 'accepted', 'cancelled' or 'rejected'.

The column 'category' contains only values for all the incidents (categorizes which incident occurred:
either the direct debit was rejected or the payment was delayed for one month).

The fee amount is either 5.00 or 10.00 and in sum creates the revenue.

The column 'reason' is dependent of the column type, in case of 'instant payment'-type it only states instant payment
request + the cash request id, in case of an incident it returns the same as 'category', which shows the reason for the 
incident. For postponed cash request it shows 'Postpone cash request + {cash request id}'.

Non-postponed fee charges are linked to 3 different dates in 3 columns, the date they were created, updated and paid. 
Some fees were not paid so far, which leads to null values.
Postponed fee charges open as well a column for the date from which the fee payment was delayed and the date it was 
delayed to.

Charge moment can be either before of after (creation date).



### Cash request:

The table for cash requests contains 23970 rows and 16 columns.

RangeIndex: 23970 entries, 0 to 23969
Data columns (total 16 columns):
     Column                      Non-Null Count  Dtype  
    ---  ------                      --------------  -----  
    0   id                          23970 non-null  int64  
    1   amount                      23970 non-null  float64
    2   status                      23970 non-null  object 
    3   created_at                  23970 non-null  object 
    4   updated_at                  23970 non-null  object 
    5   user_id                     21867 non-null  float64
    6   moderated_at                16035 non-null  object 
    7   deleted_account_id          2104 non-null   float64
    8   reimbursement_date          23970 non-null  object 
    9   cash_request_received_date  16289 non-null  object 
    10  money_back_date             16543 non-null  object 
    11  transfer_type               23970 non-null  object 
    12  send_at                     16641 non-null  object 
    13  recovery_status             3330 non-null   object 
    14  reco_creation               3330 non-null   object 
    15  reco_last_update            3330 non-null   object 
    dtypes: float64(3), int64(1), object(12)
    memory usage: 2.9+ MB

Every cash request has a unique ID that also occurs in the fees table.

Amounts for the cash requests can vary and assumingly be chosen by the likes of the requesting user.

There are 12 different statuses that mark the status of processing from being approved by Ironhack to getting the 
whole money back.

The column with the date the cash request was created at defines the cohort month by which the cash requests are grouped
by. Our analysis repeatedly compares the (13) cohorts among each other. The 13 cohorts are defined by months 
2019-11 until 2020-11.

Other dates for the cash request appear when they are updated, moderated and reimbursed. Some cash request were received
on a later date than they were created, which also creates a new date for cash request reception. Recovered cash requests
show also different dates for recovery creation and updates, as well as the status of cash request recovery (can be
either 'completed' or 'pending').

Transfer types are either 'regular' or 'instant'.

### Patterns and Outliers:

We discovered a huge peak in cash requests in October 2020 which can be explained by some sort of promotion which led 
to such a high number of cash requests. The overall revenue is coinciding with this increase of cash requests and on its
peak one month later. Since we calculated the average time of the cash being paid back and it was all around 30 days this 
gives an explanation to the peak of revenues occurring one month after the peak of cash requests.

Incident rates were on their peak in the middle of 2020.

The average time of the cash being paid back is evenly distributed over time and has slight ups and downs.

We also calculated the probability of people using the payment services again, as in here it's the probability for people 
to return. Since the first user claimed the service again for 8 times the probability of returns is 800% here. You could
instead as well calculate the probability of one user returning, which would remove this outlier but in the end showed less of an information. Overall the probability of users claiming the payment service is evenly distributed.




# Data Quality Analysis Report:

Data Quality Analysis Report: Document the results of your data quality analysis, highlighting any issues and the steps taken to resolve them.

### Null-values: 

...in fees:
- all category values are null if there was no incident.
- all from_dates and to_dates are null if the payment wasn't postponed.
- if money wasn't paid back so far there is a null value.
- there are null values for the columns for postponed fee charges if charging the fee was not postponed.

...in cash requests:
- There were some cash request IDs missing (4) which we replaced as they can be found in the reasoning column.
- all null value user IDs seem to instead have a deleted account id but (21867 + 2104 = 23971 (sum))
    -> (!) There is one account with both deleted account and user ID, reason is unclear, so we left both of the IDs 
    for further investigation.
- null values appear if the cash request wasn't received later than it was created.
- all values are null in the columns concerning the cash request recovery if there was no recovery of the cash request

