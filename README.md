# Inverted-Index

Project Submission Guidelines:

# First Java Application Implementation and Execution on Docker

I decided to implement this portion of the project in Python as I am more familiar working with APIs in Python than I am in Java. I successfully got the user to input which files they would like to run the indexing algorithm on. However, this application only works on Docker when it is not using the API to interact with the cluster and programmatically request a job. 

# Docker to Local (or GCP) Cluster Communication

The API does not fully work when not running on Docker either, as I was having some Python version issues with external libraries that I needed for the cluster communication. However, I did write the API code to do a POST request to get a job submitted to the Cluster. What I still don't have is receiving the output response from the cluster.

# Inverted Indexing MapReduce Implementation and Execution on the Cluster (GCP)

This part of the project is working to how I aimed to implement it. It returns a long list of words and occurrences for those words in the files specified.
