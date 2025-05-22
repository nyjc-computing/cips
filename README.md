# Campus Improvement Proposals

CIPs in the repository are published automatically on the web at https://nyjc-computing.github.io/cips/. To learn more about the purpose of CIPs, please start reading at [CIP 1](https://nyjc-computing.github.io/cips/cip-0001.html).

# Contributing to CIPs

Only members of [Nanyang System Developers](https://nyjc-computing.github.io/nanyang-system-developers/) may propose new CIPs.

To propose a CIP:
1. Create a new branch for your CIP.
2. Write up the CIP in [ReStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) (.rst) format.
3. Make a PR from your branch to `main`

To prevent effort drafting a CIP going to waste, you may wish to discuss it in [#general](https://discord.com/channels/690399114986389535/1353628761681166456) first to see if there’s support for the idea.

# Checking CIP formatting and rendering

## Render CIPs locally

```bash
# Install requirements
poetry install

# Build the PEPs
make html
```

The output HTML is found under the `_build/html` directory.
