---
title: "Appending Data"
audience: all
---

You can append a dataset to the current dataset to add more rows of data. When one dataset is appended to another, variables are
matched on their aliases. Variables that do not match between datasets are padded with missing values. Variables that are matched between the datasets must be the same type, but aside from that, the append process will attempt to adapt the variables to align. For variables with categories, categories are matched between the variables by name; for subvariables, they are matched by alias. Any categories or subvariables that do not match across the datasets will be kept: the resulting variable will have the superset of categories/subvariables.

It is recommended you verify that the datasets you are appending align as you expect prior to appending. If the system reaches the conclusion that it cannot append the data, the dataset will remain unchanged, except for an “automatic rollback savepoint” in [Dataset History](crunch_dataset-history.html). When the datasets are appended successfully, an additional “Appended” version will be automatically saved.

To append data, click the dataset name in the upper-left and then select the **Append** tab. You will see a list of datasets in the current project.

![](images/AppendData.png)

Select a dataset and click **Next** to append it. Appending may take a few minutes depending on the size of your datasets. Once you are finished, you will either see a success message or you will be informed that the append failed. If you are having trouble appending data, please contact us at [support@crunch.io](mailto:support@crunch.io).
