# Obsidian Setup Guide

## One-Time Setup (Already Done)

The following has been pre-configured:

```
wiki/.obsidian/
├── app.json                 # Core settings
├── appearance.json          # Theme settings
├── community-plugins.json   # Enables Dataview
├── graph.json               # Graph view colors by folder
└── plugins/
    └── dataview/            # Dataview plugin (pre-installed)
        ├── main.js
        ├── manifest.json
        ├── styles.css
        └── data.json        # Plugin settings
```

## Daily Usage

### Start Working

```bash
# Terminal 1: Activate environment
conda activate llm-wiki

# Terminal 2: Launch Obsidian (once)
obsidian
# → Open wiki/ folder as vault on first launch
# → After that, it remembers
```

### Workflow

| Claude Code | Obsidian |
|-------------|----------|
| `/wiki-ingest raw/paper.pdf` | See new page appear |
| `/wiki-query "..."` | Graph view updates |
| `/wiki-status` | Dataview tables refresh |

### Key Obsidian Views

- **Graph View**: Click graph icon in left sidebar
- **Dashboard**: Open `dashboard.md` for Dataview tables
- **Local Graph**: Right-click any page → "Open local graph"

### Graph View Colors

| Color | Folder |
|-------|--------|
| Blue | sources/ |
| Green | entities/ |
| Purple | concepts/ |
| Orange | analyses/ |

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Quick switcher | Ctrl+O |
| Command palette | Ctrl+P |
| Search in files | Ctrl+Shift+F |
| Toggle graph view | Ctrl+G |
| Back | Ctrl+Alt+← |
| Forward | Ctrl+Alt+→ |

## If Dataview Shows "Not Enabled"

1. Settings → Community plugins
2. Click "Turn on community plugins"
3. Dataview should already be in the list
4. Toggle it ON

## Files to Ignore (Already in .gitignore)

```
wiki/.obsidian/
```

This keeps your local Obsidian config out of git.
