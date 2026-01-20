# Databricks notebook source
df = spark.read.csv()

# COMMAND ----------

df.count()

# COMMAND ----------

df.join(df2,right)
