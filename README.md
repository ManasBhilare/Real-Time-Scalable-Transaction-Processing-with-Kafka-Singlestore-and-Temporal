# Real Time Scalable Transaction Processing with Kafka Singlestore and Temporal

## Overview
This project is a distributed transaction processing system using **Apache Kafka**, **Temporal**, **MySQL (SingleStore)**, and **Grafana** for monitoring. The system can handle large-scale transaction data efficiently with **data partitioning, parallelization, and distributed computing**.

## Features
- **Kafka Producers & Consumers**: Producers generate transaction events and send them to Kafka topics. Consumers process and store transactions in MySQL.
- **Temporal Workflows**: Used for **fraud detection and transaction validation**.
- **MySQL (SingleStore)**: Handles scalable data storage and high-performance queries.
- **Grafana Dashboard**: Real-time visualization of transaction data.
- **Parallelization & Partitioning**: Ensures high throughput and scalability.

## System Architecture
1. **Kafka Producer** generates and pushes transaction events.
2. **Kafka Consumer** reads messages and stores them in MySQL.
3. **Temporal Workflow** validates transactions.
4. **Grafana** queries MySQL to visualize transaction trends.
5. **Partitioning & Parallelization** handle high-volume data efficiently.

## Installation and Setup

### Prerequisites
- **Docker & Docker Compose** (for Kafka, MySQL, and Temporal)
- **Python 3.8+** (for Kafka producers/consumers and Temporal workflows)
- **Grafana** (for visualization)
- Install required Python libraries:
  ```sh
  pip install kafka-python pymysql temporalio
  ```

### Starting Services
1. **Start Zookeeper & Kafka**:
   ```sh
   docker-compose up -d
   ```
2. **Start Temporal Server**:
   ```sh
   docker run -d --network=host temporalio/auto-setup
   ```
3. **Start Kafka Producer & Consumer**:
   ```sh
   python kafka_producer.py
   python kafka_consumer.py
   ```
4. **Run Temporal Worker**:
   ```sh
   python temporal_workflow.py
   ```
5. **Access Grafana Dashboard** at:
   ```
   http://localhost:3000
   ```

## Scalability and Performance
- **SQLification**: Optimized queries for faster performance.
- **Partitioning**: Data distributed across nodes to balance the load.
- **Parallel Processing**: Multiple consumers for concurrent processing.
- **Distributed Systems**: Kafka, Temporal, and MySQL ensure fault tolerance.
- **Handling Millions of Queries**: Partitioned tables + indexing improve query speed.

## Conclusion
This system provides a **scalable, fault-tolerant, and efficient** method for processing financial transactions in real-time. It ensures **high availability** and **real-time analytics** using **Kafka, MySQL, and Grafana**.
