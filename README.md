# Privacy Risk Data Classification Tool

A practical data privacy and governance project that classifies data assets, scores privacy risk and generates evidence-ready data protection recommendations.

This project demonstrates how a data asset inventory can be transformed into a privacy risk register and executive-ready governance report.

## Project Summary

Privacy governance requires more than knowing that data exists. Organisations need to understand what kind of data they hold, who owns it, whether it contains personal or sensitive information, whether it is shared externally, whether retention is defined and whether protective controls are in place.

This project uses simulated data to demonstrate a practical privacy risk workflow.

The workflow connects:

```text
Data Asset Inventory → Data Classification → Privacy Risk Scoring → Governance Attention → Executive Report
```

## Why This Project Matters

Data privacy, cybersecurity GRC and information security roles increasingly require the ability to connect data handling practices with risk, controls, evidence and governance decisions.

A data asset is not properly governed unless an organisation can answer:

* What data is being processed?
* Does it contain personal or sensitive data?
* Who owns the data?
* Who manages the system?
* Is the data shared externally?
* Is data residency known?
* Is encryption enabled?
* Is retention defined?
* What privacy controls apply?
* Which assets require governance attention?

This project demonstrates how those questions can be structured and assessed using a simple Python-based workflow.

## Key Features

* Data asset inventory
* Data classification logic
* Personal and sensitive data flags
* Privacy risk scoring
* Retention policy mapping
* Data residency gap detection
* Encryption gap detection
* External sharing review
* Governance attention flagging
* Python-generated privacy risk register
* Executive-ready privacy report

## Repository Structure

```text
privacy-risk-data-classification-tool/
│
├── data/
│   ├── data_asset_inventory.csv
│   ├── privacy_control_requirements.csv
│   └── retention_policy.csv
│
├── src/
│   └── generate_privacy_risk_report.py
│
├── reports/
│   ├── privacy_risk_register.csv
│   └── privacy_executive_summary.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Input Files

### `data/data_asset_inventory.csv`

Contains simulated data asset records.

Each asset includes:

* Asset ID
* Asset name
* Business area
* Data type
* Personal data flag
* Sensitive data flag
* Data volume
* Access level
* External sharing status
* Data residency status
* Encryption status
* Retention status
* Business owner
* System owner
* Current status

### `data/privacy_control_requirements.csv`

Defines practical privacy control requirements.

Control areas include:

* Data classification
* Data minimisation
* Access control
* Encryption
* Retention management
* Data residency
* Third-party sharing
* DPIA review
* Logging and monitoring
* Privacy risk acceptance

### `data/retention_policy.csv`

Defines example retention expectations by data type.

It includes:

* Recommended retention period
* Retention rationale
* Review frequency

## Generated Outputs

Running the Python script generates two portfolio-ready outputs.

### `reports/privacy_risk_register.csv`

A structured privacy risk register that includes:

* Data classification
* Recommended retention
* Privacy risk score
* Privacy risk rating
* Governance attention flag
* Recommended action

### `reports/privacy_executive_summary.md`

An executive-style report that summarises:

* Total data assets reviewed
* Assets containing personal data
* Assets containing sensitive data
* Externally shared assets
* High or Critical privacy risk assets
* Governance attention items
* Privacy control areas considered
* Recommended actions

## How the Risk Logic Works

The script calculates privacy risk using factors such as:

```text
Personal Data + Sensitive Data + Data Volume + Access Level + External Sharing + Residency Gap + Encryption Gap + Retention Gap
```

It then assigns a privacy risk rating:

```text
Critical → Immediate governance action required
High → Privacy review and treatment decision required
Medium → Review during next governance cycle
Low → Maintain current controls
```

## Example Workflow

```text
Data Asset Inventory
        ↓
Retention Policy Mapping
        ↓
Privacy Control Requirements
        ↓
Python Risk Scoring Script
        ↓
Privacy Risk Register
        ↓
Executive Summary Report
```

## Example Governance Questions Answered

This project helps answer questions such as:

* Which data assets contain personal data?
* Which data assets contain sensitive data?
* Which assets are shared externally?
* Which assets have unclear data residency?
* Which assets have undefined retention?
* Which assets require DPIA-style review?
* Which business areas own the highest privacy risk assets?
* Which privacy controls should be evidenced?
* Which assets require immediate governance attention?

## Skills Demonstrated

This project demonstrates practical capability in:

* Data privacy governance
* Data classification
* Privacy risk assessment
* Sensitive data handling
* Data minimisation thinking
* Retention governance
* Privacy control mapping
* DPIA-style review logic
* Evidence-ready reporting
* Risk-based prioritisation
* Python reporting automation
* Executive privacy communication

## Career Relevance

This project aligns with roles such as:

* Data Privacy Analyst
* Privacy Governance Analyst
* Cybersecurity GRC Analyst
* Information Security Analyst
* Security Governance Analyst
* Risk and Compliance Analyst
* Data Governance Analyst
* Responsible AI Governance Analyst

## Practical Value

This project shows how privacy governance can be made structured, traceable and repeatable.

It demonstrates the ability to:

* Classify data assets
* Identify privacy risk indicators
* Link data handling to governance controls
* Prioritise high-risk datasets
* Support audit-readiness through evidence requirements
* Communicate privacy risk in business-friendly language

## Future Improvements

Planned improvements include:

* Add Streamlit dashboard
* Add privacy risk heatmap
* Add DPIA workflow template
* Add vendor/data processor mapping
* Add evidence expiry dates
* Add automated retention review flagging
* Add GDPR and Australian Privacy Principles mapping
* Add ISO 27001 and NIST Privacy Framework mapping
* Add Power BI-ready output
* Add sample screenshots of the generated report

## Disclaimer

This project uses simulated privacy and data classification data for portfolio and learning purposes. It does not contain real personal data, client data, employer data, health data or confidential organisational information.

## Author

**Parisa Shojaei**

Cybersecurity GRC · Cloud Security · Privacy Governance · Risk Analytics · AI Assurance | Turning risks into audit-ready evidence
