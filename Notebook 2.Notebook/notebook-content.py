# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "66187082-4d50-4812-ab63-805b17e449f3",
# META       "default_lakehouse_name": "LH_GH_INT",
# META       "default_lakehouse_workspace_id": "e4fdc84a-b2c0-446a-943a-bc4ce7d9d8c7",
# META       "known_lakehouses": [
# META         {
# META           "id": "66187082-4d50-4812-ab63-805b17e449f3"
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
