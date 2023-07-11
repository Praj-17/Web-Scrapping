import requests
import json
import time

# Set the base URL for the LinkedIn API.
base_url = "https://api.linkedin.com/v2/"

from config import credentials

# Set your LinkedIn API credentials.
client_id = credentials.get('client_id', None)
client_secret = credentials.get('acess_token', None)
access_token = credentials.get('secret', None)

class ConnectLinkedIn:
    def __init__(self, client_id = client_id, client_secret = client_secret, access_token = access_token) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token

    # Define a function to get the new connections of a competitor.
    def get_new_connections(self, competitor_id, target = "company"):
        # Create the request URL.
        url = base_url + "companies/" + competitor_id + "/connections?filter=new"

        # Make the request.
        response = requests.get(url, headers={"Authorization": "Bearer " + access_token})

        # Check if the request was successful.
        if response.status_code == 200:
            # Get the new connections from the response.
            new_connections = json.loads(response.content)["data"]

            return new_connections
        else:
            # Print an error message.
            print("Error getting new connections: " + response.content)

    # Define a function to generate a hyper-personalized connection request.
    def generate_connection_request(self, new_connection):
        # Get the about us section of the competitor.
        about_us = requests.get(base_url + "companies/" + new_connection["company"]["id"] + "/about-us", headers={"Authorization": "Bearer " + access_token})

        # Get the job description of the new connection.
        job_description = requests.get(base_url + "people/" + new_connection["id"] + "/positions/" + new_connection["positions"][0]["id"], headers={"Authorization": "Bearer " + access_token})

        # Get the recent posts of the new connection.
        recent_posts = requests.get(base_url + "people/" + new_connection["id"] + "/posts?filter=recent", headers={"Authorization": "Bearer " + access_token})

        # Generate the connection request.
        connection_request = "Hi " + new_connection["firstName"] + ",\n\nI saw that you recently connected with " + new_connection["company"]["name"] + ". I'm also interested in " + new_connection["company"]["name"] + ", and I was wondering if you could tell me more about your role there.\n\nI've also read your about us section, and I'm impressed with your company's mission. I'm particularly interested in your work on " + about_us["contents"][0]["title"] + ".\n\nI've also taken a look at your job description, and I think I would be a good fit for the " + job_description["title"] + " position. I have a strong background in " + job_description["skills"][0]["name"] + ", and I'm confident that I could make a significant contribution to your team.\n\nI'd love to connect with you and learn more about your work. Please let me know if you're available for a chat.\n\nThanks,\n[Your Name]"

        return connection_request

if __name__ == "__main__":
    # Get the new connections of a competitor.
    competitor_id ="1039312" #"96451819" #my page
    con = ConnectLinkedIn()
    new_connections = con.get_new_connections(competitor_id)

    # Generate a hyper-personalized connection request for each new connection.
    for new_connection in new_connections:
        connection_request = con.generate_connection_request(new_connection)

        # Send the connection request.
        requests.post(base_url + "people/" + new_connection["id"] + "/connections", headers={"Authorization": "Bearer " + access_token}, data={"message": connection_request})

    # Wait 1 minute before checking for new connections again.
    time.sleep(60)
