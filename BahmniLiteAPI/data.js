var tags = ["registration", "api", "consultation", "login"]
var specs = [{"path":"specs/API/apiConsultation.html","name":"Consultation Test","scenarios":[{"name":"Verify the active patient queue in consultation module","tags":["api","consultation"]},{"name":"Verify user is able to save the consultation encounter for a patient","tags":["api","consultation"]}]},{"path":"specs/API/apiLogin.html","name":"Login Test","scenarios":[{"name":"Verify the login location is returning status code 200","tags":["api","login"]},{"name":"Verify login location is returning valid location","tags":["api","login"]}]},{"path":"specs/API/apiRegistration.html","name":"Registration Test","scenarios":[{"name":"Verify the user is able to create a new patient","tags":["api","registration"]},{"name":"Verify the user is able to update the existing patient","tags":["api","registration"]},{"name":"Verify the search results are fetched by Patient ID","tags":["api","registration"]},{"name":"Verify the search results are fetched by Patient Name","tags":["api","registration"]},{"name":"Verify the search results are fetched by Patient Phone Number","tags":["api","registration"]},{"name":"Verify the search results are fetched by Patient Alternate Phone Number","tags":["api","registration"]},{"name":"Verify the start visit and end the visit","tags":["api","registration"]}]}]