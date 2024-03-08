variable "credentials" {
  description = "My Credentials"
  default     = "../keys/data-engineering-zoom-413802-676a43f8dfc0.json"
}

variable "location" {
  description = "location for cloud services"
  default     = "US"
}

variable "region" {
  description = "region for cloud services"
  default     = "us-central1"
}

variable "project" {
  description = "Project id"
  default     = "data-engineering-zoom-413802"
}

variable "bq_dataset_name" {
  description = "My big query dataset name"
  default     = "ski_resort_weather_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "raw_ski_resort_weather"
}

variable "gcs_storage_class" {
  description = "bucket storage class"
  default     = "STANDARD"
}

variable "google_compute_instance_name" {
  description = "compute instance name"
  default     = "ski-resort-weather-vm"
}
