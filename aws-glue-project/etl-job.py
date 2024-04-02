import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "serverless", table_name = "csvdata", transformation_ctx = "datasource0")

datasink4 = glueContext.write_dynamic_frame.from_options(frame = datasource0, connection_type = "s3", 
connection_options = {"path": "s3://serverless-glue-job/parquetdata//"}, format = "parquet", transformation_ctx = "datasink4")
job.commit()
