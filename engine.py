#!/usr/bin/env python3
"""
BHProxy Engine AI
An intelligent proxy analysis system that combines automated network
validation with AI-assisted detection to identify unhealthy, duplicate,
low-quality, and potentially abusive proxy endpoints.
https://bhproxy.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_signal(scores: dict) -> str:
    labels = {
        "availability": "Availability",
        "latency": "Latency",
        "anonymity": "Anonymity",
        "protocol_support": "Protocol Support",
        "reputation": "Reputation",
        "duplicate_risk": "Duplicate Risk",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_anonymity_level(anonymity: int) -> str:
    if anonymity <= 30:
        return "Transparent"
    elif anonymity <= 70:
        return "Anonymous"
    return "Elite"


def analyze_proxy(
    proxy_address: str,
    availability: int = 85,
    latency: int = 70,
    anonymity: int = 90,
    protocol_support: int = 80,
    reputation: int = 75,
    duplicate_risk: int = 65,
) -> dict:
    """
    Analyze and score proxy quality signals separately.

    Args:
        proxy_address: Proxy IP:port address
        availability: Availability score (0-100)
        latency: Latency score (0-100)
        anonymity: Anonymity score (0-100)
        protocol_support: Protocol support score (0-100)
        reputation: Reputation score (0-100)
        duplicate_risk: Duplicate risk score (0-100)

    Returns:
        dict with individual signal scores and overall proxy health
    """
    scores = {
        "availability": availability,
        "latency": latency,
        "anonymity": anonymity,
        "protocol_support": protocol_support,
        "reputation": reputation,
        "duplicate_risk": duplicate_risk,
    }
    overall_proxy_health = round(sum(scores.values()) / 6)

    return {
        "proxy_address": proxy_address,
        "availability_score": availability,
        "latency_score": latency,
        "anonymity_score": anonymity,
        "protocol_support_score": protocol_support,
        "reputation_score": reputation,
        "duplicate_risk_score": duplicate_risk,
        "overall_proxy_health": overall_proxy_health,
        "priority_signal": get_priority_signal(scores),
        "anonymity_level": get_anonymity_level(anonymity),
    }


if __name__ == "__main__":
    proxy_address = sys.argv[1] if len(sys.argv) > 1 else "192.0.2.10:8080"
    availability = int(sys.argv[2]) if len(sys.argv) > 2 else 85
    latency = int(sys.argv[3]) if len(sys.argv) > 3 else 70
    anonymity = int(sys.argv[4]) if len(sys.argv) > 4 else 90
    protocol_support = int(sys.argv[5]) if len(sys.argv) > 5 else 80
    reputation = int(sys.argv[6]) if len(sys.argv) > 6 else 75
    duplicate_risk = int(sys.argv[7]) if len(sys.argv) > 7 else 65

    result = analyze_proxy(
        proxy_address, availability, latency, anonymity,
        protocol_support, reputation, duplicate_risk
    )

    print(f"Proxy: {result['proxy_address']}")
    print("=" * 45)
    print(f"Availability Score:            {result['availability_score']}/100  [{get_status(result['availability_score'])}]")
    print(f"Latency Score:                 {result['latency_score']}/100  [{get_status(result['latency_score'])}]")
    print(f"Anonymity Score:               {result['anonymity_score']}/100  [{get_status(result['anonymity_score'])}]")
    print(f"Protocol Support Score:        {result['protocol_support_score']}/100  [{get_status(result['protocol_support_score'])}]")
    print(f"Reputation Score:              {result['reputation_score']}/100  [{get_status(result['reputation_score'])}]")
    print(f"Duplicate Risk Score:          {result['duplicate_risk_score']}/100  [{get_status(result['duplicate_risk_score'])}]")
    print("=" * 45)
    print(f"Overall Proxy Health:          {result['overall_proxy_health']}/100")
    print(f"Priority Signal:               {result['priority_signal']}")
    print(f"Anonymity Level:               {result['anonymity_level']}")
