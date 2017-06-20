The variable organizer allows dataset editors to sort variables into groups and determine the order in which they will appear in the sidebar. It can also be used to quickly edit variable names, descriptions, and aliases.

If the dataset you wish to organize is already shared with other you users, you may with to consider [creating a draft](crunch_draft-and-publish.html) before organizing it (or making other large changes). This will allow you to assure that the dataset organization appears as you expect before pushing the reorganized dataset to your clients.

Open the variable organizer by [opening dataset properties](crunch_dataset-properties.html) and then selecting the **Edit Variables** tab.

![](images/OrganizeVariables.png)

Variables are listed in their current order, along with their descriptions and aliases.

On the right side of the interface, you'll see the **Actions** sidebar.

![](images/OrganizeActions.png)

The options available in this sidebar depend on what mode you are in (**Organize** or **Edit Names**) and whether you have any variables selected. See below for more information.

### Changing variable order

The order of variables in the list can be changed by dragging and dropping them. Select multiple variables at once using shift-click and command-click (Mac)/control-click (PC). Once a group of variables has been selected they can be dragged as a group.

### Creating and using folders

Create a folder by clicking **Add Folder** in the **Actions** sidebar. This opens the **New folder name** dialog, where you can give the folder a name.

![](images/AddFolder.png)

The new folder will appear at the top of the variable list. You can drag and drop variables into the folder to move them. Click the folder icon to open the folder and view and organize its contents.

When a folder is open, the path to that folder is shown at the top of the interface.

![](images/OrganizeBreadcrumbs.png)

Drag variables to a location on the path to move them up in the hierarchy. Click on a location on the path to navigate to it directly.

### Editing variable and folder names, descriptions, and aliases

To edit variable and folder names, descriptions, and aliases, slide the toggle to **Edit Names** in the **Actions** sidebar. This puts the interface into **Edit** mode. While in edit mode:

* You can click any variable or folder name, description, or alias to edit it. You can use **Tab** to move to the next field or **Enter** to move to the next row (i.e. if you are editing a description you'll move to the next description).
* You cannot arrange variables or put them into folders. If you need to arrange variables, click **Organize** in the **Actions** sidebar to return to **Organize** mode.

### Hiding, unhiding, and deleting variables

Hidden variables do not appear in the sidebar, but any variables derived from them will be unaffected. Deleted variables are permanently removed from the dataset; any filters, analyses, or other variables derived from a deleted variable may be removed as a result.

When a variable or variables are selected, actions that can be performed on them will appear at the bottom of the **Actions** sidebar. Click **Hide** to hide a variable (or group of selected variables). Once hidden, the variable will disappear. You can view hidden variables in the Organize interface by toggling on **Show Hidden** in the **Actions** sidebar, and then unhide them by selecting them and selecting **Unhide**.

Permanently delete a variable by clicking **Delete**.
