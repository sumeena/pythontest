Feature: Super admin authentication and Authorization

    Scenario: test logged out user is redirected to login window
        Given we have a logged out user
        when she navigates to backoffice login window
        then she is redirected to the login window
        
    Scenario: test login
        Given we have an admin user
        when he logs in as admin
        then he should see the main dashboard
