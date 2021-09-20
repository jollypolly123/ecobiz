# ECOBIZ
 
To deploy changes, use:
```
gcloud builds submit --tag gcr.io/ecobiz-com/ecobiz
gcloud beta run deploy ecobiz --image gcr.io/ecobiz-com/ecobiz

firebase deploy
```

done pages:
- resources
- jobs
- directory

needs work:
- login, register
- postservices, postjoblisting
- forgotpassword