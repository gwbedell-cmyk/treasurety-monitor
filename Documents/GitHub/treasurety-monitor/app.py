import streamlit as st


st.set_page_config(
    page_title="Treasurety Monitor",
    page_icon="TM",
    layout="wide",
)


CERTIFICATE = {
    "atc_status": "Active",
    "certificate_id": "ATC-2026-000145",
    "certified_system": "Autonomous Accounts Payable Platform",
    "certification_tier": "Enterprise",
    "issuer": "Treasurety™",
    "operating_entity": "iThoth Systems Inc.",
    "issuer_line": "Created by Treasurety™, a subsidiary of iThoth Systems Inc.",
    "issue_date": "2026-05-28",
    "expiry_date": "2027-05-28",
    "verification_status": "Cryptographic fingerprint verified",
}


METRICS = [
    {
        "label": "Trust Score",
        "value": "92",
        "note": "Certified posture remains operationally trusted.",
        "tone": "green",
    },
    {
        "label": "Governance Health",
        "value": "Excellent",
        "note": "Control state aligns with the issued ATC.",
        "tone": "blue",
    },
    {
        "label": "Governance Drift",
        "value": "0.02%",
        "note": "No material drift against certification baseline.",
        "tone": "gold",
    },
    {
        "label": "Risk Exposure",
        "value": "Low",
        "note": "Runtime exposure remains inside approved bounds.",
        "tone": "green",
    },
    {
        "label": "Monitoring Status",
        "value": "Enabled",
        "note": "Continuous assurance is actively watching the system.",
        "tone": "blue",
    },
    {
        "label": "Last Verification",
        "value": "2 minutes ago",
        "note": "Latest verification cycle completed successfully.",
        "tone": "blue",
    },
]


DRIFT_INDICATORS = [
    ("Evidence Integrity", "Confirmed"),
    ("Governance Manifest", "Matched"),
    ("Assessment Hash", "Valid"),
    ("Runtime Profile", "Within Certified Bounds"),
    ("Material Drift", "Not Detected"),
]


ASSURANCE_EVENTS = [
    "Certificate fingerprint verified",
    "Governance profile validated",
    "Evidence integrity confirmed",
    "Runtime permissions checked",
    "No material drift detected",
]


TRUST_ARTIFACT = {
    "Certificate Fingerprint": "SHA256: 8af8e71f...42c9",
    "Evidence Hash": "SHA256: 7ac9210d...19be",
    "Governance Hash": "SHA256: 91fe02aa...e481",
    "Assessment Hash": "SHA256: cce40921...77af",
    "Verification URL": "verify.treasurety.com/ATC-2026-000145",
}


