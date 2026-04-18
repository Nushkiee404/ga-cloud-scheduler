# Job Scheduling in Cloud Computing Using Genetic Algorithm

> **Research Paper Project** | B.Tech AI/ML — Chandigarh Group of Colleges, Landran  
> **Author:** Anushka | **Supervisor:** [Professor's Name]  
> **Duration:** April 2026 – May 2026  
> **Status:** 🟡 In Progress

---

## Overview

This repository contains all code, datasets, results, and documentation for a research paper on optimizing job scheduling in cloud computing environments using a Genetic Algorithm (GA).

Classical scheduling algorithms (FCFS, Round Robin, Min-Min) fail to efficiently handle the NP-hard complexity of real-world cloud workloads. This work proposes a GA-based scheduler that minimizes **makespan** and maximizes **resource utilization**, benchmarked against classical baselines using the **CloudSim Plus** simulation framework.

---

## Research Objectives

- Study existing job scheduling algorithms in cloud computing
- Design and implement a Genetic Algorithm-based scheduler
- Simulate cloud environments using CloudSim Plus
- Compare GA vs FCFS, Round Robin, Min-Min on key metrics
- Produce a publishable research paper

---

## Repository Structure

```
ga-cloud-scheduler/
│
├── /code
│   ├── ga_scheduler.py          # GA implementation (chromosome, fitness, crossover, mutation)
│   ├── baselines.py             # FCFS, Round Robin, Min-Min baseline schedulers
│   └── cloudsim_config/         # CloudSim Plus simulation configuration files
│
├── /data
│   ├── workload_50tasks.csv     # Experiment input: 50 tasks, varied execution times
│   ├── workload_100tasks.csv    # Experiment input: 100 tasks
│   └── workload_200tasks.csv    # Experiment input: 200 tasks (stress test)
│
├── /results
│   ├── makespan_comparison.png  # Bar chart: GA vs baselines on makespan
│   ├── utilization_chart.png    # Resource utilization comparison
│   └── raw_results.xlsx         # All experiment data (all runs, all algorithms)
│
├── /docs
│   ├── paper_draft.pdf          # Current draft of the research paper
│   └── literature_notes.md     # Summary notes on papers read
│
└── README.md                    # This file
```

---

## Metrics Evaluated

| Metric | Description |
|---|---|
| **Makespan** | Total time to complete all tasks (lower = better) |
| **Resource Utilization** | % of VM capacity used (higher = better) |
| **Throughput** | Tasks completed per unit time (higher = better) |

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python 3.x | GA implementation, data processing |
| CloudSim Plus | Cloud environment simulation |
| Java 11+ | CloudSim integration |
| Matplotlib / Seaborn | Result visualization |
| Overleaf (LaTeX) | Paper writing |
| Zotero | Reference management |

---

## Progress Log

| Week | Status | Key Milestone |
|---|---|---|
| Week 1 | ✅ Done | Cloud scheduling foundations + literature review |
| Week 2 | 🔄 In Progress | GA design + CloudSim setup |
| Week 3 | ⏳ Upcoming | Implementation + experiments |
| Week 4 | ⏳ Upcoming | Results analysis + paper writing |

---

## Live Research Document

📝 **Working research log (Google Doc):** [Insert link here]  
All daily progress, literature notes, GA design decisions, and paper draft sections are maintained there.

---

## Key References

1. Zhan, Z. H., et al. — *Cloud Computing Resource Scheduling and a Survey of Its Evolutionary Approaches.* ACM Computing Surveys, 2015.
2. Kalra, M., & Singh, S. — *A review of metaheuristic scheduling techniques in cloud computing.* Egyptian Informatics Journal, 2015.
3. Calheiros, R. N., et al. — *CloudSim: A toolkit for modeling and simulation of cloud computing environments.* Software: Practice and Experience, 2011.

---

## Contact

**Anushka**  
B.Tech — Artificial Intelligence & Machine Learning (3rd Year)  
Chandigarh Group of Colleges, Landran  
