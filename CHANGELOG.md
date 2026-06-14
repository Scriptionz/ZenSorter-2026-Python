# Version History - ZenSorter 📂

All notable changes to the ZenSorter file management system will be documented in this file.

## [1.2.0] - 2026-06-15
### Added
- **🧬 Smart SHA-256 Deduplication:** Introduced cryptographic hashing (`hashlib`) to detect completely identical files (exact twins) regardless of their names, isolating them into a dedicated `Duplicates_Vault`.
- **📦 Time Capsule Hierarchy:** Added an optional feature to automatically build a subfolder tree organized by `Year/Month` based on the file's last modified timestamp.
- **📡 Zen Watcher Mode:** Implemented a live, real-time background tracking system (`watch_mode`) that continuously monitors the target directory and moves incoming files on the fly.
- **🎨 Beautiful CLI Dashboard:** Designed an adaptive terminal user interface utilizing ANSI color coding to display status panels, progress states, and execution summaries elegantly.

### Improved
- **Modern Architecture Migration:** Fully deprecated the old `os` / `os.path` methods and migrated the entire codebase to modern `pathlib.Path` structures for true cross-platform stability.
- **Collision Counter Logic:** Enhanced the unique path generator by combining both a `timestamp` and an incremental `counter` to completely eliminate the risk of naming collisions during rapid executions.
- **Safe Directory Allocation:** Optimized folder creation logic; the engine now safely checks and generates target folders only when a file transfer is actively verified.

## [1.1.0] - 2026-01-23
### Added
- **Dynamic Categorization:** Added new rules for sorting 'Programming' files (.py, .js, .cpp).
- **Empty Folder Cleanup:** Added a feature to automatically remove empty subdirectories after sorting.
- **Log System:** Created a simple session log to show how many files were moved.

### Improved
- **Collision Handling:** Improved file naming logic; if a file with the same name exists in the target folder, it now appends a timestamp.
- **Performance:** Optimized the directory scanning algorithm for faster processing of folders with 1000+ files.

### Fixed
- Fixed an issue where system-hidden files (like .DS_Store or desktop.ini) would cause sorting errors.
- Resolved a bug that prevented sorting files with no extensions.

## [1.0.0] - 2026-01-23
### Added
- **Core Automation Engine:** Initial release of the automated file organizer.
- **Default Categories:** Implemented basic sorting for Images, Documents, and Media.
- **OS Integration:** Added support for Windows and Linux directory structures.
