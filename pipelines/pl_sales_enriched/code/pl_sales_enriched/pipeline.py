from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_sales_enriched.config.ConfigStore import *
from pl_sales_enriched.functions import *
from prophecy.utils import *
from pl_sales_enriched.graph import *

def pipeline(spark: SparkSession) -> None:
    df_adls_data = adls_data(spark)
    df_select_industry_fields = select_industry_fields(spark, df_adls_data)
    dest_tbl(spark, df_select_industry_fields)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("pl_sales_enriched").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_sales_enriched")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_sales_enriched", config = Config)(pipeline)

if __name__ == "__main__":
    main()
