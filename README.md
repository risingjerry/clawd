# Clawd — a pixel desktop pet that makes you take breaks and go to bed (macOS)

**English** · [中文](README.zh-CN.md)

**A pixel pet for your Mac desktop that combines a Pomodoro-style work/rest timer, an Apple Reminders board, and a bedtime guard: when it is time to stand up, or go to sleep, it takes over the screen.**

![Clawd: pixel desktop companion, reminders board, work timer and bedtime guard](Docs/assets/clawd-hero.png)

By risingjerry. Source-available under a non-commercial license (see [License](#license)).

## Install

[Download Clawd-0.1.0.dmg](https://github.com/risingjerry/clawd/releases/download/v0.1.0/Clawd-0.1.0.dmg), open it, and drag `Clawd.app` to `Applications`. All releases: [GitHub Releases](https://github.com/risingjerry/clawd/releases).

The first time, macOS may say the app is from an unidentified developer. Right-click `Clawd.app` and choose **Open**.

Or build it yourself (macOS 13+ and Xcode Command Line Tools):

```sh
git clone https://github.com/risingjerry/clawd.git
cd clawd
./Scripts/build.sh        # produces build/Clawd.app
./Scripts/package-dmg.sh 0.1.0   # optional: output/Clawd-0.1.0.dmg
```

## Highlights

- **Todo board** — reads your open Apple Reminders and shows them on a pixel sign (5 by default, live refresh, collapsible to a small icon).
- **Forced rest** — work 30 minutes, then Clawd covers the screen for 3 minutes. Notifications are too easy to ignore; this is not.
- **Bedtime guard** — warnings 1 hour, 30 minutes and 5 minutes before bedtime, then a 15-minute screen takeover, then lock and display sleep.
- **12 pixel work scenes** — coffee, keyboard, reading, stretching, meditation, tidying the desk, cheering, fitness, napping, running, swimming, daydreaming.
- **Multi-display aware** — follows your active screen; rest and bedtime overlays cover every screen.
- **English and Chinese UI.**

## Screenshots

<table>
  <tr>
    <td width="33%"><img src="Docs/assets/features/work.png" alt="Work mode"><br><b>Work mode</b><br>The timer starts only when you click Start Work.</td>
    <td width="33%"><img src="Docs/assets/features/reminders.png" alt="Todo list"><br><b>Todo list</b><br>Open Apple Reminders, 5 shown by default.</td>
    <td width="33%"><img src="Docs/assets/features/break.png" alt="Forced rest"><br><b>Forced rest</b><br>Covers the screen when time is up.</td>
  </tr>
  <tr>
    <td width="33%"><img src="Docs/assets/features/bedtime.png" alt="Bedtime guard"><br><b>Bedtime guard</b><br>Takes over the screen at bedtime, then locks and sleeps the display.</td>
    <td width="33%"><img src="Docs/assets/features/settings.png" alt="Settings"><br><b>Settings</b><br>Work, rest and bedtime times, language, reminders board.</td>
    <td width="33%"><img src="Docs/assets/features/warning.png" alt="Bedtime warning"><br><b>Bedtime warning</b><br>1 hour, 30 minutes and 5 minutes before.</td>
  </tr>
</table>

<table>
  <tr>
    <td width="25%"><img src="Docs/assets/states/coffee.png" alt="Coffee"></td>
    <td width="25%"><img src="Docs/assets/states/keyboard.png" alt="Keyboard"></td>
    <td width="25%"><img src="Docs/assets/states/reading.png" alt="Reading"></td>
    <td width="25%"><img src="Docs/assets/states/stretch.png" alt="Stretching"></td>
  </tr>
  <tr>
    <td width="25%"><img src="Docs/assets/states/meditation.png" alt="Meditation"></td>
    <td width="25%"><img src="Docs/assets/states/tidy-desk.png" alt="Tidying the desk"></td>
    <td width="25%"><img src="Docs/assets/states/cheer-sign.png" alt="Cheering"></td>
    <td width="25%"><img src="Docs/assets/states/fitness.png" alt="Fitness"></td>
  </tr>
  <tr>
    <td width="25%"><img src="Docs/assets/states/nap.png" alt="Napping"></td>
    <td width="25%"><img src="Docs/assets/states/running.png" alt="Running"></td>
    <td width="25%"><img src="Docs/assets/states/swimming.png" alt="Swimming"></td>
    <td width="25%"><img src="Docs/assets/states/daydream.png" alt="Daydreaming"></td>
  </tr>
</table>

## How it works

- **Work** starts only when you press Start Work, so Clawd does not count down while you are away. Default: 30 minutes, with scenes switching at random; in the last 10 seconds an alarm animation plays.
- **Rest** then covers the screen for 3 minutes with a large countdown, and returns to work mode afterwards.
- **Bedtime** defaults to 22:30 to 05:00 (editable). Warnings come at 1 hour, 30 minutes and 5 minutes before. At bedtime the screen is covered for 15 minutes, then locked and the display put to sleep. There is one emergency exit per bedtime window.
- The pet and the overlays are HTML/JS pixel scenes in `Resources/Animations/` rendered in a transparent web view. Open `Resources/Animations/clawd-preview-index.html` in a browser to preview them.

## Permissions, limits and requirements

- macOS 13 or newer. Building from source uses your Mac's own architecture.
- **Reminders** access, to show open reminders. No Accessibility permission, and it does not control other apps.
- The bedtime guard uses full-screen cover windows and puts the display to sleep. On start it also sets macOS to require a password immediately after the display sleeps (`com.apple.screensaver askForPassword`).
- The app is ad-hoc signed, not notarized.
- No automated test suite; CI checks that the app builds.

## FAQ

### How do I force myself to take breaks on a Mac?
Use Clawd: press Start Work, and after 30 minutes (configurable) it covers the screen for 3 minutes until you have stood up.

### How do I stop staying up late on my Mac?
Turn on the bedtime guard. It warns you three times, then covers the screen for 15 minutes and locks and sleeps the display. Set your own bedtime in Settings.

### macOS says Clawd is from an unidentified developer.
Clawd is not notarized by Apple. Right-click `Clawd.app` and choose **Open** the first time.

### What permissions does Clawd need?
Reminders only, to read your open items. It needs no Accessibility permission.

### Does it send my reminders anywhere?
No. The source contains no network code; reminders are only displayed on your own screen.

### Can I change the 30/3 minute rhythm?
Yes. Work, rest and bedtime times are in the Settings panel.

## Uninstall

1. Quit Clawd and drag `/Applications/Clawd.app` to the Trash.
2. Optional: remove its settings with `defaults delete com.risingjerry.clawd`.
3. If you enabled launch at login, turn it off in Clawd settings first, or remove it in **System Settings → General → Login Items**.
4. Note: the bedtime guard writes "require password right after display sleep" into your macOS settings; uninstalling does not revert it. Change it in **System Settings → Lock Screen** if you want.

## License

Clawd uses a **custom non-commercial license**. It is source-available, **not MIT and not OSI open source**. You may use, study, modify, fork and share it for personal and other non-commercial purposes; any commercial use needs the author's prior explicit permission. See [LICENSE](LICENSE).

---

If Clawd got you out of your chair, a star helps others find it.

[![Star History Chart](https://api.star-history.com/svg?repos=risingjerry/clawd&type=Date)](https://star-history.com/#risingjerry/clawd&Date)
