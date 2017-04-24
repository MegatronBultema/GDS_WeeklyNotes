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
