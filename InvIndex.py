from google.cloud import dataproc_v1

from google.cloud import storage
import json
import requests

class InvIndex():

    def __init__(self):
        self.client = dataproc_v1.ClusterControllerClient()
        self.REGION = 'us-west2'
        self.ZONE = 'us-west2-b'
        self.BUCKET = 'dataproc-staging-us-west2-610497321971-qs6cfefi'
        self.CLUSTER_NAME = 'cluster-c62e'
        self.PROJECT_ID = 'inverted-index-274019'
        self.selFile = ''
        inp = input("Select which files you'd like to get a word count of: \nPress 1 for Hugo\nPress 2 for Shakespeare\nPress 3 for Tolstoy\nPress 4 for All of them\n")
        if (int(inp) >= 1 and int(inp) <= 4):
            if (inp == 1):
                self.selectFile = 'gs://dataproc-staging-us-west2-610497321971-qs6cfefi/Hugo'
            elif (inp == 2):
                self.selectFile = 'gs://dataproc-staging-us-west2-610497321971-qs6cfefi/Shakespeare'
            elif (inp == 3):
                self.selectFile = 'gs://dataproc-staging-us-west2-610497321971-qs6cfefi/Tolstoy'
            else:
                self.selectFile = 'gs://dataproc-staging-us-west2-610497321971-qs6cfefi/Data'

        else:
            print("Invalid Input")
            exit(1)

        self.start_job_submission()

    def start_job_submission(self):
        #cluster = self.client.get_cluster(self.PROJECT_ID, self.REGION, self.CLUSTER_NAME)
        query = "https://dataproc.googleapis.com/v1/projects/{}/regions/{}/jobs:submit".format(self.PROJECT_ID, self.REGION)
        response = requests.post(
            query,
            headers={
                "job": {
                    "hadoopJob": {
                        "mainClass": "InvertedIndex",
                        "args": [
                            self.selectFile,
                            "gs://dataproc-staging-us-west2-610497321971-qs6cfefi/Output"
                        ],
                        "mainJarFileUri": "gs://dataproc-staging-us-west2-610497321971-qs6cfefi/JAR/invertedindex.jar"
                    }
                }
            }
        )
        if response:
            print('Request Success')
        else:
            print('Request Failed')



if __name__ == '__main__':
    ind = InvIndex()
