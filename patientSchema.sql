DROP DATABASE IF EXISTS patientDB;

CREATE DATABASE patientDB;

USE patientDB;

CREATE TABLE heartMonitors (
  id int(11) NOT NULL AUTO_INCREMENT,
  account_id int(11) DEFAULT NULL,
  ip_address varchar(100) DEFAULT NULL,
  hardware_address varchar(100) DEFAULT NULL,
  serial_number varchar(255) NOT NULL DEFAULT '',
  info JSON,
  last_reported datetime DEFAULT NULL,
  last_info datetime DEFAULT NULL,
  online tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (id)
) DEFAULT CHARSET=utf8mb4;
