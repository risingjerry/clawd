# Clawd — macOS 像素桌面伙伴（番茄钟 + 待办 + 睡眠守护）

[English](README.md) · **中文**

作者：risingjerry

**一个住在 Mac 桌面上的像素小宠物：到点强制你站起来，到点强制你睡觉。**

Clawd 是一个给 macOS 用的像素桌面伙伴。它把 Todo List、番茄钟、桌面宠物合在一起，专门解决一个人长期坐在电脑前工作、忘记起身、容易熬夜的问题。

![演示：桌面上的 Clawd 像素宠物、30 分钟工作计时、12 种像素工作场景、强制休息全屏接管、Apple 提醒事项待办板和睡眠守护](Docs/demo.gif)

## 下载安装

直接下载最新 DMG：

[下载 Clawd-0.1.0.dmg](https://github.com/risingjerry/clawd/releases/download/v0.1.0/Clawd-0.1.0.dmg)

安装方式：

1. 下载 `Clawd-0.1.0.dmg`
2. 打开 DMG
3. 把 `Clawd.app` 拖到 `Applications`
4. 第一次打开时，如果 macOS 提示来自未知开发者，请右键点击 `Clawd.app`，选择 `Open`

备用下载页面：

[GitHub Releases](https://github.com/risingjerry/clawd/releases/tag/v0.1.0)

## 它是什么

Clawd 是一个三合一工具：

- Todo List：读取 Apple Reminders，显示你当前未完成的事项
- 番茄钟：工作 30 分钟后，强制你休息 3 分钟
- 桌面宠物：一个透明背景的像素 Clawd，会在屏幕边缘陪你工作

它不是一个单纯的效率工具。它更像是一个健康守门员：你可以专心工作，但时间到了，它会强制打断你，让你站起来活动一下。

## 为什么做它

很多人每天都是一个人坐在电脑前工作。时间久了很容易连续坐好几个小时，身体会变差，也更容易长脂肪。很多时候不是不知道要休息，而是工作一忙就会忘。

所以 Clawd 的设计很直接：

- 工作时，它尽量小，不挡你的界面
- 到点后，它会霸占屏幕，让你不能继续操作
- 休息结束后，自动回到正常工作状态
- 到了睡觉时间，它会强制进入睡眠守护，提醒你不要继续熬夜

默认节奏是工作 30 分钟，休息 3 分钟。睡眠守护默认从晚上 10:30 到早上 5:00，你也可以自己改时间。

## 功能展示

![Clawd：像素桌面伙伴、待办板、番茄钟和睡眠守护](Docs/assets/clawd-hero.png)

<table>
  <tr>
    <td width="33%"><img src="Docs/assets/features/work.png" alt="工作模式"><br><b>工作模式</b><br>手动点击 Start Work 后才开始计时。</td>
    <td width="33%"><img src="Docs/assets/features/reminders.png" alt="Todo List"><br><b>Todo List</b><br>读取 Apple Reminders，默认显示 5 条未完成事项。</td>
    <td width="33%"><img src="Docs/assets/features/break.png" alt="强制休息"><br><b>强制休息</b><br>时间到后覆盖屏幕，提醒你站起来活动。</td>
  </tr>
  <tr>
    <td width="33%"><img src="Docs/assets/features/bedtime.png" alt="睡眠守护"><br><b>睡眠守护</b><br>到睡觉时间后进入霸屏状态，并在结束后锁屏息屏。</td>
    <td width="33%"><img src="Docs/assets/features/settings.png" alt="设置面板"><br><b>设置面板</b><br>工作时间、休息时间、睡眠时间、语言和提醒板都可以配置。</td>
    <td width="33%"><img src="Docs/assets/features/warning.png" alt="睡前提醒"><br><b>睡前提醒</b><br>睡觉前 1 小时、30 分钟、5 分钟会提醒你收尾。</td>
  </tr>
</table>

## 12 种工作状态动画

工作时 Clawd 会以透明背景显示在屏幕边缘，随机切换不同动画。下面这些是当前内置的 12 种状态。

<table>
  <tr>
    <td width="25%"><img src="Docs/assets/states/coffee.png" alt="喝咖啡"><br><b>喝咖啡</b></td>
    <td width="25%"><img src="Docs/assets/states/keyboard.png" alt="敲键盘"><br><b>敲键盘</b></td>
    <td width="25%"><img src="Docs/assets/states/reading.png" alt="看书"><br><b>看书</b></td>
    <td width="25%"><img src="Docs/assets/states/stretch.png" alt="拉伸"><br><b>拉伸</b></td>
  </tr>
  <tr>
    <td width="25%"><img src="Docs/assets/states/meditation.png" alt="冥想"><br><b>冥想</b></td>
    <td width="25%"><img src="Docs/assets/states/tidy-desk.png" alt="收拾桌面"><br><b>收拾桌面</b></td>
    <td width="25%"><img src="Docs/assets/states/cheer-sign.png" alt="举牌加油"><br><b>举牌加油</b></td>
    <td width="25%"><img src="Docs/assets/states/fitness.png" alt="健身"><br><b>健身</b></td>
  </tr>
  <tr>
    <td width="25%"><img src="Docs/assets/states/nap.png" alt="午休"><br><b>午休</b></td>
    <td width="25%"><img src="Docs/assets/states/running.png" alt="跑步"><br><b>跑步</b></td>
    <td width="25%"><img src="Docs/assets/states/swimming.png" alt="游泳"><br><b>游泳</b></td>
    <td width="25%"><img src="Docs/assets/states/daydream.png" alt="发呆"><br><b>发呆</b></td>
  </tr>
</table>

## 休息逻辑

工作模式需要你手动开始。这样电脑开着但你还没开始工作时，Clawd 不会自动进入倒计时。

工作开始后：

- 默认倒计时 30 分钟
- 工作期间动画会随机切换
- 最后 10 秒切到闹钟准备动画
- 时间到后进入强制休息
- 休息期间倒计时放大显示，Clawd 和闹钟在屏幕中间动起来
- 休息结束后自动回到工作流程

这个设计的重点是强制站起来。普通通知太容易被忽略，所以 Clawd 会覆盖屏幕，让你不能继续点来点去。

## 睡眠守护

睡眠守护是为了减少熬夜。

默认规则：

- 开始时间：22:30
- 结束时间：05:00
- 睡前 1 小时提醒一次
- 睡前 30 分钟提醒一次
- 睡前 5 分钟提醒一次
- 到点后霸屏 15 分钟
- 霸屏结束后自动锁屏并息屏
- 每个睡眠窗口只有一次紧急退出机会

睡眠时间可以自己改。比如你不是 10:30 睡，也可以改成自己的作息。

## Todo List

Clawd 会读取 Apple Reminders 里的未完成事项，并用像素告示牌展示出来。

当前逻辑：

- 默认显示 5 条未完成事项
- 支持实时刷新
- 支持打开和收起
- 收起后变成小图标
- 展开时尽量避开 Clawd 动画区域

它不是完整的任务管理软件，而是让你在桌面上持续看到“还有什么没做”。

## 多屏幕支持

Clawd 会跟随当前活跃屏幕显示。多显示器工作时，时间、动画和提醒板会尽量移动到你正在使用的屏幕上。

休息和睡眠霸屏时，会覆盖所有连接的屏幕。

## 动画预览

所有 HTML 动画都在这里：

[Resources/Animations](Resources/Animations)

本地克隆后，可以直接打开这个预览页：

[clawd-preview-index.html](Resources/Animations/clawd-preview-index.html)

## 权限说明

Clawd 会用到这些 macOS 能力：

- Reminders：读取 Apple Reminders 里的未完成事项
- 屏幕覆盖窗口：用于休息和睡眠霸屏
- Display sleep：睡眠守护结束后调用系统息屏
- Lock-after-sleep：启动时会尝试把锁屏策略配置为息屏后立即需要密码

Clawd 不需要 Accessibility 权限，也不需要控制你的其他 App。

## 本地构建

要求：

- macOS 13+
- Xcode Command Line Tools

构建 App：

```sh
./Scripts/build.sh
```

生成 DMG：

```sh
./Scripts/package-dmg.sh 0.1.0
```

输出位置：

```text
output/Clawd-0.1.0.dmg
```

## 发布

推送 `v*` 版本 tag 后，[release.yml](.github/workflows/release.yml) 会自动打包并发布 DMG；每次推送和 PR 还会跑 [ci.yml](.github/workflows/ci.yml) 确认能编译。

## 项目结构

```text
Sources/Clawd/          macOS App 源码
Resources/Animations/   像素 HTML 动画
Resources/Info.plist    App 元数据和权限说明
Scripts/build.sh        构建 Clawd.app
Scripts/package-dmg.sh  生成 DMG
Docs/assets/            README 展示图片
```

## 授权协议

Clawd 使用**自定义的非商业授权协议**，属于「源码可见（source-available）」，**不是 MIT，也不是 OSI 意义上的开源**。

你可以个人使用、学习、修改、二次开发、Fork 和分享，但不允许商用。任何商业使用都必须先获得作者 risingjerry 的明确同意。

详细条款见 [LICENSE](LICENSE)。

## 常见问题

### Clawd 是什么？怎么让 Mac 强制我休息？
Clawd 是一个 macOS 像素桌面宠物，同时是番茄钟：默认工作 30 分钟后，它会覆盖屏幕强制你休息 3 分钟，之后自动回到工作状态。

### 怎么让 Mac 到点提醒我睡觉？
打开睡眠守护（默认 22:30–05:00，可改）。睡前 1 小时、30 分钟、5 分钟各提醒一次，到点后霸屏 15 分钟，然后自动锁屏并息屏。

### 打开时提示「来自未知开发者」，打不开？
Clawd 目前没有 Apple 开发者签名公证。第一次请右键 `Clawd.app`，选择「打开」。

### Clawd 需要哪些权限？
只需要 Reminders（读取未完成事项）。休息和睡眠霸屏使用覆盖窗口。不需要 Accessibility 权限，也不控制其他 App。

### 它能读我的 Apple 提醒事项吗？会上传吗？
会读取未完成事项并显示在像素告示牌上。代码里没有任何联网上传逻辑，数据只在本机显示。

### 它支持多显示器吗？
支持。平时跟随当前活跃屏幕，休息和睡眠霸屏时覆盖所有屏幕。

## 卸载

1. 退出 Clawd，把 `/Applications/Clawd.app` 拖进废纸篓。
2. 可选：清除设置 `defaults delete com.risingjerry.clawd`。
3. 如果开启过「开机启动」，先在 Clawd 设置里关掉，或在「系统设置 → 通用 → 登录项」里移除。
4. 注意：睡眠守护启动时会把「息屏后立即需要密码」写入系统设置，卸载不会自动还原。需要的话到「系统设置 → 锁定屏幕」里自行调整。

---

如果 Clawd 帮你站起来动了动，点个 star 能让更多人找到它。

[![Star History Chart](https://api.star-history.com/svg?repos=risingjerry/clawd&type=Date)](https://star-history.com/#risingjerry/clawd&Date)
