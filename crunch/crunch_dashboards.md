---
title: Configuring a Dataset Dashboard
audience: all
---

The first thing a user sees when they open a dataset is its **dashboard**. By default, the dashboard will show a summary of the dataset based on its [dataset properties](crunch_dataset-properties.html).

![](images/DatasetSummary.png)

To customize this dashboard page, click the dataset name and select **Configure Dashboard** from the dropdown to open the dashboard configuration panel.

![](images/ConfigureDashboard.png)

In this panel you can select from one of the following options:

### Dataset Summary
This is the default view – a summary of the dataset metadata configured in [dataset properties](crunch_dataset-properties.html), as seen above.

### URL
Select **URL** to specify a custom URL that will be used as the dataset dashboard. Typically this is used to show a [Shiny Dashboard](https://rstudio.github.io/shinydashboard/) built from your dataset using Rstudio's Shiny tool, but it could also be a CrunchBox or any web-based content you host in another location.

### Deck
Select **Deck** to choose a deck to use as a dashboard. The first four analyses saved to that deck will be displayed in a two-by-two grid.

![](images/dashboard.png)
The selected deck will become shared (available to all users on the dataset) when it is used as a dashboard. See [Saving, Exporting, and Sharing Analyses](crunch_saving-analyses.html) for more information about creating decks.
