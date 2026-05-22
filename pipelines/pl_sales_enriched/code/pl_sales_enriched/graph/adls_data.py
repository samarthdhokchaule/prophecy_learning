from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sales_enriched.config.ConfigStore import *
from pl_sales_enriched.functions import *

def adls_data(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("year", StringType(), True), StructField("industry_code_ANZSIC", StringType(), True), StructField("industry_name_ANZSIC", StringType(), True), StructField("rme_size_grp", StringType(), True), StructField("variable", StringType(), True), StructField("value", StringType(), True), StructField("unit", StringType(), True), StructField("_c7", StringType(), True), StructField("_c8", StringType(), True), StructField("_c9", StringType(), True), StructField("_c10", StringType(), True), StructField("_c11", StringType(), True), StructField("_c12", StringType(), True), StructField("_c13", StringType(), True), StructField("_c14", StringType(), True), StructField("_c15", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/Volumes/man_cata/myschema/sales_volume/sample.csv")
