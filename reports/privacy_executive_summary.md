# Privacy Risk and Data Classification Executive Summary

## Overview

This report summarises a simulated privacy risk and data classification assessment.

The project demonstrates how a data asset inventory can be classified and assessed for privacy risk based on personal data, sensitive data, access level, sharing, residency, encryption and retention factors.

The workflow connects:

Data Asset Inventory -> Data Classification -> Privacy Risk Score -> Governance Attention -> Recommended Action

## Key Metrics

| Metric | Value |
|---|---:|
| Total data assets reviewed | 10 |
| Assets containing personal data | 7 |
| Assets containing sensitive data | 3 |
| Assets shared externally | 6 |
| High or Critical privacy risk assets | 6 |
| Assets requiring governance attention | 6 |

## Privacy Risk Rating Summary

| privacy_risk_rating   |   asset_count |
|:----------------------|--------------:|
| High                  |             4 |
| Medium                |             3 |
| Critical              |             2 |
| Low                   |             1 |

## Data Classification Summary

| data_classification   |   asset_count |
|:----------------------|--------------:|
| Personal              |             3 |
| Sensitive             |             3 |
| Potentially Personal  |             2 |
| Low Privacy Impact    |             1 |
| Potentially Sensitive |             1 |

## Business Area Summary

| business_area       |   asset_count |
|:--------------------|--------------:|
| Research            |             2 |
| Marketing           |             2 |
| Customer Operations |             1 |
| Engineering         |             1 |
| GRC                 |             1 |
| Finance             |             1 |
| Human Resources     |             1 |
| Product Analytics   |             1 |

## Governance Attention Items

| asset_id   | asset_name                    | business_area       | data_classification   | data_volume   | external_sharing   | data_residency_known   | encryption_enabled   | retention_defined   |   privacy_risk_score | privacy_risk_rating   | business_owner           |
|:-----------|:------------------------------|:--------------------|:----------------------|:--------------|:-------------------|:-----------------------|:---------------------|:--------------------|---------------------:|:----------------------|:-------------------------|
| DA-003     | Research Participant Dataset  | Research            | Sensitive             | High          | Yes                | Partial                | Partial              | No                  |                   20 | Critical              | Research Team            |
| DA-009     | Clinical Trial Prototype Data | Research            | Sensitive             | Medium        | No                 | Partial                | Yes                  | No                  |                   16 | Critical              | Research Team            |
| DA-007     | Vendor Due Diligence Files    | GRC                 | Potentially Sensitive | Medium        | Yes                | Yes                    | Yes                  | Yes                 |                   13 | High                  | GRC Team                 |
| DA-002     | Employee HR Records           | Human Resources     | Sensitive             | Medium        | No                 | Yes                    | Yes                  | Yes                 |                   13 | High                  | HR Team                  |
| DA-001     | Customer Support Tickets      | Customer Operations | Personal              | High          | Yes                | Yes                    | Yes                  | Partial             |                   12 | High                  | Customer Operations Team |
| DA-008     | Product Usage Analytics       | Product Analytics   | Potentially Personal  | High          | Yes                | Partial                | Yes                  | No                  |                   12 | High                  | Product Team             |

## Privacy Control Areas Considered

| control_id   | control_area            | control_requirement                                                                                      | evidence_required                                               |
|:-------------|:------------------------|:---------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| PC-001       | Data Classification     | Data assets must be classified based on confidentiality privacy sensitivity and business impact          | Approved data classification register                           |
| PC-002       | Data Minimisation       | Only data necessary for the stated business purpose should be collected stored and processed             | Data minimisation review record                                 |
| PC-003       | Access Control          | Access to personal and sensitive data must be restricted to authorised users based on business need      | Access review export and approval record                        |
| PC-004       | Encryption              | Personal sensitive or restricted data should be protected using encryption at rest and in transit        | Encryption configuration evidence                               |
| PC-005       | Retention Management    | Retention periods must be defined and reviewed for datasets containing personal or sensitive information | Retention schedule and disposal review evidence                 |
| PC-006       | Data Residency          | Data location and cross-border processing arrangements should be understood and documented               | Data residency statement or vendor processing location evidence |
| PC-007       | Third-Party Sharing     | External sharing of personal or sensitive data must be reviewed and approved                             | Approved sharing record DPA or vendor review evidence           |
| PC-008       | DPIA Review             | A privacy impact review should be completed for high-risk personal or sensitive data processing          | DPIA checklist risk decision and approval evidence              |
| PC-009       | Logging and Monitoring  | Access to high-risk data assets should be monitored and reviewable                                       | Access logs monitoring configuration and review record          |
| PC-010       | Privacy Risk Acceptance | Unresolved privacy risks should have documented treatment decision owner and review date                 | Risk acceptance or treatment decision record                    |

## Privacy Governance Interpretation

The highest-risk data assets are those containing sensitive or personal data, high data volume, restricted access requirements, external sharing, unclear residency, incomplete encryption evidence or undefined retention.

These assets require stronger privacy governance because they may create data protection, compliance, audit-readiness or stakeholder trust risks.

## Recommended Actions

1. Prioritise Critical and High privacy risk assets for review.
2. Complete DPIA-style review for high-risk sensitive datasets.
3. Confirm retention periods for all personal and sensitive data assets.
4. Validate encryption evidence for restricted or sensitive datasets.
5. Confirm data residency and external sharing arrangements.
6. Review access permissions for restricted and sensitive assets.
7. Maintain a data classification register as part of ongoing privacy governance.

## Disclaimer

This report is generated from simulated privacy and data classification data for portfolio and learning purposes. It does not contain real personal data, client data, employer data or confidential organisational information.
