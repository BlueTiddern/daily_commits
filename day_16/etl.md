# ETL/ELT Concepts: Extract, Transform, Load

This document provides a production-grade overview of the three core stages in an ETL/ELT pipeline. It is intended for data engineering and analytics engineering teams requiring precise definitions and reproducible pipeline semantics.

---

## 1. Extract

**Extract** is the ingestion phase where data is retrieved from source systems. Extraction should preserve data fidelity and minimize disruption to source workloads.

**Characteristics:**
- **Sources:** OLTP databases, REST APIs, event streams, SaaS systems, flat files.
- **Access patterns:** full loads, incremental loads, Change Data Capture (CDC), log-based replication.
- **Constraints:** authentication, rate limits, schema drift detection, snapshot isolation.

**Common tooling:** Airbyte, Fivetran, Stitch, Kafka Connect, Debezium, custom ingestion workers.

---

## 2. Transform

**Transform** is the preparation and modeling stage. Raw data is cleaned, normalized, and shaped into analytical structures.  
In **ETL**, transformations occur before loading into the warehouse.  
In **ELT**, transformations occur inside the warehouse after raw data is loaded.

**Operations:**
- **Cleansing:** null handling, type coercion, deduplication.
- **Normalization / denormalization:** star schemas, SCD patterns.
- **Business logic:** metric definitions, joins, window functions.
- **Validation:** integrity checks, anomaly detection, schema guarantees.

**Common tooling:** dbt, Spark, Flink, SQL engines, Python processors.

---

## 3. Load

**Load** is the persistence phase where processed or raw data is stored in the destination system. Load operations must be idempotent, consistent, and operationally predictable.

**Load types:**
- **Append-only:** event logs, historical facts.
- **Merge/upsert:** dimension tables, CDC-based models.
- **Overwrite:** periodic full snapshots or reference datasets.

**Destinations:** Snowflake, BigQuery, Redshift, Databricks, data lakes, operational databases.

---

# Examples

---

## Example 1: API → Raw Landing → Analytics Warehouse (ELT Pattern)

**Scenario:** Daily ingestion of SaaS product usage metrics from a vendor REST API.

### Extract
- Scheduled job queries `/v1/events?date=YYYY-MM-DD`.
- Retrieves paginated JSON responses.
- Stores raw files in object storage:
  - `s3://landing/events/YYYY/MM/DD/*.json`
- Tracks incremental progress via a date watermark.

### Load (ELT sequence: Extract → Load → Transform)
- Warehouse loads JSON files using native bulk loaders.
- Raw data is stored as-is in a *bronze* layer.

### Transform
- dbt parses nested JSON into relational structures:
  - `stg_events` normalizes fields and types.
  - `int_events` deduplicates and cleans records.
  - `fct_user_events` computes engagement metrics.
- Tests enforce uniqueness and referential integrity.

---

## Example 2: OLTP Database → CDC Stream → Curated Data Mart (ETL Pattern)

**Scenario:** Near-real-time update of invoices and payments from a PostgreSQL OLTP database.

### Extract
- Debezium reads PostgreSQL WAL to capture inserts, updates, and deletes.
- Emits Avro messages to Kafka topic: `finance.invoices.cdc`.
- Includes before/after images and transaction metadata.

### Transform (ETL sequence: Extract → Transform → Load)
- Spark Structured Streaming consumes CDC events:
  - Rebuilds the latest invoice state via upserts.
  - Applies SCD Type 2 modeling for invoice status changes.
  - Normalizes monetary values using FX rate tables.
  - Validates business rules (e.g., no negative invoice totals).

### Load
- Writes curated tables to warehouse as micro-batches:
  - `dim_customer`
  - `fct_invoices`
  - `fct_payments`
- Uses warehouse-native merge semantics for upserts.
- Downstream dashboards update automatically.

---

