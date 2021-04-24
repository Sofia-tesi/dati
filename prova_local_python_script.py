# Databricks notebook source
import datetime
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--ImportDateWidget',    type=str)
parser.add_argument('--StartDateWidget',    type=str) 
args = parser.parse_args()

importDate = args.ImportDateWidget
StartDate = args.StartDateWidget

if importDate=="current_date":
  importDate = datetime.date.today()



print(importDate)



print(StartDate)

print(dbutils.fs.help())


