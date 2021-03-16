
# 1.Return a single risk type.
# 2.Return a list of risk types
# 3.Populate page with details of a single risk type


# There are two endpoints to achieve this

# Return Single Risk Type
# url = "http://127.0.0.1:8080/riskname/"
# request method get
# query params = {risk_type_name:"your_risk_type_name}

# This returns the risk type as specified in the query params
# If risk_type doesnt exist it returns an error messages


# Return all risk Type

# url = "http://127.0.0.1:8080/riskdetails/"

# This returns a list of all risk types available in the db with related fields



# Populate vuejs page with details of risk type

# "http://127.0.0.1:8080/risk_details/?risk_name=" + risk_type_name" 

#
