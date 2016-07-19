To combine variable categories, you can either:

* Open [Variable Properties](crunch_variable-properties.html) for the categorical variable you wish to combine, and then select **Combine Categories** to create a new variable derived from combining categories from this one, or

* open Variable Properties for a variable that was previously created by combining categories, and then select **Edit Categories** to modify how this variable is derived (this is usually a better option than creating a new derived variable), or

* click [Create New Variable](crunch_creating-variables-2.html) at the bottom of the sidebar, select **Combine Categories**, and then select the variable to be combined from the sidebar.

Any of these methods open the Combine Categories interface:

![](images/CombineVariableInterface.png)

The left side of the interface shows the source variable and the right side shows the variable that will be created.

Click the variable name or category names on the right side of the right side of th interface to rename them. To combine categories, drag them together. Combined categories will show the categories that were used the create them on the left and the new category on the right.

![](images/VariableCombined.png)

Right-click a combined category and select **Split Category** to split it back into its component categories.

Hover over a category to show the valid/missing toggle on the right side. Use this to determine whether the category will be valid or missing in the new variable.

Once you have finished combining categories, click **Save** to create the new variable.