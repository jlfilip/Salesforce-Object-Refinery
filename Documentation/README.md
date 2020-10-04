Salesforce Object Refinery

Use plain text, regular expressions, and an inclusionary or exclusionary method selection to refine big data sets (Salesforce Objects {.xml} or Comma Separated Values{.csv, .txt, .tsv}) into an easy to analyze CSV files for the purpose of better understanding your data. 

Regular Expression support allows for deep contextual analysis of your customer or enterprise data. You can create a structural linquistic algorithm to focus in on a common speech trend for a situation, or simply look for exact phrases that indicate an interesting data point.

Every entry in your data set is processed, one line at a time. If your criteria matches the record being processed, it is either included or excluded in the result data. 



This tool allows you to perform ad-hoc transformation of large common format data structures quickly on your local machine.

The advantage of using this tool is that you do not have to write a new script each time you are given a new dataset to analyse. It also allows you to use Regular Expressions on Salesforce Objects and Anaplan modules (Exports), which neither allow you to do within their SaaS platforms. 

Use Case Example:

Your director asks you to find out how many customers are asking for enablement of features that they are contractually entitled to have, but are not enabled for them. 

Step 1	
Export Support Case emails from Salesforce and place the file inside of a folder with a name of your choice that you create within the Customer directory.

Step 2
Build the Customer Object Field Index (COFI) file by executing the build_cofi.py file within the Application directory.

Step 3
Open the COFI file from the Customer directory and use the index values therein to configure the parameters.csv file.

Step 4
Execute the object_engine.py file from the Application directory.

Step 5
Collect the result records from the Search Results directory and begin your standard analysis practices.


Processing Methods:
Include ( parameter value: 0 )

For each record in the data structure, check the user-defined ‘field to search’ for content matching the user-defined String or Regular Expression, known as the ‘criteria’. For each record that matches, the user-defined ‘fields to return’ for the record are written to the result file. 

Exclude ( parameter value: 1 )

For each record in the data structure, check the user-defined ‘field to search’ for content matching the user-defined String or Regular Expression, known as the ‘criteria’. For each record that matches, skip the record. For each record that does not match the ‘criteria’, the user-defined ‘fields to return’ for the record will be written to the result file. 


Supported Data Structures:
XML (E.g. Salesforce Objects)
CSV (E.g. Salesforce Exports, Anaplan Exports, Database Exports)
TSV (E.g. Salesforce Anaplan Exports, Database Exports)
TXT (E.g. Salesforce Anaplan Exports, Database Exports)


Result Data Structure:
CSV


Requirements:
Python (2.7 or 3+)


Supported Platforms:
UNIX / Mac OS
Linux
