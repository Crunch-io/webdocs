The variable organizer allows dataset editors to sort variables into groups and determine the order in which they will appear in the sidebar. It can also be used to quickly edit variable names, descriptions, and aliases.

If the dataset you wish to organize is already shared with other users, you should consider [creating a draft](crunch_draft-and-publish.html) before organizing it (or making other significant changes). This will allow you to verify that the dataset organization appears as you expect before pushing the reorganized dataset to your clients.

Open the variable organizer by [opening dataset properties](crunch_dataset-properties.html) and then selecting the **Edit Variables** tab.

![](images/OrganizeVariables.png)

Variables are listed in their current order, along with their descriptions and aliases.

On the right side of the interface, you'll see three large dropzone buttons **New Folder**, **Delete** and **Open hidden**.

![](images/OrganizeActions.png)

### Changing variable order

The order of variables in the list can be changed by dragging and dropping them. Select multiple variables at once using shift-click and command-click (Mac)/control-click (PC). Once a group of variables has been selected they can be dragged as a group.

### Creating and using folders

Create a folder by clicking **New Folder** in the sidebar. This opens the **New folder name** dialog, where you can give the folder a name.

![](images/AddFolder.png)

The new folder will appear at the top of the variable list. You can drag and drop variables or folders into a folder to move them. Click the folder icon to open a folder and view and organize its contents.

When a folder is open, the path to that folder is shown at the top of the interface.

![](images/OrganizeBreadcrumbs.png)

Drag variables or folders to a location on the path to move them up in the hierarchy. Click on a location on the path to navigate to it directly.

### Editing variable and folder names, descriptions, and aliases

To edit a variable or folder name, description, or alias, double click it. When editing, you can use **Tab** to move to the next field or **Enter** to move to the next row (i.e. if you are editing a description you'll move to the next description).

### Hiding, unhiding, and deleting variables

Hidden variables or folders do not appear in the variables list. Deleted variables or folders are permanently removed from the dataset; any filters, analyses, or other variables derived from a deleted variable may be removed as a result.

To hide or delete variables or folders, either select them and click **Move to hidden** or **Delete**, or you can drag and drop them to these dropzones (note that these dropzones will only be active when folders or variables are being dragged or have been selected). Multiple variables and folders can be selected and dragged using shift-click to select a range and and command-click (Mac)/control-click (PC) to select multiple non-adjacent variables and folders.

You can view your hidden variables and folders by clicking **Open hidden** (this will only appear when no variables or folders are currently selected). This opens the **Hidden** folder. In the hidden folder you can move variables back to the visible variable order by dragging them to or clicking on **Unhide** after selecting them.
