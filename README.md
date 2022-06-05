# msds434-gcp
MDSD434-GCP Dev

This is the Main Development branch for the MSDS 434 Covid-19 Forcasting project.

This project uses ML to forcast probible cases in Germany from Google's Bigquery open source data.

![Forcast Image](https://user-images.githubusercontent.com/9835157/172074018-aac6c6c5-64f4-42d7-a43c-ee44371ecf97.PNG)

Resource is created with Dash and all code running this is set in Main.py

Testing is done through Git Actions

App.yaml is the file that sets gunicorn gate/server information for App Engine

App engine was set to pull form development in Git as well for a test, however, it was return to manual for simplicity.

In BigQuery two queries where used one to create the model, the other to create the forcast. This was also loaded into main.

![Model](https://user-images.githubusercontent.com/9835157/172074216-40e17fe2-419f-4ba0-80c9-76a661d2791f.PNG)
![Forecast Query](https://user-images.githubusercontent.com/9835157/172074241-3ae9e7d3-117c-4f51-979c-68a5528a013b.PNG)
