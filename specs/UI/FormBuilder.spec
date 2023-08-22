# Form-Builder

## Admin should be able to create a form using form-builder

tags: ui

* Login to Bahmni snomed location "General Ward" as a "admin"
* Open "Implementer interface" module
* Create a form with form name as "Test Form"
* create obs "Height"

   |Property |
   |---------|
   |Mandatory|
   |AddMore  |
   |Abnormal |
* create obs "Is admission to hospital required?"

   |Property|
   |--------|
   |Url     |
* Create obs group "Coronary Artery Disease, Progress" and add an ecl query for "Coronary Artery Disease, Risk factors"

   |Property    |
   |------------|
   |Notes       |
   |Url         |
   |AutoComplete|
* Save data
* Click Publish button
* Click back button
* Login to Bahmni snomed location "General Ward" as a "receptionist"
* Create new patient with random details and start an OPD visit
* Logout and Login to Bahmni snomed location "General Ward" as a "doctor"
* Open clinical tab
* Enter Form Values and validate no error is displayed on save "consultation/observations/testForm"
* Click back button
* Goto All sections and search the newly created patient
* Validate obs "consultation/observations/testForm" on the patient clinical dashboard
* Click back button
* Click back button
* Open "Reports" module
* Select start date, end date and "HTML" format for "SNOMED Form builder form Report" and click on run button
* Validate the report generated for Snomed form builder form Report "consultation/observations/testForm"
* Click on home page
* Logout and Login to Bahmni snomed location "General Ward" as a "receptionist"
* visit is closed at the front desk
* Login to openMRS as user "admin"
* Goto Administration
* Delete the form from the openMRS