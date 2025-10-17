# Step by Step with GCP Data Fusion

## 1. Run BigQuery Script at a Given Time

- Create a pipeline in Data Fusion Studio.
- Use the BigQuery Execute plugin to run my SQL script.
  - Either embed the SQL directly or reference a saved query.
- Scheduled the pipeline using Cloud Scheduler or Data Fusion's built-in scheduler.

## 2. Save Result in GCP (Optional)

- Add a BigQuery Table sink to store the result.
- Alternatively, use Cloud Storage sink to save as CSV/JSON/Avro.

## 3. Export Result to On-Prem SQL Server

- Use the Database sink plugin in Data Fusion.
- Configure it to connect to my SQL server using JDBC.
  - JDBC connection string
  - SQL server credentials
  - Network access (VPN, Cloud Interconnect, or Cloud VPN)
- Map the output schema from BigQuery to the SQL Server table.

## Networking Considerations

To connect to on-prem SQL Server securely:

- Use Cloud VPN or Cloud Interconnect to establish a secure connection.
- Ensure firewall rules allow traffic from Data Fusion to SQL Server.
- We may need to configure Private IP for Data Fusion instance.

## Tips

- Use Wrangler in Data Fusion to preview and transform data before loading.
- Use parameterized pipelines if you want to reuse the same pipeline with different queries or destinations.
- Monitor pipeline runs via Cloud Logging and Data Fusion UI.
