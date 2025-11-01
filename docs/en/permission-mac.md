# Fix permission denied errors
[Deutsch](../de/permission-mac.md) | English

This guide explains how to install **uv** on macOS when the terminal shows messages such as `Permission denied` or `unable to create receipt directory at ~/.config/uv`.

---

## 1️⃣ Open Terminal

Quick path:
- Open Spotlight with `⌘ + Space`
- Type "Terminal"
- Press **Return**

---

## 2️⃣ Start the uv installer

**Goal:** Download and run the installer.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If no error appears, the installation is complete (still do step 6 "Check").
If you see **"Permission denied"**, continue with step 3.

---

## 3️⃣ Most common cause: missing permissions on `.zshrc` or `.config`

The following steps repair permissions for **`~/.zshrc`** and **`~/.config`**.

### 3a) Make `.zshrc` owned by the current account again

**Goal:** Set the owner of `~/.zshrc` to the current account so the installer can modify it.

```bash
chown $(whoami) ~/.zshrc 2>/dev/null || true
```

> If the file does not exist, that is fine-you will create an empty file in the next command.

**Goal:** Ensure `~/.zshrc` exists (create an empty file if necessary).

```bash
touch ~/.zshrc
```

**Goal:** Give the file read and write permissions for the user.

```bash
chmod u+rw ~/.zshrc
```

---

### 3b) Ensure `.config` is accessible and not locked

**Goal:** Check the status of the configuration folder (owner, flags, permissions).

```bash
ls -ldO ~/.config ~/.config/uv 2>/dev/null
```

> The "Owner" column should list your username. The "Flags" column must **not** contain `uchg` (that flag means write protection).

**Goal:** Remove a potential macOS write-protection flag (`uchg`).

```bash
chflags -R nouchg ~/.config 2>/dev/null || true
```

**Goal:** Make sure you can read, write, and traverse the directory. Without execute permission (`x`) on the folder, `mkdir` fails.

```bash
chmod u+rwx ~/.config
```

**Goal:** Create the target directory for uv (if it does not exist yet).

```bash
mkdir -p ~/.config/uv
```

---

## 4️⃣ Run the installer again

**Goal:** Repeat the installation with repaired permissions.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## 5️⃣ Reload the shell configuration

**Goal:** Activate the changes immediately.

```bash
source ~/.zshrc
```

---

## 6️⃣ Verify the installation

**Goal:** Confirm that uv is available.

```bash
uv --version
```

> If a version number appears, the installation succeeded. 🎉

---

# 🆘 If it **still** fails

Sometimes every step above is performed correctly and `mkdir` still fails.
That usually points to one of the following special cases. Each cause comes with a single check or repair command.

---

### A) The owner is not the current account (cannot be changed without admin rights)

**Goal:** Check the owner of `~/.config` explicitly.

```bash
stat -f "%Su %N" ~/.config
```

- If the command does **not** return your username, the folder belongs to another account.
- Without admin privileges you cannot change that. On managed machines (e.g. campus devices) this is common.

**Workaround without changing ownership:** point uv to a **user-owned configuration directory**.

**Goal:** Define a custom config path (persistent).

```bash
echo 'export XDG_CONFIG_HOME="$HOME/.config-user"' >> ~/.zshrc
```

**Goal:** Create the target directory.

```bash
mkdir -p ~/.config-user/uv
```

**Goal:** Reload the shell and rerun the installer.

```bash
source ~/.zshrc
```

**Goal:** Install uv with the new config path.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

> This stores all configuration files in `~/.config-user` and leaves the locked `~/.config` untouched.

---

### B) `.zshrc` is a directory or link instead of a file

**Goal:** Determine the type of the resource.

```bash
file ~/.zshrc
```

- If the output says "directory" or "symbolic link", the installer cannot edit it.
- In that case fix the structure (e.g. rename the directory).

**Goal:** (Only if `.zshrc` was a directory) back it up and create an empty file.

```bash
mv ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d-%H%M%S)
```

**Goal:** Create an empty configuration file.

```bash
touch ~/.zshrc
```

**Goal:** Set the permissions.

```bash
chmod u+rw ~/.zshrc
```

Afterwards go back to **step 4** (run the installer).

---

### C) Missing execute permission on the home directory itself

Without `x` on the home directory you cannot enter subdirectories.

**Goal:** Check the permissions of the home directory.

```bash
ls -ld ~
```

- In the first column, the **user** permissions should include an **x** (e.g. `drwx------`).
- If the **x** is missing, you cannot traverse the directory.

**Goal:** Add execute permission for the user (only if the **x** is missing).

```bash
chmod u+x ~
```

Then return to **step 4** (run the installer).

---

## 💡 Background information

- **uv** installs into `~/.local/bin` and stores internal files in `~/.config/uv`.
- `mkdir` fails when:
  - the **parent directory** is not owned by the current account,
  - a macOS **write-protection flag (`uchg`)** is set,
  - the directory is missing the **execute permission (`x`)**,
  - the expected **file** (`~/.zshrc`) is actually a **directory or link**.
- The section "🆘 If it still fails" covers these special cases - no administrator required.

---

## 🧭 Summary

| Step | Task |
|---|---|
| 1 | Open Terminal |
| 2 | Install uv |
| 3 | Repair permissions on `.zshrc` and `.config` |
| 4 | Run the installer again |
| 5 | Reload the shell |
| 6 | Check the version |
| 🆘 | If problems persist: check A/B/C and run the respective single commands |

After these steps the installation should succeed even in the shown edge cases.
