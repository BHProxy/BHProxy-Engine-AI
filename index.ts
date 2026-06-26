#!/usr/bin/env node

interface ProxyInput {
  proxyAddress: string;
  availability: number;
  latency: number;
  anonymity: number;
  protocolSupport: number;
  reputation: number;
  duplicateRisk: number;
}

interface ProxyOutput {
  proxyAddress: string;
  availabilityScore: number;
  latencyScore: number;
  anonymityScore: number;
  protocolSupportScore: number;
  reputationScore: number;
  duplicateRiskScore: number;
  overallProxyHealth: number;
  prioritySignal: string;
  anonymityLevel: string;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPrioritySignal(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    availability: "Availability",
    latency: "Latency",
    anonymity: "Anonymity",
    protocolSupport: "Protocol Support",
    reputation: "Reputation",
    duplicateRisk: "Duplicate Risk",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getAnonymityLevel(anonymity: number): string {
  if (anonymity <= 30) return "Transparent";
  if (anonymity <= 70) return "Anonymous";
  return "Elite";
}

export function analyzeProxy(input: ProxyInput): ProxyOutput {
  const scores = {
    availability: input.availability,
    latency: input.latency,
    anonymity: input.anonymity,
    protocolSupport: input.protocolSupport,
    reputation: input.reputation,
    duplicateRisk: input.duplicateRisk,
  };
  const overallProxyHealth = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    proxyAddress: input.proxyAddress,
    availabilityScore: input.availability,
    latencyScore: input.latency,
    anonymityScore: input.anonymity,
    protocolSupportScore: input.protocolSupport,
    reputationScore: input.reputation,
    duplicateRiskScore: input.duplicateRisk,
    overallProxyHealth,
    prioritySignal: getPrioritySignal(scores),
    anonymityLevel: getAnonymityLevel(input.anonymity),
  };
}

const args = process.argv.slice(2);
const proxyAddress = args[0] || "192.0.2.10:8080";
const availability = parseInt(args[1]) || 85;
const latency = parseInt(args[2]) || 70;
const anonymity = parseInt(args[3]) || 90;
const protocolSupport = parseInt(args[4]) || 80;
const reputation = parseInt(args[5]) || 75;
const duplicateRisk = parseInt(args[6]) || 65;

const result = analyzeProxy({
  proxyAddress, availability, latency, anonymity,
  protocolSupport, reputation, duplicateRisk,
});

console.log(`Proxy: ${result.proxyAddress}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Availability Score:            ${result.availabilityScore}/100  [${getStatus(result.availabilityScore)}]`);
console.log(`Latency Score:                 ${result.latencyScore}/100  [${getStatus(result.latencyScore)}]`);
console.log(`Anonymity Score:               ${result.anonymityScore}/100  [${getStatus(result.anonymityScore)}]`);
console.log(`Protocol Support Score:        ${result.protocolSupportScore}/100  [${getStatus(result.protocolSupportScore)}]`);
console.log(`Reputation Score:              ${result.reputationScore}/100  [${getStatus(result.reputationScore)}]`);
console.log(`Duplicate Risk Score:          ${result.duplicateRiskScore}/100  [${getStatus(result.duplicateRiskScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Proxy Health:          ${result.overallProxyHealth}/100`);
console.log(`Priority Signal:               ${result.prioritySignal}`);
console.log(`Anonymity Level:               ${result.anonymityLevel}`);
