# NoSQL Database
### Maximize availability at the expense of consistency.
### Better choice for storing semi-structured and unstructured data
### Data models associated with the NoSQL concept are
#### Key-value Databases (Redis, MemcacheDB)
* They work by storing and managing associative arrays(dictionary or hash table). it consists of a collection of key-value pairs in which a key serves as a unique identifier to retrieve an associated value. Commonly used in caching, message queuing, and session management.
#### Columnar Databases (Cassandra, Apache HBase)
* They store data in columns. each column is stored in a separate file or region in the system’s storage first entry in one column is related to the first entry in other columns. widely used for data analytics.
#### Document-oriented Databases (MongoDB, Couchbase)
* They store data in the form of documents. each document has a unique identifier — its key — and the document itself serves as the value. regular use in e-commerce, blogging, and analytics platforms.
#### Graph Databases (OrientDB, Neo4j)
* They don’t insist that data adhere to a predefined schema. they add an extra layer to the document model by highlighting the relationships between individual documents. regular use in fraud detection, recommendation engines.
# Introduction to data lakes
## Data Lake
* central location that holds a large amount of data in its native, raw format. it uses a flat architecture and object storage to store the data.‍
### Pros
* open format
* highly durable and low cost
* unique ability to ingest raw data in a variety of formats (structured, unstructured, semi-structured) 
#### When properly architected, it has the ability to 
* Power data science and machine learning
* Quickly and seamlessly integrate diverse data sources and formats
* Centralize, consolidate, and catalogue your data
* Democratize your data by offering users self-service tools
### Challenges
* Reliability issues
* Slow performance
* Lack of security features
#### The answer to the challenges of data lakes is the lakehouse. it solves the challenges by adding a transactional storage layer on top.
#### Lakehouse uses similar data structures and data management but instead runs them directly on cloud data lakes
### Lakehouse best practices
* Use the data lake as a landing zone for all of your data
* Mask data containing private information before it enters your data lake
* Secure your data lake with role- and view-based access controls
* Build reliability and performance into your data lake by using Delta Lake
* Catalog the data in your data lake
