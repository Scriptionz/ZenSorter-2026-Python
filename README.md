# ZenSorter v16.0 📁✨

ZenSorter is a safe, ultra-fast, and modular Python utility designed to achieve ultimate digital peace by automating file organization. It scans your messy target directory, handles duplication with cryptographic precision, and brings total order. 

It is designed with a **Zero-Dependency** philosophy—no `pip install` required, just pure native Python power. You don't need to touch the core logic; simply tune the `SETTINGS` panel at the top of the script, and you're ready to go!

---

## 🚀 Ultimate Features

* **🧬 Smart SHA-256 Deduplication:** It analyzes the unique digital fingerprint (hash) of your files. Even if two identical twins have different filenames, ZenSorter detects them, saves your disk space, and isolates exact duplicates inside the `Duplicates_Vault`.
* **📦 Time Capsule Sorting:** Go beyond basic sorting. ZenSorter can automatically build a time-capsule hierarchy (`Category/Year/Month/`) based on when the file was last modified—perfect for massive, chaotic photo/video archives.
* **📡 Zen Watcher Mode (Live Automation):** Turn on `watch_mode` and let the script run silently in the background. The moment a new file drops into your target folder, an invisible hand instantly moves it to its rightful place.
* **🛡️ Duplicate Protection:** If two completely different files share the same name, ZenSorter automatically appends a precise timestamp counter to prevent overwriting.
* **📊 Beautiful CLI Dashboard:** Packed with adaptive ANSI terminal colors and a clean execution panel that gives you instant feedback on your system status.
* **📝 Automated Reporting:** Generates a detailed `ZenSorter_Summary.txt` log file at the end of every clean-up session.
* **🛠️ Developer Friendly:** Out-of-the-box support for 30+ major extensions across Images, Documents, Videos, Audio, Programming, Archives, and Executables.

---

## ⚙️ Configuration Layer

Tuning the engine is incredibly easy. Just open the script and modify the `SETTINGS` panel:

```python
SETTINGS = {
    "ask_confirmation": True,         # Require user approval before execution
    "create_report": True,            # Generate a summary .txt file
    "case_sensitive": False,          # Treat .JPG and .jpg as the same
    "verbose_mode": True,             # Print real-time move status
    "auto_rename_duplicates": True,   # If names match but content differs, rename
    
    # --- ULTIMATE UPDATE FEATURES ---
    "time_capsule_sorting": True,     # Organize into Year/Month subfolders
    "smart_deduplication": True,      # Find EXACT duplicates using SHA-256 hash
    "watch_mode": False                # Active tracking: Live watch and sort directory
}
