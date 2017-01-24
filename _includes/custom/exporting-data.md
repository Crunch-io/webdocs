Export data by opening [Dataset Properties](crunch_dataset-properties.html) and then clicking **Export**.

![](images/ExportData.png)

### Selecting variables

The dataset's variable are listed on the left side. By default all variables are selected – you can choose to export only a subset of variables by deselecting any variables or groups that you don't want to export.

### Filtering variables

You can use the filter bar on the right side to export a filtered subset of rows. By default, any filters that were applied to the dataset will still be applied, and you can [add and remove filters](crunch_filtering-data.html) in the same manner as you would elsewhere.

###Export Options

Once you have determined what rows and columns to export, select a format (SPSS or CSV) from the **Format** selector.

If **CSV** is selected, you can set the following option:

**Category Labels** – By default, category names will be exported to the CSV file. Change to **IDs** to have the numeric ID of the category exported instead.

If **SPSS** is selected, you can set the following options:

**Variable Labels** – By default the variable description will be exported as the SPSS variable label. Select **Name** to export the variable name as the SPSS variable label instead.

**Array Labels** – By default array and multiple response subvariables will be exported with only their subvariable name. Select **Include array name** to have the array variable name prepended in the format **Array name | Subvariable name**.

### Exporting

Once finished setting options, click **Export** to export the dataset. You will see a loading indicator. Once the export is complete, **Download** and **Cancel** buttons will be available.

![](images/DownloadExport.png)

Click **Download** to download the exported dataset using your browser. Click **Cancel** to cancel the export, e.g. to select different variables and rows to export.
