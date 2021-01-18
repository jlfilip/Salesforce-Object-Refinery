Salesforce Object Refinery

Use plain text, regular expressions, and an inclusionary or exclusionary method selection to refine big data sets (Salesforce Objects {.xml} or Comma Separated Values{.csv, .txt, .tsv}) into an easy to analyze CSV files for the purpose of better understanding your data. 

Regular Expression support allows for deep contextual analysis of your customer or enterprise data. You can create a structural linquistic algorithm to focus in on a common speech trend for a situation, or simply look for exact phrases that indicate an interesting data point.

Every entry in your data set is processed, one line at a time. If your criteria matches the record being processed, it is either included or excluded in the result data. 

---

How to use:

Step 1 

Export your dataset from Salesforce and place it in a directory within the 'Objects' directory. You can name the directory whatever you'd like, but it is useful to name it according to your use case or question that you're answering. 

Step 2

Build the Customer Object Field Index (COFI) file by executing 'Application/build_cofi.py'. Use the resulting output file, 'Objects/cofi.csv', to understand the available fields and their indicies from your data set, using them to build your 'Application/parameters.csv' file.

    Building your parameters file:

        From left to right, the fields required in the parameters file are:

            Batch ID 
                
                This can be whatever you'd like, it is ignored.

            Selected Method (0 or 1)

                Include ( parameter value: 0 )

                    For each record in the data structure, check the user-defined ‘field to search’ for content matching the user-defined String or Regular Expression, known as the ‘criteria’. For each record that matches, the user-defined ‘fields to return’ for the record are written to the result file. 

                Exclude ( parameter value: 1 )

                    For each record in the data structure, check the user-defined ‘field to search’ for content matching the user-defined String or Regular Expression, known as the ‘criteria’. For each record that matches, skip the record. For each record that does not match the ‘criteria’, the user-defined ‘fields to return’ for the record will be written to the result file. 

            Selected Objects

                Integer representing the file present within the target 'Objects/{Use Case Name}' directory. You may process multiple 'chunks' of a data set or multiple data sets that share the same structure at once by including multiple object values, separated by a hashtag '#'. (E.g. 0#1#2)

            Selected Field

                Integer representing the desired field to match against your plain text or Regular Expression. Only one value is supported.

            Return Fields

                Pipe delimited integers representing the fields from the original data set that you would like to either return or exclude from the processed data set, depending on the selected method. (E.g. 2|3|4)

            Search Criteria

                Your plain text or Regular Expression that you would like to use to refine the data set.

            Customer

                The name of the directory within the Objects directory that contains the data sets for this job.

Step 3

Execute Application/salesforce_object_refinery.py.

Step 4

Locate and utilize the result data sets from your processing jobs in 'Objects/Refined Objects/{Use Case Name}'.

---

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

Windows

Mac OS

Linux


Support:

Feel free to email me at contact@metasoft.co


Donate:

If you find this tool useful, please consider donating: https://www.paypal.com/donate?token=pFAWAhSL14n6iqjra-ebwwZt2sNSIxXZzMhFdZSpLGQXy_NVTCDw7OgUupzS0BxBAAjN2GbI-hO1hdjL

Bitcoin address:
bc1qwemuj6pnvvnyjzfrhq6hdhz53l4z9wxa65h37l
