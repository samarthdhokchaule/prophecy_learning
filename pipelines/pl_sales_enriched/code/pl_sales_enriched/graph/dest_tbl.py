from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_sales_enriched.config.ConfigStore import *
from pl_sales_enriched.functions import *

def dest_tbl(spark: SparkSession, in0: DataFrame):
    in0.write.format("delta").mode("overwrite").saveAsTable("`man_cata`.`myschema`.`dest_tbl_1`")
