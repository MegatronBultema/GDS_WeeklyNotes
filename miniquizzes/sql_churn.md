## Miniquiz: SQL Practice

**Include your code and answers in** this file or in `sql_churn_soln.md`.

### Tables

You have a SQL database of advertisers on your site and advertising campaigns.

```
advertisers
    id
    name
    city
    state
    business_type
```

```
campaigns
    advertiser_id
    campaign_id
    start_date
    duration
    daily_budget
```

### Questions
You would like to determine which advertisers are *churning*, which means leaving the site. First, we define churn as if a user hasn't had an ad running for 14 days.

1. Write a query to create the following table so that we can export it and build a model for predicting churn.

    ```
    churn
        advertiser_id
        name
        city
        state
        business_type
        churn
    ```

    The first 5 columns are from the advertisers table. The churn column has a boolean value of whether or not they have churned. Keep in mind that you'll need to use the duration to determine if the ad is still running.


2. Say we have another table that has predicted results of churn.

    ```
    predicted_churn
        advertiser_id
        churn
    ```

    Write a query to calculate each of the following metrics:

    * accuracy
    * precision
    * recall (aka sensitivity)
    * specificity

    The [confusion matrix wikipedia page](http://en.wikipedia.org/wiki/Confusion_matrix) has all of the metrics defined nicely in case you are getting them mixed up.

