# template-docs

MkDocs template for ICIQ-DMP project documentation.  
Fork this repo to create `PROJECT-docs` for any ICIQ project.

## Forking checklist

1. Fork this repo to `iciq-dmp/PROJECT-docs`.
2. In `mkdocs.yml`, update the **PROJECT-SPECIFIC** block at the top:
   - `site_name`, `site_url`, `repo_url`, `repo_name`
   - `extra.source_repo` — the GitHub repo containing the source code
   - `extra.project_name`
3. Edit `docs/index.md` with the project description.
4. Enable GitHub Pages in the repo settings (source: **GitHub Actions**).
5. Push to `main`/`master` — the `deploy-docs.yml` workflow will build and deploy.

## Structure

```
docs/
├── index.md            # Home page
├── tutorials/          # Learning-oriented content (write by hand)
├── how-to/             # Task-oriented content (write by hand)
├── reference/          # Auto-generated from source docstrings
├── explanation/        # Understanding-oriented content (write by hand)
└── gen_ref_pages.py    # mkdocs-gen-files script for reference generation
mkdocs.yml
requirements.txt
.github/workflows/
├── deploy-docs.yml         # Build + deploy to GitHub Pages
└── sync-from-template.yml  # PR from template-docs when it changes
```

## Syncing template changes

Run the `sync-from-template` workflow manually (or let it run on its Monday
schedule) to get a PR with the latest common changes from `template-docs`.
Resolve any conflicts in the project-specific block of `mkdocs.yml`.

## Local development

```bash
pip install -r requirements.txt

# Clone the project source alongside this repo:
git clone https://github.com/iciq-dmp/PROJECT_NAME source

mkdocs serve
```
