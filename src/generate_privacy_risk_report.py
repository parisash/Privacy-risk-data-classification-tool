from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"

ASSET_INVENTORY_FILE = DATA_DIR / "data_asset_inventory.csv"
CONTROL_REQUIREMENTS_FILE = DATA_DIR / "privacy_control_requirements.csv"
RETENTION_POLICY_FILE = DATA_DIR / "retention_policy.csv"

OUTPUT_REGISTER_FILE = REPORTS_DIR / "privacy_risk_register.csv"
OUTPUT_REPORT_FILE = REPORTS_DIR / "privacy_executive_summary.md"


YES_PARTIAL_NO_SCORE = {
    "Yes": 0,
    "Partial": 1,
    "No": 2,
}

DATA_VOLUME_SCORE = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
}

ACCESS_LEVEL_SCORE = {
    "Public": 1,
    "Internal": 2,
    "Restricted": 3,
}

DATA_SENSITIVITY_SCORE = {
    "No": 0,
    "Partial": 2,
    "Yes": 4,
}


def load_csv(file_path: Path) -> pd.DataFrame:
    if not file_path.exists():
        raise FileNotFoundError(f"Required file not found: {file_path}")
    return pd.read_csv(file_path)


def validate_columns(df: pd.DataFrame, required_columns: list[str], file_name: str) -> None:
    missing = [column for column in required_columns if column not in df.columns]
    if missing:
        raise ValueError(f"{file_name} is missing required columns: {', '.join(missing)}")


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    assets = load_csv(ASSET_INVENTORY_FILE)
    controls = load_csv(CONTROL_REQUIREMENTS_FILE)
    retention = load_csv(RETENTION_POLICY_FILE)

    validate_columns(
        assets,
        [
            "asset_id",
            "asset_name",
            "business_area",
            "data_type",
            "contains_personal_data",
            "contains_sensitive_data",
            "data_volume",
            "access_level",
            "external_sharing",
            "data_residency_known",
            "encryption_enabled",
            "retention_defined",
            "business_owner",
            "system_owner",
            "current_status",
        ],
        "data_asset_inventory.csv",
    )

    validate_columns(
        controls,
        [
            "control_id",
            "control_area",
            "control_requirement",
            "applies_when",
            "evidence_required",
        ],
        "privacy_control_requirements.csv",
    )

    validate_columns(
        retention,
        [
            "data_type",
            "recommended_retention",
            "retention_rationale",
            "review_frequency",
        ],
        "retention_policy.csv",
    )

    return assets, controls, retention


def classify_data_asset(row: pd.Series) -> str:
    if row["contains_sensitive_data"] == "Yes":
        return "Sensitive"
    if row["contains_sensitive_data"] == "Partial":
        return "Potentially Sensitive"
    if row["contains_personal_data"] == "Yes":
        return "Personal"
    if row["contains_personal_data"] == "Partial":
        return "Potentially Personal"
    return "Low Privacy Impact"


def calculate_privacy_risk_score(row: pd.Series) -> int:
    personal_data_score = DATA_SENSITIVITY_SCORE.get(row["contains_personal_data"], 1)
    sensitive_data_score = DATA_SENSITIVITY_SCORE.get(row["contains_sensitive_data"], 1)
    data_volume_score = DATA_VOLUME_SCORE.get(row["data_volume"], 1)
    access_score = ACCESS_LEVEL_SCORE.get(row["access_level"], 1)

    external_sharing_score = 2 if row["external_sharing"] == "Yes" else 0
    residency_gap_score = YES_PARTIAL_NO_SCORE.get(row["data_residency_known"], 1)
    encryption_gap_score = YES_PARTIAL_NO_SCORE.get(row["encryption_enabled"], 1)
    retention_gap_score = YES_PARTIAL_NO_SCORE.get(row["retention_defined"], 1)

    return (
        personal_data_score
        + sensitive_data_score
        + data_volume_score
        + access_score
        + external_sharing_score
        + residency_gap_score
        + encryption_gap_score
        + retention_gap_score
    )


def assign_privacy_risk_rating(score: int) -> str:
    if score >= 16:
        return "Critical"
    if score >= 12:
        return "High"
    if score >= 8:
        return "Medium"
    return "Low"


def assign_recommended_action(row: pd.Series) -> str:
    if row["privacy_risk_rating"] == "Critical":
        return "Complete DPIA review, restrict access, confirm residency, define retention and validate encryption before continued use"
    if row["privacy_risk_rating"] == "High":
        return "Complete privacy review, address missing controls and document risk treatment decision"
    if row["privacy_risk_rating"] == "Medium":
        return "Review data minimisation, access and retention evidence during next governance cycle"
    return "Maintain current controls and review as part of routine governance"


