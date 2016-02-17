---
title: "Creating a Categorical Variable"
audience: all
---

<p>When you open the categorical variable creator from the <a href="2-help/14-creating-variables-2.html">New variables</a> page the following interface opens:</p>
<p><img src="images/CreateCategorical.png" alt="" /></p>
<p>This interface allows you to define categories for the new categorical variable one at a time. Select a variable from the sidebar by clicking or dragging it to get started. The selected variable will be added to the open category.</p>
<p><img src="images/DefiningACategory.png" alt="" /></p>
<p>Defining a category works identically to the <a href="2-help/5-filtering-data.html">Filter Builder</a> - you can define what rows of the data will be included in the category based on other variables in the dataset. </p>
<p>Once you have finished defining a category, click <strong>Add Category</strong> to close that category and start a new one. You must name a category before starting a new one. As you add categories, they will be shown at the top of the interface.</p>
<p><img src="images/DefinedCategories.png" alt="" /></p>
<p>Click on a category to expand it and edit it.</p>
<p>You can change the order of categories by clicking and dragging them to a new spot in the list. The categories will be evaluated in order, so if a row evaluates as true for more than one category, it will be included in the top-most one.</p>
<p>The valid/missing toggle on the right side of each category determines whether the category will be counted as valid or missing in the new variable.</p>
<p>At the bottom of the interface is the Other category:</p>
<p><img src="images/OtherCategory.png" alt="" /></p>
<p>This category contains all rows that meet none of the defined conditions. By default is is named Other and marked missing, but you can edit the name and toggle whether it is valid or missing. It cannot be moved from the bottom position in the variable.</p>
<p>Once you have finished defining categories, click Save to create the variable. The variable must have a name in order to be saved.</p>