def inject_css() -> None:
    st.markdown(
        """
        <style>
            :root {
                --bg: #040812;
                --panel: rgba(11, 17, 29, 0.90);
                --panel-strong: rgba(7, 12, 22, 0.96);
                --border: rgba(144, 211, 255, 0.20);
                --border-strong: rgba(144, 211, 255, 0.34);
                --blue: #90d3ff;
                --gold: #e5cc43;
                --green: #37d88f;
                --text: #f2f8ff;
                --muted: #9dafc4;
                --soft: #d6e8f8;
            }

            .stApp {
                background:
                    radial-gradient(circle at 84% 8%, rgba(144, 211, 255, 0.16), transparent 29rem),
                    radial-gradient(circle at 8% 5%, rgba(229, 204, 67, 0.07), transparent 24rem),
                    radial-gradient(circle at 30% 88%, rgba(144, 211, 255, 0.08), transparent 32rem),
                    linear-gradient(135deg, #040812 0%, #07111f 46%, #02050c 100%);
                color: var(--text);
            }

            [data-testid="stHeader"] {
                background: transparent;
            }

            [data-testid="stToolbar"] {
                display: none;
            }

            .block-container {
                max-width: 1240px;
                padding: 2.6rem 2rem 3rem;
            }

            .hero {
                position: relative;
                overflow: hidden;
                border: 1px solid var(--border-strong);
                border-radius: 22px;
                padding: clamp(1.5rem, 4vw, 2.8rem);
                background:
                    linear-gradient(135deg, rgba(11, 17, 29, 0.94), rgba(3, 8, 17, 0.86)),
                    radial-gradient(circle at 88% 26%, rgba(144, 211, 255, 0.14), transparent 18rem);
                box-shadow: 0 34px 90px rgba(0, 0, 0, 0.48);
            }

            .hero::before {
                content: "";
                position: absolute;
                right: -6.5rem;
                top: -7.5rem;
                width: 28rem;
                height: 28rem;
                border-radius: 50%;
                border: 1px solid rgba(144, 211, 255, 0.16);
                box-shadow:
                    inset 0 0 0 3.8rem rgba(144, 211, 255, 0.030),
                    inset 0 0 0 7.6rem rgba(144, 211, 255, 0.024),
                    inset 0 0 0 11.4rem rgba(144, 211, 255, 0.016);
                opacity: 0.8;
            }

            .hero-content {
                position: relative;
                z-index: 1;
                max-width: 860px;
            }

            .eyebrow {
                color: var(--blue);
                font-size: 0.76rem;
                font-weight: 850;
                letter-spacing: 0.18em;
                text-transform: uppercase;
                margin-bottom: 0.8rem;
            }

            .title {
                color: var(--text);
                font-size: clamp(2.5rem, 5.4vw, 5.1rem);
                font-weight: 900;
                line-height: 0.94;
                margin: 0 0 0.85rem;
            }

            .subtitle {
                color: var(--soft);
                font-size: clamp(1.1rem, 2vw, 1.35rem);
                line-height: 1.55;
                margin: 0;
                max-width: 760px;
            }

            .strategic-line {
                color: var(--gold);
                font-size: 1.05rem;
                font-weight: 800;
                line-height: 1.45;
                margin-top: 1.25rem;
            }

            .issuer-line {
                color: var(--muted);
                font-size: 0.93rem;
                margin-top: 0.55rem;
            }

            .status-strip {
                display: flex;
                flex-wrap: wrap;
                gap: 0.75rem;
                margin-top: 1.65rem;
            }

            .pill {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                border: 1px solid rgba(144, 211, 255, 0.24);
                border-radius: 999px;
                background: rgba(144, 211, 255, 0.075);
                color: var(--soft);
                font-size: 0.86rem;
                font-weight: 760;
                padding: 0.58rem 0.9rem;
            }

            .pill strong {
                color: var(--blue);
            }

            .live-dot {
                width: 0.58rem;
                height: 0.58rem;
                border-radius: 999px;
                background: var(--green);
                box-shadow: 0 0 20px rgba(55, 216, 143, 0.90);
            }

            .section-title {
                color: var(--blue);
                font-size: 0.82rem;
                font-weight: 880;
                letter-spacing: 0.16em;
                margin: 2rem 0 0.9rem;
                text-transform: uppercase;
            }

            .metric-grid {
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 1rem;
            }

            .card,
            .metric-card,
            .event-card,
            .interpretation {
                border: 1px solid var(--border);
                background: linear-gradient(180deg, rgba(12, 19, 32, 0.92), rgba(6, 11, 20, 0.91));
                box-shadow: 0 22px 54px rgba(0, 0, 0, 0.30);
                border-radius: 18px;
            }

            .card {
                padding: 1.35rem;
            }

            .card-title {
                color: var(--text);
                font-size: 1.05rem;
                font-weight: 850;
                margin: 0 0 0.35rem;
            }

            .card-copy {
                color: var(--muted);
                font-size: 0.96rem;
                line-height: 1.55;
                margin: 0 0 1rem;
            }

            .detail-row,
            .artifact-row {
                display: flex;
                justify-content: space-between;
                gap: 1.5rem;
                border-bottom: 1px solid rgba(144, 211, 255, 0.11);
                padding: 0.84rem 0;
            }

            .detail-row:first-of-type,
            .artifact-row:first-of-type {
                padding-top: 0.2rem;
            }

            .detail-row:last-child,
            .artifact-row:last-child {
                border-bottom: 0;
                padding-bottom: 0;
            }

            .label {
                color: var(--muted);
                font-size: 0.78rem;
                font-weight: 800;
                letter-spacing: 0.08em;
                text-transform: uppercase;
            }

            .value {
                color: var(--text);
                font-weight: 780;
                text-align: right;
            }

            .value-blue {
                color: var(--blue);
            }

            .value-gold {
                color: var(--gold);
            }

            .metric-card {
                min-height: 150px;
                padding: 1.15rem;
            }

            .metric-label {
                color: var(--muted);
                font-size: 0.76rem;
                font-weight: 820;
                letter-spacing: 0.09em;
                text-transform: uppercase;
            }

            .metric-value {
                color: var(--text);
                font-size: clamp(1.7rem, 3vw, 2.3rem);
                font-weight: 900;
                line-height: 1.05;
                margin-top: 0.65rem;
            }

            .metric-value.green {
                color: var(--green);
            }

            .metric-value.blue {
                color: var(--blue);
            }

            .metric-value.gold {
                color: var(--gold);
            }

            .metric-note {
                color: var(--muted);
                font-size: 0.88rem;
                line-height: 1.45;
                margin-top: 0.75rem;
            }

            .indicator-grid {
                display: grid;
                gap: 0.75rem;
            }

            .indicator {
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 1rem;
                border: 1px solid rgba(144, 211, 255, 0.14);
                border-radius: 14px;
                background: rgba(144, 211, 255, 0.045);
                padding: 0.9rem 1rem;
            }

            .indicator-name {
                color: var(--soft);
                font-weight: 760;
            }

            .indicator-status {
                color: var(--green);
                font-weight: 850;
                text-align: right;
            }

            .event-list {
                display: grid;
                gap: 0.75rem;
            }

            .event-card {
                display: flex;
                align-items: center;
                gap: 0.85rem;
                padding: 0.95rem 1rem;
            }

            .check {
                width: 2rem;
                height: 2rem;
                border-radius: 999px;
                display: grid;
                place-items: center;
                flex: 0 0 auto;
                color: var(--green);
                border: 1px solid rgba(55, 216, 143, 0.42);
                background: rgba(55, 216, 143, 0.10);
                font-weight: 900;
            }

            .event-text {
                color: var(--soft);
                font-weight: 760;
            }

            .artifact-row .value {
                color: var(--blue);
                font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
                font-size: 0.92rem;
            }

            .interpretation {
                padding: 1.35rem;
                border-color: rgba(229, 204, 67, 0.28);
                background:
                    linear-gradient(135deg, rgba(229, 204, 67, 0.10), transparent 30rem),
                    rgba(7, 12, 22, 0.94);
            }

            .interpretation-title {
                color: var(--gold);
                font-size: 0.82rem;
                font-weight: 900;
                letter-spacing: 0.14em;
                text-transform: uppercase;
                margin-bottom: 0.6rem;
            }

            .interpretation-copy {
                color: var(--soft);
                font-size: 1.08rem;
                line-height: 1.55;
                margin: 0;
            }

            @media (max-width: 980px) {
                .metric-grid {
                    grid-template-columns: 1fr;
                }

                .block-container {
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
            }

            @media (max-width: 680px) {
                .detail-row,
                .artifact-row,
                .indicator {
                    align-items: flex-start;
                    flex-direction: column;
                    gap: 0.35rem;
                }

                .value,
                .indicator-status {
                    text-align: left;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        f"""
        <section class="hero">
            <div class="hero-content">
                <div class="eyebrow">Continuous Assurance Layer</div>
                <h1 class="title">Treasurety Monitor</h1>
                <p class="subtitle">Continuous Assurance for Certified Agentic Systems</p>
                <div class="strategic-line">
                    Certification verifies trust at a moment in time. Monitoring verifies trust over time.
                </div>
                <div class="issuer-line">{CERTIFICATE['issuer_line']}</div>
                <div class="status-strip">
                    <span class="pill"><span class="live-dot"></span> ATC Status: <strong>{CERTIFICATE['atc_status']}</strong></span>
                    <span class="pill">Certificate: <strong>{CERTIFICATE['certificate_id']}</strong></span>
                    <span class="pill">Verification: <strong>{CERTIFICATE['verification_status']}</strong></span>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_section_title(title: str) -> None:
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def render_certificate_status() -> None:
    details = [
        ("ATC Status", CERTIFICATE["atc_status"], "value-gold"),
        ("Certificate ID", CERTIFICATE["certificate_id"], "value-blue"),
        ("Certified System", CERTIFICATE["certified_system"], ""),
        ("Certification Tier", CERTIFICATE["certification_tier"], "value-gold"),
        ("Issuer", CERTIFICATE["issuer"], ""),
        ("Operating Entity", CERTIFICATE["operating_entity"], ""),
        ("Issue Date", CERTIFICATE["issue_date"], ""),
        ("Expiry Date", CERTIFICATE["expiry_date"], ""),
        ("Verification Status", CERTIFICATE["verification_status"], "value-blue"),
    ]
    rows = "".join(
        f"""
        <div class="detail-row">
            <div class="label">{label}</div>
            <div class="value {tone}">{value}</div>
        </div>
        """
        for label, value, tone in details
    )

    st.markdown(
        f"""
        <div class="card">
            <h2 class="card-title">Certificate Status</h2>
            <p class="card-copy">The ATC is monitored as a living trust artifact, not a static document.</p>
            {rows}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_governance_drift() -> None:
    indicators = "".join(
        f"""
        <div class="indicator">
            <div class="indicator-name">{name}</div>
            <div class="indicator-status">{status}</div>
        </div>
        """
        for name, status in DRIFT_INDICATORS
    )

    st.markdown(
        f"""
        <div class="card">
            <h2 class="card-title">Governance Drift Visibility</h2>
            <p class="card-copy">
                Monitor watches whether the live system remains aligned with the governance state
                under which the ATC was issued.
            </p>
            <div class="indicator-grid">{indicators}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metrics() -> None:
    cards = "".join(
        (
            '<div class="metric-card">'
            f'<div class="metric-label">{metric["label"]}</div>'
            f'<div class="metric-value {metric["tone"]}">{metric["value"]}</div>'
            f'<div class="metric-note">{metric["note"]}</div>'
            "</div>"
        )
        for metric in METRICS
    )
    html_content = f'<div class="metric-grid">{cards}</div>'
    st.markdown(html_content, unsafe_allow_html=True)


def render_events() -> None:
    events = "".join(
        f"""
        <div class="event-card">
            <div class="check">✓</div>
            <div class="event-text">{event}</div>
        </div>
        """
        for event in ASSURANCE_EVENTS
    )
    st.markdown(f'<div class="event-list">{events}</div>', unsafe_allow_html=True)


def render_trust_artifact() -> None:
    rows = "".join(
        f"""
        <div class="artifact-row">
            <div class="label">{label}</div>
            <div class="value">{value}</div>
        </div>
        """
        for label, value in TRUST_ARTIFACT.items()
    )

    st.markdown(
        f"""
        <div class="card">
            <h2 class="card-title">ATC Trust Artifact</h2>
            <p class="card-copy">
                The Agentic Trust Certificate is time-bounded and cryptographically verifiable.
                Monitor continuously checks certificate integrity, evidence alignment, and governance state.
            </p>
            {rows}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_interpretation() -> None:
    st.markdown(
        """
        <div class="interpretation">
            <div class="interpretation-title">Executive Interpretation</div>
            <p class="interpretation-copy">
                The certified system remains within its approved governance profile. No material drift
                has been detected since the last verification cycle. Continuous assurance is active.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


inject_css()
render_hero()

render_section_title("Certificate Status")
left, right = st.columns([1.05, 0.95], gap="medium")
with left:
    render_certificate_status()
with right:
    render_governance_drift()

render_section_title("Continuous Assurance Metrics")
render_metrics()

render_section_title("Recent Assurance Events")
render_events()

render_section_title("Cryptographic Trust Artifact")
render_trust_artifact()

render_section_title("Operational Readout")
render_interpretation()
