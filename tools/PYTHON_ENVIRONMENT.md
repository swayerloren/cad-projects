# Python Environment

Current venv path:

```text
C:\Users\LJ\CAD Projects\tools\.venv
```

Activation from PowerShell:

```powershell
& 'C:\Users\LJ\CAD Projects\tools\.venv\Scripts\Activate.ps1'
```

Direct Python command:

```powershell
& 'C:\Users\LJ\CAD Projects\tools\.venv\Scripts\python.exe'
```

## Venv Audit

`pyvenv.cfg` reports:

- Python version: `3.12.10`
- System site packages: `false`
- Base executable: `C:\Users\LJ\AppData\Local\Python\pythoncore-3.12-64\python.exe`
- Historical creation command references `C:\Users\LJ\OpenSCAD Projects\command link\tools\.venv`

Treat the historical creation path as metadata only. The current venv exists at `C:\Users\LJ\CAD Projects\tools\.venv`.

## Packages Seen

```text
contourpy==1.3.3
cycler==0.12.1
fonttools==4.62.1
kiwisolver==1.5.0
matplotlib==3.10.9
numpy==2.4.4
packaging==26.2
pandas==3.0.2
pillow==12.2.0
pip==26.0.1
pyparsing==3.3.2
python-dateutil==2.9.0.post0
sexpdata==1.0.2
six==1.17.0
tzdata==2026.2
```

## Outputs

Existing legacy/current output:

```text
C:\Users\LJ\CAD Projects\tools\output
```

New normalized analysis output folder:

```text
C:\Users\LJ\CAD Projects\tools\Analysis Output
```

Do not delete old outputs. New scripts should prefer `tools\Analysis Output` unless a project-specific path is better.

