# My GitHub Actions Lab 🚀

A project to master **GitHub Actions**.

## What I Learned
- [x] Workflows & Jobs
- [x] Caching
- [ ] Reusable Workflows

## Example Workflow
```yaml
name: CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
