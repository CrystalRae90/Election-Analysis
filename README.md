# Election-Analysis

##Overview of Election Audit
The purpose of the election analysis was to analyze the votes cast and determine the outcome of the election. In order to do this succicently, a python script was run to determine the outcome of the election and summarize accordingly. 

##Election-Audit Results
- How many votes were cast in this congressional election?

To begin the analysis, we used python to open and read the data. The file path was previously defined as _file_to_load_ and by using the _open_ and _cvs.reader_ methods, we are able to read the data within python. As our original data had headers, we used the _next_ function to skip that row for all future tasks. To calculate the total number of votes, we can tally them based on the number of rows remaining. _total_votes_ had previously been initialized with a value of 0. By using  _for_ loop to loop through the remaining rows, we increase the _total_vote_ count by one. 

      # Initialize a total vote counter.
      total_votes = 0

      with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
        header = next(reader)
       
    # For each row in the CSV file.
     for row in reader:
        # Add to the total vote count
        total_votes = total_votes + 1
 
 The total number of votes cast was 369,711. 
 
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

To be able to break down the votes by county, we started by creating a list _county_list_ to hold the county names as well as a dictionary told hold each county' vote count. Using the appropriate index for the county name, we are able to incorporate an _if_ statement within the _for loop_. In this case as we cylcle through the rows, the _if_ statement checks to see if the county name was in the list previously. If not, then it adds it the list. We then are able to utilize the _county_votes_ dictionary to hold the county names as keys and preset their values to 0. As each row cycles through the appropriate key we are able to add 1, thus summing the total number of votes by county. This can be seen below. 


      county_list =[]
      county_votes={}

      for row in reader:
        
        # Add to the total vote count
        total_votes = total_votes + 1

        # 3: Extract the county name from each row.
        county_name = row[1]

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name]= 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

The results were as follows: 

Jefferson had 10.5% of the votes with 38,855 votes. Denver had 82.8% of the total votes with 306,055 votes and Arapahoe had 6.7% of the total with 24,801 votes. 

- Which county had the largest number of votes?

Overall, Denver county had the largest number of votes. They had over 80% of the total votes. This can be shown in the output of the script. 

<kbd>![County_Results.PNG](Resources/County_Results.PNG)<kbd>

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

##Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
