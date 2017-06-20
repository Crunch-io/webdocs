# Getting Started: Importing Data Files to Crunch

You can upload datasets into Crunch.io that come from 2 different file types: 1) comma-separated value (.csv) files and 2) SPSS .sav files. Depending on which one you have, please follow the instructions below. If you have a different file type, see the FAQ below. We recommend you have a web browser window and this vignette both open side-by-side.

## I have a .csv

Here is a toy .csv dataset that we will use as a reference.
[insert screenshot how_to_upload_csv_1.png]

There are two main stages to the upload process a) sending the file up to Crunch.io, and b) "cleaning" and organizing the data once it's in Crunch. Step "a" is very quick (seconds or minutes, depending on your internet connection speed) and step "b" can take minutes or hours, depending how much you want to polish the Crunch dataset.

### Uploading

The first step is to open up a browser tab and [log into Crunch](https://app.crunch.io/login). Then, open up a second tab and follow the instructions on [this page](http://support.crunch.io/crunch/crunch_importing-data.html)

Once uploaded, the dataset will look something like our example from above
[insert screenshot how_to_upload_csv_2.png]

The second step is to clean and organize the uploaded data, which we can break into a few substeps: i) rename variables, ii) organize variables into folders, iii) build "hierarchical" variables. Note that there are additional tools in Crunch you can use, for example, to estimate weights or excluded "bad" cases from the data, and we cover those in separate documents.

### Editing variable names

Here are the steps to rename variables in Crunch. In the upper left corner of the screen is the dataset's name, click on it and you will see "Properties".

After you click on "Properties", then you will see several tabs, for example the "Dataset Properties" tab where you can change the name of the dataset, and more importantly, the tab "Edit Variables"; click on the "Edit Variables" tab.

After you click on the "Edit Variables" tab you will see on the left side of the screen all of the variables in your survey, and on the right side of your screen some controls that we will use. First, on the right side of the screen, click the toggle to "Edit Names".

[insert screenshot how_to_upload_csv_3.png]

Now you can click on any of the variables on the left side of the screen and edit their "Name", for example changing "gender" to "Gender", "q1" to "Education", "q2_1" to "Ice Cream" and so forth. You can change any variables' "Descriptions" as well. When you have made all of the changes you'd like, look at the bottom left of the screen and click "Apply" and now all your changes are saved. Congratulations, you have given your variables a nice human-readable name and description. [Note, if you are using the toy .csv dataset, please change the names for the variables: 'q2_1' to 'q2_4' into "Ice Cream", "Cookies", "Pie" and "Cake" to follow along below.]

### Organizing variables

Onto the next step, organizing variables into folders. From the same "Edit Variables" tab (reached by clicking on the dataset's name > Properties > "Edit Variables"), on the right side of the screen click the toggle to "Organize".

[insert screenshot how_to_upload_csv_4.png]

In the "Organize" view, on the right side of the screen click on "New Folder", which functions like "create folder" on your Mac or PC, and give it a name, e.g. "Demographics".

Then on the left side of the screen, click once on any variable you'd like to move into the "Demographics" folder.

Now click a second time, hold the mouse button down and drag that variable on top of the "Demographics" folder. You have now made a folder and organized a variable into it. You can repeat this process as you see fit to organize all of the variables and we recommend putting each variable into a folder. [Note that to save time, if you hold the "shift" key you can select a continuous range of variables at once.]

Before moving on, in the lower left corner of the screen are 3 buttons: "save", "apply" and "close", let's click "save" so that we're back at the "Variable Summaries" view of the dataset.

### Building complex variable types

The third step - building "hierarchical" variables - what do we mean by "hierarchical" variables? It is best shown through example.

[insert screenshot how_to_upload_csv_5.png]

This question asks people to say whether they like or strongly like product "One" and product "Two", and so in essence this one "question" is actually asking two "subquestions" bound together in a "hierarchical" way. Unlike most data analysis tools, Crunch allows you to represent this type of question similarly to how you asked people... by displaying the data in a "hierarchical" way as well. Note, another form these types of questions often take is asking a "multiple response" such as "choose as many of these as apply" rather than forcing respondents to choose just one option than can choose > 1 if they desire.

Back to our example dataset, the variables with the names "Ice Cream", "Cookies", "Pie" and "Cake" (or named "q2_1" to "q2_4" if you did not change them earlier) were actually related in this way and so we'd like to build a "hierarchical" variable from them. To do so, we make sure to close the dataset "Properties" view and that we are in the normal views that summarize the data e.g. "Variable Summaries". Now in the lower left corner of the screen is a "+" icon which if we mouse over will change to "New Variable".

[insert screenshot how_to_upload_csv_6.png]

If we click on "New Variable" we see a screen with several options for making new variables and we want to click on "Build Array Variable" (we use "array" here because a "hierarchical" variable can be made into either an "array" or "multiple response" variable and so we had to choose one).

[insert screenshot how_to_upload_csv_7.png]

On the new screen it will say "Select or drag variable", which is asking you to look at the left edge of the screen at the folders of variables you made earlier, and then click on the names of whichever variables you'd like to bind into a "hierarchical" variable. In our example, I've clicked on the variables "Ice Cream", "Cookies", "Pie", and "Cake", and then given the new "hierarchical" variable the name "Dessert Preferences".

[insert screenshot how_to_upload_csv_8.png]

After you have chosen the variables you'd like, click on where it says "New Variable" directly above your chosen variables and type in a name.

Then at the bottom left of the screen click "Save" and below is what the now built "hierarchical" variables looks like in Crunch.io

[insert screenshot how_to_upload_csv_9.png]

There are other great tools inside Crunch to help you discover information in your data but we will stop this document for uploading a .csv here. To keep digging into the features please visit here http://support.crunch.io or contact us at support@crunch.io.




I have a SPSS .sav file

Here is a toy .sav dataset that we will use as a reference.
[insert screenshot how_to_upload_sav_1.png]

There are two main stages to the upload process a) sending the file up to Crunch.io, and b) "cleaning" and organizing the data once it's in Crunch. Step "a" is very quick (~5 minutes) and step "b" can take several hours depending how much you want to polish the Crunch dataset.

