# RFID-M0 Documentation

Documentation for the **RFID-M0** autonomous monitoring device developed by the MIBE technical platform at IPHC.

This repository contains the source files used to build the RFID-M0 documentation website.

## Repository

The **GitLab repository is the primary project repository**. The GitHub repository is maintained as a mirror.

- **GitLab:** <https://gitlab.in2p3.fr/rfid-m0/rfid.m0.wiki>
- **GitHub:** <https://github.com/Julien-768/rfid-m0-wiki>

## Documentation website

The latest version of the documentation is available online:

**<https://rfid-m0.pages.in2p3.fr/rfid.m0.wiki/latest/>**

## Contents

The documentation covers the complete RFID-M0 project, including:

- device operation;
- user procedures;
- configuration;
- hardware architecture;
- electronic boards;
- power supply;
- RFID antennas;
- assembly;
- programming;
- manufacturing;
- testing and maintenance;
- advanced technical topics.

The documentation is available in **English and French**.

## Repository structure

```text
rfid.m0.wiki/
├── docs/               # Documentation source files
├── overrides/          # MkDocs theme customizations
├── mkdocs.yml          # MkDocs configuration
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project/tool configuration
├── .markdownlint.json  # Markdown linting configuration
└── .prettierrc         # Prettier configuration
```

## Requirements

The documentation is built using **MkDocs** with the **Material for MkDocs** theme.

Install the required Python packages with:

```bash
pip install -r requirements.txt
```

## Local development

To preview the documentation locally:

```bash
mkdocs serve
```

The development server is then available at:

```text
http://127.0.0.1:8000/
```

To build the static website:

```bash
mkdocs build
```

The generated website is placed in the `site/` directory.

## Firmware

The RFID-M0 firmware is maintained in a separate repository.

- **GitLab:** <https://gitlab.in2p3.fr/rfid-m0/rfid.m0.code>
- **GitHub:** <https://github.com/Julien-768/rfid-m0-code>

Firmware changes that affect device operation or documented behaviour should be reflected in this repository.

## Contributing

Documentation improvements, corrections, and clarifications are welcome.

When modifying documentation, please keep the structure and terminology consistent with the existing project documentation.

## License

This documentation is distributed under the **GNU General Public License v3.0**.

See [`LICENSE.txt`](LICENSE.txt) for the complete license text.

## Project

**RFID-M0**
MIBE Technical Platform — IPHC
