"""
advanced_threat_detector.py
----------------------------
Moteur de détection avancée de menaces pour SIEM
Détecte : APT, menaces internes, zero-day, comportements malveillants
Intègre : Machine Learning, Threat Intelligence, MITRE ATT&CK, OWASP Top 10
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json
import requests
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pickle
import hashlib
import ipaddress
import os
from collections import Counter

# === DATA CLASSES ===

@dataclass
class ThreatIndicator:
    """Indicateur de menace (IoC)"""
    ioc_type: str  # ip, domain, hash, pattern
    value: str
    confidence: float  # 0.0 à 1.0
    source: str
    timestamp: datetime
    description: str


@dataclass
class SecurityIncident:
    """Incident de sécurité structuré"""
    id: str
    type: str  # apt_behavior, insider_threat, zero_day_exploitation
    severity: str  # critical, high, medium, low
    confidence: float
    source_ips: List[str]
    affected_assets: List[str]
    indicators: List[ThreatIndicator]
    timeline: List[Dict]
    mitigation_steps: List[str]
    timestamp: datetime
    status: str = "open"
    mitre_techniques: List[str] = None  # Ex: ["T1059", "T1078"]
    owasp_categories: List[str] = None  # Ex: ["A03", "A01"]


# === CLASSE PRINCIPALE ===

class AdvancedThreatDetector:
    def __init__(self, elasticsearch_url="http
