# Agent guide — Clawd

A macOS menu-bar/desktop app (pixel desktop pet + Apple Reminders board + work/rest timer + bedtime guard). Plain Swift, no Swift package and no Xcode project: `Scripts/build.sh` compiles `Sources/Clawd/*.swift` with `swiftc`.

## Layout

- `Sources/Clawd/` — app source (AppKit, WebKit, EventKit, ServiceManagement). `TimerController`, `BedtimeController`, `RemindersManager`, `WindowCoordinator` hold the main behavior; `L10n.swift` holds English/Chinese strings.
- `Resources/Animations/` — pixel scenes as HTML/JS, bundled into the app. `clawd-preview-index.html` previews them in a browser.
- `Resources/Info.plist`, `Resources/AppIcon.*` — metadata and icon (`Scripts/generate_icon.swift` regenerates the icon).
- `Scripts/build.sh` — builds and ad-hoc signs `build/Clawd.app`. `Scripts/package-dmg.sh VERSION` — builds `output/Clawd-VERSION.dmg`.
- `.github/workflows/ci.yml` builds on every push/PR; `release.yml` publishes a DMG for `v*` tags.
- `Docs/`, `Docs/assets/` — README images and the HTML cards used to make them.

## Build and run

```sh
./Scripts/build.sh          # needs macOS 13+ and Xcode Command Line Tools; ~40 s
open build/Clawd.app
```

There is no automated test suite; verify by building and, for UI changes, running the app. Say clearly what you did not run (for example the full-screen rest/bedtime overlay).

## Rules

- License is the custom non-commercial Clawd license (`LICENSE`). Keep it; do not relabel the project as MIT or open source.
- Keep both languages in `L10n.swift` in sync when adding a user-visible string.
- Do not add Accessibility permission or any control of other apps. Permissions are limited to Reminders and the overlay windows.
- `build/` and `output/` are ignored; do not commit build products or DMGs.
- Bedtime guard writes `com.apple.screensaver` lock settings and sleeps the display. Do not trigger it on the user's machine while testing without asking.
- No personal data in the repo (names, local paths, reminder contents).
