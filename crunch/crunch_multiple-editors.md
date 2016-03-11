---
title: "Datasets with Multiple Editors"
audience: all
---

When a dataset has multiple editors, only one at a time can commit certain changes to the dataset. This prevents data and metadata from getting out of sync. You must be the active editor to perform these actions:

* Edit [dataset properties](crunch_dataset-properties.html).
* Edit [variable properties](crunch_variable-properties.html).
* [Organize variables](crunch_organizing-variables.html).
* Create public [filters](crunch_filtering-data.html).
* Create public [variables](crunch_creating-variables-for-dataset-editors.html).

Dataset editors will see a lock icon near the upper-right corner. 

![](images/unlocked.png)

If unlocked, you will be able to do all the actions described above. Click the lock to stop editing.

![](images/locked.png)

If locked, you won't be able to make those kinds of edits without clicking the lock first. If another user is currently the active editor, you will see a warning that you are taking editing rights from them – if they are in the middle of an edit (e.g. they currently have variable or dataset properties open), they won't be able to save their changes. If no one is editing, the dataset will just unlock. 