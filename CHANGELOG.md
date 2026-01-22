# Version History - ZenSorter 📂

All notable changes to the ZenSorter file management system will be documented in this file.

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

## [1.0.0] - 2026-01-13
### Added
- **Core Automation Engine:** Initial release of the automated file organizer.
- **Default Categories:** Implemented basic sorting for Images, Documents, and Media.
- **OS Integration:** Added support for Windows and Linux directory structures.
