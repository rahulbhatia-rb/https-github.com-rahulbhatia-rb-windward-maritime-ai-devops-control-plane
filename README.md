# Windward Maritime AI DevOps Control Plane

Independent proof-of-work inspired by Windward's public Maritime AI platform, AWS partnership, MLOps foundation, APIs, streaming, analytical data systems, and agentic AI capabilities.

> Based only on public Windward information. This does not represent Windward's private architecture.

## Why this repo

Windward publicly describes a Maritime AI platform built around:
- data
- analytical databases
- streaming
- APIs
- MLOps
- mission-grade operational intelligence
- agentic AI workflows
- AWS ecosystem integration

That means platform engineering has to connect reliability, cloud infrastructure, streaming/data workloads, model operations, APIs, and secure AI-assisted workflows.

## Reference architecture

```text
External maritime / sensor feeds
          |
          v
   Ingestion / Streaming
          |
          +--> validation / schema controls
          +--> buffering / backpressure
          +--> replay / DLQ
          |
          v
   Analytical data platform
          |
          +--> batch / stream processing
          +--> feature / model data
          +--> API-serving data
          |
          v
        MLOps
          |
          +--> model build
          +--> validation
          +--> registry
          +--> deployment
          +--> monitoring
          |
          v
   Maritime AI applications
          |
          +--> APIs
          +--> mission workflows
          +--> agentic AI / GenAI
          |
          v
   Customers / operators
```

## AWS platform contract

An AWS-first platform baseline should make explicit:
- VPC segmentation
- private workloads
- IAM least privilege
- KMS encryption
- secrets lifecycle
- autoscaling
- multi-AZ resilience
- immutable artifacts
- backup / restore
- audit trails
- cost ownership

## Kubernetes / runtime platform

Standardize:
- requests / limits
- HPA / autoscaling
- PodDisruptionBudget
- topology spread
- workload identity
- NetworkPolicy
- graceful shutdown
- probes
- immutable images
- release metadata
- ownership labels

## Streaming reliability

Mission-grade data pipelines need:
- partition strategy
- schema compatibility
- replay
- DLQ
- consumer lag visibility
- backpressure controls
- idempotent processing
- retention ownership
- failure isolation

## MLOps reliability

Model operations should track:
- model version
- training data lineage
- feature lineage
- validation evidence
- deployment target
- rollback candidate
- model / data drift
- latency
- error rate
- cost per inference
- business-quality signals

## API platform

APIs should define:
- authentication / authorization
- rate limits
- SLO
- latency/error budgets
- tenant isolation
- versioning
- deprecation policy
- request tracing
- auditability

## Agentic AI controls

Windward publicly describes agentic workflows and AWS-powered GenAI tools.

Safe operational patterns:
- read-only tools by default
- tool allowlists
- tenant-aware authorization
- prompt/input validation
- secret isolation
- audit logs
- human approval for destructive actions
- traceable model/tool decisions

## Observability

Track four layers:

### Platform
- CPU / memory
- node health
- saturation
- network
- storage
- autoscaling

### Streaming
- throughput
- lag
- retry rate
- DLQ
- processing latency

### APIs
- request rate
- p50/p95/p99 latency
- 4xx / 5xx
- dependency latency
- tenant-level SLOs

### MLOps / AI
- model latency
- inference failures
- model version
- data freshness
- drift
- agent tool failures
- token / inference cost

## Incident model

```text
Detect
 -> classify customer / mission impact
 -> identify latest change
 -> correlate platform + data + model signals
 -> mitigate
 -> rollback / fail over
 -> restore service
 -> postmortem
 -> corrective action
```

## Cost engineering

Track:
- cost per API request
- cost per vessel / entity processed
- streaming cost per event
- storage growth
- observability retention
- model inference cost
- idle compute
- committed-use efficiency

## 30 / 60 / 90

### 0-30
- map platform, streaming, API and MLOps dependencies
- baseline SLOs / incidents / capacity
- identify cloud spend and reliability hotspots
- map model and deployment pipelines
- review security and tenant boundaries

### 31-60
- standardize Terraform / runtime modules
- improve progressive delivery
- define streaming and API health gates
- improve model deployment safety
- unify deployment markers with observability

### 61-90
- automate recurring failure prevention
- improve platform self-service
- implement cost / reliability dashboards
- strengthen AI tool-control boundaries
- exercise DR / failover paths

## Run locally

```bash
python -m unittest -v tests.test_gate
python src/cli.py examples/production.json
python src/cli.py examples/unsafe.json
```
