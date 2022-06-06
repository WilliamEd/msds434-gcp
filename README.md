#**MDSD434-GCP Dev**

This is the Main Development branch for the Northwestern MS Data Science Analytics Application Engineering course - MSDS 434. 
The project built is for Covid-19 ML Forcasting.

#**Architecture Design**
![image](https://user-images.githubusercontent.com/9835157/172215695-4c369b75-40ca-4a11-9593-643571ae6c45.png)

Using a CI/CD pipeline and Google Cloud Platform (GCP) this project creates a app via the App Engine. The data used by the app is sourced from Google BigQuery's public dataset Covid-19.

![Forcast Image](https://user-images.githubusercontent.com/9835157/172074018-aac6c6c5-64f4-42d7-a43c-ee44371ecf97.PNG)

Resource is created with Dash and all code running this is set in Main.py

Testing is done through Git Actions

App.yaml is the file that sets gunicorn gate/server information for App Engine

App Engine was set to pull fromm development in Git as well for a test, however, it was return to manual for simplicity.

In BigQuery two queries where used one to create the model, the other to create the forcast. This was also loaded into main.

![Model](https://user-images.githubusercontent.com/9835157/172074216-40e17fe2-419f-4ba0-80c9-76a661d2791f.PNG)
![Forecast Query](https://user-images.githubusercontent.com/9835157/172074241-3ae9e7d3-117c-4f51-979c-68a5528a013b.PNG)

Logging is all done through the Logging application in GCP
![image](https://user-images.githubusercontent.com/9835157/172076138-53c87f26-014f-453d-9372-b0cb78d58e7c.png)

Billing is all tracked in the billing section of GCP
![image](https://user-images.githubusercontent.com/9835157/172076185-13e01ffe-59ad-4aa4-8b57-f986ebdcd957.png)
