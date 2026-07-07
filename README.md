# Low-Overhead Automotive ECU Log Simulator

An optimized, deterministic automotive ECU telemetry stream generator designed and benchmarked under hardware architecture constraints.

## Technical Specifications & Features
- **Deterministic Task Scheduling:** Emulates dynamic embedded hardware statuses (INFO, WARN, CRITICAL) using calibrated mathematical frequencies (3 and 5 divisibility cycles).
- **Resource-Constrained Optimization:** Architecture-aware script written and validated on localized ARM64 Linux layers to evaluate strict system footprint and memory efficiency.
- **Zero Linting Overhead:** 100% compliant with PEP 8 standards with absolute zero Flake8 linter warnings or syntax style variations.

## Local Execution
To run the telemetry generator pipeline locally:
```bash
python my_monitor.py

## File log checking process
```bash
.\monitor.txt