The first step is to open up a browser tab and log into Crunch. Then, open up a second tab and follow the instructions on this page:  http://support.crunch.io/crunch/crunch_importing-data.html

Once uploaded, the dataset will look something like our example from above
[insert screenshot how_to_upload_sav_2.png]

The second step is to clean and organize the uploaded data, which we can break into a few substeps: i) rename variables, ii) organize variables into folders, iii) convert "text"-type variables into "categorical"-type variables, iv) build "hierarchical" variables. [Note, there are additional tools in Crunch you can use, for example, to estimate weights or excluded "bad" cases from the data and we cover those in separate documents on http://support.crunch.io.]

Here are the steps to rename variables in Crunch. In the upper left corner of the screen is the dataset's name, click on it and you will see "Properties".

After you click on "Properties", then you will see several tabs, for example the "Dataset Properties" tab where you can change the name of the dataset, and more importantly, the tab "Edit Variables"; click on the "Edit Variables" tab.

After you click on the "Edit Variables" tab you will see on the left side of the screen all of the variables in your survey, and on the right side of your screen some controls that we will use. First, on the right side of the screen, click the toggle to "Edit Names".

[insert screenshot how_to_upload_csv_3.png]

Now you can click on any of the variables on the left side of the screen and edit their "Name", for example changing "gender" to "Gender", "q1" to "Education", "q2_1" to "Ice Cream" and so forth. You can change any variables' "Descriptions" as well. When you have made all of the changes you'd like, look at the bottom left of the screen and click "Apply" and now all your changes are saved. Congratulations, you have given your variables a nice human-readable name and description. [Note, if you are using the toy .sav dataset, please change the names for the variables: 'q2_1' to 'q2_4' into "Ice Cream", "Cookies", "Pie" and "Cake" to follow along below.]

Onto the second step, organizing variables into folders. From the same "Edit Variables" tab (reached by clicking on the dataset's name > Properties > "Edit Variables"), on the right side of the screen click the toggle to "Organize".

[insert screenshot how_to_upload_csv_4.png]

In the "Organize" view, on the right side of the screen click on "New Folder", which functions like "create folder" on your Mac or PC, and give it a name, e.g. "Demographics".

Then on the left side of the screen, click once on any variable you'd like to move into the "Demographics" folder.

Now click a second time, hold the mouse button down and drag that variable on top of the "Demographics" folder. You have now made a folder and organized a variable into it. You can repeat this process as you see fit to organize all of the variables and we recommend putting each variable into a folder. [Note that to save time, if you hold the "shift" key you can select a continous range of variables at once.]

Before moving on, in the lower left corner of the screen are 3 buttons: "save", "apply" and "close", let's click "save" so that we're back at the "Variable Summaries" view of the dataset.

Now for the third step, converting "text"-type variables into "categorical"-type variables. First, what do we mean by "text" variables and "categorical" variables? A "text" variable is when the data is stored in Crunch as a long list of text:

[insert screenshot how_to_upload_sav_3.png]

In comparison, a "categorical" variable is when the data is stored in Crunch as counts for each different category in that question:

[insert screenshot how_to_upload_sav_4.png]

Usually we want to represent data in Crunch as "categorical" rather than "text" so that we can make crosstabulations with it. The typical time when we want to leave a "text" variable as "text" is when the question was an "open-end" or "verbatim" where people wrote in whatever they wanted to a question, e.g. "Please tell us about why you love ice cream". And so unless you have an open-ended response question, we probably want to convert any variables that were imported into Crunch as "text" into being "categorical" instead.

How do we convert a variable from "text" to "categorical"? Go to the "Variable Summaries" view of the data, then mouse over the rectangle for a variable you want to convert, and in the upper right corner of that rectangle a little "gear" icon will appear, click on it.

[insert screenshot how_to_upload_sav_5.png]

Now mouse over and click on "convert to categorical".

[insert screenshot how_to_upload_sav_6.png]

Then mouse to the bottom of the card and click on "Convert".

[insert screenshot how_to_upload_sav_7.png]

Now the variable is converted to type "categorical".

[insert screenshot how_to_upload_sav_8.png]

You can do this as much as you would like and we recommend converting any "text" variable that is not an "open end" or "verbatim" to be a "categorical" (in the toy .sav data you can convert all of the 'q2' and 'q3' variables).

The third step - building "hierarchical" variables - what do we mean by "hierarchical" variables? It is best shown through example.

[insert screenshot how_to_upload_csv_5.png]

This question asks people to say whether they like or strongly like product "One" and product "Two", and so in essence this one "question" is actually asking two "subquestions" bound together in a "hierarchical" way. Unlike most data analysis tools, Crunch allows you to represent this type of question similar to how you asked people by displaying the data in a "hierarchical" way as well. Note, another form these types of questions often take is asking a "multiple response" such as "choose as many of these as apply" rather than forcing respondents to choose just one option than can choose > 1 if they desire.

Back to our example dataset, the variables with the names "Ice Cream", "Cookies", "Pie" and "Cake" (or named "q2_1" to "q2_4" if you did not change them earlier) were actually related in this way and so we'd like to build a "hierarchical" variable from them. To do so, we make sure to close the dataset "Properties" view and that we are in the normal views that summarize the data e.g. "Variable Summaries". Now in the lower left corner of the screen is a "+" icon which if we mouse over will change to "New Variable".

[insert screenshot how_to_upload_csv_6.png]

If we click on "New Variable" we see a screen with several options for making new variables and we want to click on "Build Array Variable" (we use "array" here because a "hierarchical" variable can be made into either an "array" or "multiple response" variable and so we had to choose one).

[insert screenshot how_to_upload_csv_7.png]

On the new screen it will say "Select or drag variable", which is asking you to look at the left edge of the screen at the folders of variables you made earlier, and then click on the names of whichever variables you'd like to bind into a "hierarchical" variable. In our example, I've clicked on the variables "Ice Cream", "Cookies", "Pie", and "Cake", and then given the new "hierarchical" variable the name "Dessert Preferences".

[insert screenshot how_to_upload_csv_8.png]

After you have chosen the variables you'd like, click on where it says "New Variable" directly above your chosen variables and type in a name.

Then at the bottom left of the screen click "Save" and below is what the now built "hierarchical" variables looks like in Crunch.io

[insert screenshot how_to_upload_csv_9.png]

There are other great tools inside Crunch to help you discover information in your data but we will stop this document for uploading a .sav here. To keep digging into the features please visit here http://support.crunch.io or contact us at [support@crunch.io](mailto:support@crunch.io).


# FAQs

* *What if I have an .xls or .xlsx file?* You're good; just open the file in Excel and then Save As as .csv format instead.
* *What about other file formats?* Likewise, if you can export from that program to .csv or .sav, you can upload as described here. Alternatively, if you use R or have access to someone who does, you can read the file in there and use our [R package](https://github.com/Crunch-io/rcrunch) functions to import the data. Regardless, we're always looking to expand the kinds of data we import natively, so let us know at [support@crunch.io](mailto:support@crunch.io) that you have another file type you'd like us to support.
* *Can anyone edit the contents of a dataset or only a subset of people?* There are 2 levels of permissions in Crunch: "editors" and "viewers". Editors can do more to alter a dataset (including delete it) and so generally there are only one or a small number of editors. If you uploaded the dataset then you are automatically an editor, which you can confirm because there will be a little padlock icon in the upper right corner of your Crunch screen.
