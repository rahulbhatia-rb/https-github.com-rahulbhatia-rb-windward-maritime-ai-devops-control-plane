REQUIRED={'aws': ['vpc', 'iam', 'kms', 'secrets', 'autoscaling', 'multi_az', 'backup_restore', 'audit_logs', 'cost_tags'], 'kubernetes': ['requests_limits', 'hpa', 'pdb', 'topology_spread', 'workload_identity', 'network_policy', 'graceful_shutdown', 'probes', 'immutable_images'], 'streaming': ['partition_strategy', 'schema_controls', 'replay', 'dlq', 'consumer_lag', 'backpressure', 'idempotency', 'retention_owner'], 'mlops': ['model_version', 'training_lineage', 'feature_lineage', 'validation', 'registry', 'deployment', 'rollback', 'drift', 'latency', 'cost_per_inference'], 'api': ['authn_authz', 'rate_limit', 'slo', 'latency_budget', 'tenant_isolation', 'versioning', 'tracing', 'auditability'], 'ai_agents': ['tool_allowlist', 'read_only_default', 'tenant_authz', 'input_validation', 'secret_isolation', 'audit_logs', 'human_approval', 'traceability'], 'observability': ['platform_metrics', 'streaming_metrics', 'api_metrics', 'model_metrics', 'deployment_markers', 'alert_owner', 'runbook', 'cost_metrics'], 'reliability': ['incident_owner', 'rollback', 'failure_domains', 'dependency_map', 'capacity_headroom', 'postmortem', 'corrective_action', 'dr_test'], 'iac_cicd': ['terraform', 'remote_state', 'locking', 'reviewed_plan', 'security_scan', 'immutable_artifact', 'progressive_delivery', 'health_gate', 'rollback_gate']}

def evaluate(spec):
    findings=[]
    for section, fields in REQUIRED.items():
        values=spec.get(section,{})
        for field in fields:
            if not values.get(field): findings.append(f'{section}.{field} is required')
    return {'allowed': not findings, 'findings': findings}
