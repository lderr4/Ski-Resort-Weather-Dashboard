# Ski-Resort-Weather-Dashboard


[Link to Live Dashboard](https://lookerstudio.google.com/reporting/09bbe597-d530-4135-a1c4-fe7f2c9969ef) **UPDATE: due to reaching API call limit, the dashboard no longer shows weather forecasts (historical data still shown)**

A fully deployed ETL pipeline and dashboard so I can easily check the weather report for my favorite ski resorts! Additionally, there is a bulk weather pipeline that uses spark to transform a large dataset and put it directly into BigQuery!

## Architecture Diagram
![architecture_diagram.png](https://github.com/lderr4/Ski-Resort-Weather-Dashboard/blob/main/architecture_diagram.png)

## Tools and Technologies
- Cloud - [Google Cloud Platform](https://cloud.google.com/)
- Infrastructure as Code - [Terraform](https://www.terraform.io/)
- Containerization - [Docker](https://www.docker.com/), [Docker Compose](https://www.docker.com/)
- Large Scale Data Processing - [Spache Spark](https://spark.apache.org)
- Orchestration - [Mage.ai](https://www.mage.ai)
- Data Lake - [Google Cloud Storage](https://cloud.google.com/storage)
- Data Warehouse - [BigQuery](https://cloud.google.com/bigquery)
- Dashboard - [LookerStudio](https://lookerstudio.google.com/u/0/navigation/reporting)
- Language - [Python](https://www.python.org)

## Requirements
- Configured Google Cloud Platform Account with [Google Cloud CLI](https://cloud.google.com/sdk/docs/initializing)
- [Terraform configured with Google Cloud Account](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_1_basics_n_setup/1_terraform_gcp/windows.md#terraform)

## Setup

API Credentials:

Go to https://openweathermap.org, make a free account, and save free API key.

Setup Terraform Infrastructure:
```
cd terraform
terraform init
terraform plan
terraform apply
```

Inside Google Cloud Compute Instance .ssh tunnel:

1. Run vm_setup script to install required technologies.
2. Upload Google Cloud Credentials key into VM.
3. Setup up Google Cloud credentials and .env file:
```
# Move GCP key into correct folder
mv key.json Ski-Resort-Weather-Dashboard/keys

# Create .env file. Fill in these values as desired.
cd Ski-Resort-Weather-Dashboard
echo "PROJECT_NAME=
POSTGRES_DBNAME=
POSTGRES_SCHEMA=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
OPENWEATHERMAP_API_KEY=
GCP_PROJECT_ID=" >> .env


make build

make run
```

Getting external access to the Mage Instance inside the Virtual Machine:

1. Go to the Virtual Machine in Google Cloud Console.
2. Network Interfaces --> nic0
3. On the left-hand side click 'Firewall'
4. Click 'Create Firewall Rule'
5. IP Ranges: your IP address/32
6. Ports: TCP: 6789
7. Click Create. Make sure the rule is set for the VM's firewall rules.
8. Navigate to VM external IP:6789






