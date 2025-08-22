# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1284da76-0271-4cbc-b143-0c9f7f9301ff",
# META       "default_lakehouse_name": "LH_GH_INT",
# META       "default_lakehouse_workspace_id": "65b0ce32-32d0-4180-9cff-39039acfc19c",
# META       "known_lakehouses": [
# META         {
# META           "id": "1284da76-0271-4cbc-b143-0c9f7f9301ff"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM LH_GH_INT.city_safety_seattle LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
