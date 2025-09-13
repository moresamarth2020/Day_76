#!/usr/bin/env python
# coding: utf-8

# # Requests module in python
# - The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python. This module enables you to send HTTP requests using Python code and makes it possible to interact with APIs and web services.
# - Installation

# In[1]:


pip install requests


# #### Get Request
# - Once you have installed the Requests module, you can start using it to send HTTP requests. Here is a simple example that sends a GET request to the Google homepage:

# In[2]:


import requests
response = requests.get("https://bhulekh.mahabhumi.gov.in/")
print(response.text)


# #### Post Request
# - Here is another example that sends a POST request to a web service and includes a custom header:

# In[4]:


import requests

# Target POST URL (example, you'll need the correct endpoint)
url = "https://bhulekh.mahabhumi.gov.in/some_action_endpoint"

# Form data to send
payload = {
    "district": "Pune",
    "taluka": "Haveli",
    "village": "SomeVillage",
    # add other required fields here
}

# Optional headers to mimic browser request
headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# Create a session (to keep cookies)
session = requests.Session()

# First, get the page to establish session cookies (if needed)
session.get("https://bhulekh.mahabhumi.gov.in/")

# Then send the POST request
response = session.post(url, data=payload, headers=headers)

print(response.text)


# In[ ]:





# In[ ]:




