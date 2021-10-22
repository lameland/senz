# senz
Senz - GCP Cloud Run sensitive information sharing tool

Required Environment Variables:

1. var: bucket
  - Bucket used to store secrets temporary. It's good to apply lifecycle policy with retention. 
2.  var: app_senz_sec_key
  - Flask "app.secret_key". This is used for sessions. Good idea to generate long, complicated string. 
