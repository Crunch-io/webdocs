---
title: "Creating Variables"
audience: all
---

You can use Crunch.io to created variables that are based on existing
variables in a dataset. These variables will only be visible to you and will
appear in the My Variables group at the top of the variable list in the left
sidebar. Once created you can use these variables in analyses just like any
other variables.

To create a variable click **+New Variable** at the bottom of the variable
list in the left sidebar. This opens the New Variable page where you can
select what type of variable you want to create:

**Combined variables** \- To create a combined variable you will start with an existing categorical, multiple response, or array variable and combine categories of that variable to make a new variable with fewer categories. For example, starting with a variable that recorded people's opinions on issues on a scale from 1-10, you could combine the "1-3" responses into "Disagree", "4-7" into "Unsure", and "8-10" into "Agree". The type of variable created will be the same as the type of the variable it is based on. See [Creating a Combined Variable](crunch_creating-a-combined-variable.html) for more information.

**Categorical variables** \- To create a categorical variable you define each category in the new variable with a logical expression based on one or more existing variables. For example, you could create a variable that defined "Soccer Moms" as "Gender = Female" and "Children Under 18 = Yes" and "Single Dads" as "Gender = Male", "Children Under 18 = Yes", and "Marital Status = Single, Divorced, or Widowed". See [Creating a Categorical Variable](crunch_creating-a-categorical-variable.html) for more information.





###
