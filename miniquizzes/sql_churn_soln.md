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

SELECT a.id, a.name, a.city, a.state, a.business_type, CASE WHEN c.duration >= 14 THEN 'True' ELSE 'False' END as churn
FROM advertisers as a
JOIN campaigns as c
ON a.id = c.advertiser_id

2. Say we have another table that has predicted results of churn.

    ```
    predicted_churn
        advertiser_id
        churn
    ```

    Write a query to calculate each of the following metrics:

    * accuracy: (TP + TN)/(P + N)
    * precision: TP/(TP + FP)
    * recall (aka sensitivity): TP/(TP + FN)
    * specificity: TN/(TN + FP)

  Table:
          Predicted:
  Truth:          True        False
    True    |     TP            FN

    False   |     FP            TN

    The [confusion matrix wikipedia page](http://en.wikipedia.org/wiki/Confusion_matrix) has all of the metrics defined nicely in case you are getting them mixed up.

    WITH confusion_matrix AS
    (SELECT
    CASE WHEN c.churn = 'True' and p_c.chrun ='True' THEN 'TP'
    ELSE WHEN c.churn = 'True' and p_c.chrun ='False' THEN 'FP'
    ELSE WHEN c.churn = 'False' and p_c.chrun ='True' THEN 'FN'
    ELSE WHEN c.churn = 'False' and p_c.chrun ='False' THEN 'TN'
    AS c_mat END
    FROM churn AS c
    JOIN predicted_churn as p_c
    ON c.advertiser_id = p_c.advertiser_id)

    SELECT
    (COUNT(cm.c_mat = 'TP') + COUNT(cm.c_mat = 'TN'))/(COUNT(c.churn = 'True') + COUNT(c.churn = 'False')) as accuracy,
    (COUNT(cm.c_mat = 'TP')/COUNT(cm.c_mat = 'TP') + COUNT(cm.c_mat = 'FP')) as precision,
    (COUNT(cm.c_mat = 'TP')/(COUNT(cm.c_mat = 'TP')+COUNT(cm.c_mat = 'FN'))) as recall,
    (COUNT(cm.c_mat = 'TN')/(COUNT(cm.c_mat = 'TN') + COUNT(cm.c_mat = 'FP'))) as specificity
    FROM confusion_matrix as cm
    JOIN churn as c
    ON cm.advertiser_id = c.advertiser_id;
