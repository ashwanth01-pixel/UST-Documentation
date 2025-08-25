CI-build and test
CDELIVERY-deploy the app with manual accept
CDEPLOY-deploy automatically
Events -pull/push/fork/issues
         |
       workflows
          |
        jobs
          |
        steps  

workflow components:
1. Events
events types:
- webhook events (push, pull request, release, issues)
- maunal events
- sheduled events (cron syntax)
2. jobs
3. steps
4. actions
5. runners

benefits
- supports variety of plugins
- can upload or write our actions
- self hosted runners (nvidia,unity)

1. workflows will be running on runner
2. runner can be self hosted  or also github provides linux,widnow and macos.
3. on runner the code will be downloaded , cache will be stored and also the artifacts.