def assign_governance_attention(row: pd.Series) -> str:
    if row["privacy_risk_rating"] in ["Critical", "High"]:
        return "Yes"
    if row["contains_sensitive_data"] == "Yes" and row["retention_defined"] != "Yes":
        return "Yes"
    if row["external_sharing"] == "Yes" and row["data_residency_known"] != "Yes":
        return "Yes"
    return "No"


def build_privacy_risk_register(
    assets: pd.DataFrame,
    retention: pd.DataFrame,
) -> pd.DataFrame:
    register = assets.merge(retention, on="data_type", how="left")

    register["data_classification"] = register.apply(classify_data_asset, axis=1)
    register["privacy_risk_score"] = register.apply(calculate_privacy_risk_score, axis=1)
    register["privacy_risk_rating"] = register["privacy_risk_score"].apply(assign_privacy_risk_rating)
    register["recommended_action"] = register.apply(assign_recommended_action, axis=1)
    register["governance_attention_required"] = register.apply(assign_governance_attention, axis=1)

    return register.sort_values(by="privacy_risk_score", ascending=False)


def markdown_table(df: pd.DataFrame, columns: list[str]) -> str:
    if df.empty:
        return "No records found."
    return df[columns].to_markdown(index=False)


def generate_report(register: pd.DataFrame, controls: pd.DataFrame) -> str:
    total_assets = register["asset_id"].nunique()
    sensitive_assets = register[register["contains_sensitive_data"] == "Yes"]["asset_id"].nunique()
    personal_assets = register[register["contains_personal_data"] == "Yes"]["asset_id"].nunique()
    externally_shared_assets = register[register["external_sharing"] == "Yes"]["asset_id"].nunique()
    high_or_critical_assets = register[
        register["privacy_risk_rating"].isin(["High", "Critical"])
    ]["asset_id"].nunique()
    governance_attention = register[
        register["governance_attention_required"] == "Yes"
    ]["asset_id"].nunique()

    risk_rating_summary = (
        register.groupby("privacy_risk_rating")["asset_id"]
        .nunique()
        .reset_index(name="asset_count")
        .sort_values(by="asset_count", ascending=False)
    )

    classification_summary = (
        register.groupby("data_classification")["asset_id"]
        .nunique()
        .reset_index(name="asset_count")
        .sort_values(by="asset_count", ascending=False)
    )

    business_area_summary = (
        register.groupby("business_area")["asset_id"]
        .nunique()
        .reset_index(name="asset_count")
        .sort_values(by="asset_count", ascending=False)
    )

    attention_items = register[
        register["governance_attention_required"] == "Yes"
    ].copy()

    report = f"""# Privacy Risk and Data Classification Executive Summary

## Overview

This report summarises a simulated privacy risk and data classification assessment.

The project demonstrates how a data asset inventory can be classified and assessed for privacy risk based on personal data, sensitive data, access level, sharing, residency, encryption and retention factors.

The workflow connects:

Data Asset Inventory -> Data Classification -> Privacy Risk Score -> Governance Attention -> Recommended Action

## Key Metrics

| Metric | Value |
|---|---:|
| Total data assets reviewed | {total_assets} |
| Assets containing personal data | {personal_assets} |
| Assets containing sensitive data | {sensitive_assets} |
| Assets shared externally | {externally_shared_assets} |
| High or Critical privacy risk assets | {high_or_critical_assets} |
| Assets requiring governance attention | {governance_attention} |

## Privacy Risk Rating Summary

{markdown_table(risk_rating_summary, ["privacy_risk_rating", "asset_count"])}

## Data Classification Summary

{markdown_table(classification_summary, ["data_classification", "asset_count"])}

## Business Area Summary

{markdown_table(business_area_summary, ["business_area", "asset_count"])}

## Governance Attention Items

{markdown_table(
        attention_items,
        [
            "asset_id",
            "asset_name",
            "business_area",
            "data_classification",
            "data_volume",
            "external_sharing",
            "data_residency_known",
            "encryption_enabled",
            "retention_defined",
            "privacy_risk_score",
            "privacy_risk_rating",
            "business_owner",
        ],
    )}

## Privacy Control Areas Considered

{markdown_table(
        controls,
        [
            "control_id",
            "control_area",
            "control_requirement",
            "evidence_required",
        ],
    )}

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
"""
    return report


def save_outputs(register: pd.DataFrame, report: str) -> None:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    register.to_csv(OUTPUT_REGISTER_FILE, index=False)
    OUTPUT_REPORT_FILE.write_text(report, encoding="utf-8")

    print("Privacy risk and data classification report generated successfully.")
    print(f"- {OUTPUT_REGISTER_FILE}")
    print(f"- {OUTPUT_REPORT_FILE}")


def main() -> None:
    assets, controls, retention = load_data()
    register = build_privacy_risk_register(assets, retention)
    report = generate_report(register, controls)
    save_outputs(register, report)


if __name__ == "__main__":
    main()
