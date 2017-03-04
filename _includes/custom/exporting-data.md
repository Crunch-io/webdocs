Export data by opening [Dataset Properties](crunch_dataset-properties.html) and then clicking **Export**.

![](images/ExportData.png)

### Selecting variables

The dataset's variables are listed on the left side. By default, all non-hidden variables are selected – you can choose to export only a subset of variables by deselecting any variables or groups that you don't want to export.

### Filtering variables

You can use the filter bar on the right side to export a filtered subset of rows. By default, any filters that were applied to the dataset will still be applied, and you can [add and remove filters](crunch_filtering-data.html) in the same manner as you would elsewhere.

### Export options

**Output Format** – Once you have determined what rows and columns to export, select a format (SPSS or CSV) from the **Format** selector. The other export options change depending on output format.

#### CSV export options

**Cell Labels** – How the category names will be exported for categorical variables. Select **Category names** to export category names; select **IDs** to export the categories' numeric IDs.

**Missing Values** – What will be exported for missing values. Select **Missing Reason** to use the missing reason text; select **Blanks** to use an empty cell for missing values; select **"." (Dot)** to use ".".

#### SPSS export options

**Variable Labels** – What will be exported as the SPSS variable label. Set to **Description** to export the variable description; select **Name** to export the variable name.

**Array Labels** – How array and multiple response subvariable names will be exported. Select **Independent** to export only the subvariable names; select **Include array name** to have the array variable name prepended in the format **Array name /&#124; Subvariable name**.

### Exporting

After setting options, click **Export** to export the dataset.

![](images/DownloadExport.png)

Once the export is complete, click **Download** to download the exported dataset using your browser. Click **Cancel** to cancel the export, e.g. to select different variables and rows to export.
