---
title: "Variable Properties"
audience: all
---

<p>When editing a dataset, you can access properties of individual variables by clicking <strong>Edit</strong> underneath the variable card. </p>
<p style="padding-left: 30px;"><img src="images/edit-variable-properties-resized.png" alt="" /></p>
<p>You can edit the name and description of all variables, as well as hide or delete them. (these can also be done in the variable organizer).</p>
<figure><img src="images/variable-properties-page.png" alt="" /><figcaption>Example properties panel</figcaption></figure>
<p><span style="color: #333333; font-family: Tahoma, Helvetica, Arial, sans-serif; font-size: 12.16px; line-height: 1.3em;">Additional properties depend on the variable type:</span></p>
<h3>Categorical Variable Properties</h3>
<p><strong>Numeric Values</strong> - Show or hide the numeric value associated with each category. These values can be used to treat the variable as numeric (and compute its mean) in an analysis.</p>
<p><strong>Counts/Percentages</strong> - Show counts or percentages on the variable card.</p>
<p><strong>Decimal Places</strong> - If showing percentages, how many decimal places to display on the variable card.</p>
<p><strong>Include/Exclude Missing</strong> - If set to <strong>Include</strong>, missing categories will be shown on the variable card and missing rows will be used when calculating percentages.</p>
<h3>Numeric Variable Properties</h3>
<p><strong>Use as Weight</strong> - Set to yes to use this numeric variable as a weight for the dataset. Weight variables can also be created using existing categorical variables using the Weight Builder.</p>
<p><strong>Add Missing Value/Range</strong> - Designate a value or range of values on this numeric value that should be marked as missing.</p>
<h3>Text Variable Properties</h3>
<p><strong>Counts/Percentages</strong> - Show counts or percentages on the variable card.</p>
<p><strong>Decimal Places</strong> - If showing percentages, how many decimal places to display on the variable card.</p>
<p><strong>Add missing</strong> - Designate a text string to be treated as missing.</p>
<h3>Multiple Response Variable Properties</h3>
<p><strong>Counts/Percentages</strong> - Show counts or percentages on the variable card.</p>
<p><strong>Decimal Places</strong> - If showing percentages, how many decimal places to display on the variable card.</p>
<p><strong>“None of the Above”</strong> - If set to <strong>Yes</strong>, the variable will include a None of the Above category used for rows in which none of the constituent variables is true.  </p>
<p><strong>Include/Exclude Missing</strong> - If set to <strong>Include</strong>, missing categories will be shown on the variable card and missing rows will be used when calculating percentages.</p>
<p><strong>Split</strong> – Turn each row of the variable into a separate categorical variable.</p>
<h3>Array Variable Properties</h3>
<p><strong>Counts/Percentages</strong> - Show counts or percentages on the variable card.</p>
<p><strong>Decimal Places</strong> - If showing percentages, how many decimal places to display on the variable card.</p>
<p><strong>Include/Exclude Missing</strong> - If set to Include, missing categories will be shown on the variable card and missing rows will be used when calculating percentages.</p>
<p><strong>Rearrange</strong> – Change the names, values, missingness, and order of items and categories.</p>
<p><strong>Split</strong> – Turn each “row” item of the array into a separate categorical variable</p>
<p> </p>
<p>When finished, you can save your changes, and if you cancel, you’ll be asked to confirm that you want to discard changes.</p>
<figure><img src="images/variable-properties-save.png" alt="Discard changes confirmation" /><figcaption>Discard changes confirmation</figcaption></figure>
