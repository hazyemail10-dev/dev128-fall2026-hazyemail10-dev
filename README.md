# DEV 128 – Object-Oriented Programming with Python

Fall 2026

Welcome to the DEV 128 course code repository.

This repository contains:

- Example programs used in course materials
- Starter files for lab activities
- Starter files for programming projects

## Repository Folders

### examples
Small example programs demonstrating weekly Python concepts.

### labs
Starter files for lab assignments.

### projects
Starter files and resources for larger programming projects.

## Using Codespaces

Most course programs can be run directly in GitHub Codespaces.

Click:

Code → Codespaces → Create codespace on main

Python and VS Code are already configured for you.

## Important: Tkinter GUI Programs

Tkinter requires a graphical desktop environment.

Beginning with our GUI assignments, you may still use GitHub to
store and edit your files, but Tkinter programs may need to be
downloaded and run locally using Python and VS Code.

Web-based GUI frameworks such as Streamlit may be run through
Codespaces.

## Assignment Instructions

Always use Canvas for the complete assignment requirements,
due dates, grading criteria, and submission instructions.

Absolutely. For students with little or no GitHub experience, I’d keep the instructions **very procedural** and repeat the same workflow every week.

One important note first: when students create their own repository from your **template repository**, GitHub gives them a separate repository with the same files and folders, but its history is independent from your template. That means **future files you add to the instructor repository do not automatically appear in the student repository**. :chatgpt-content-reference{index="0"}

Here’s a Canvas-ready guide you can adapt.

---

# 🐙 Using GitHub & Codespaces in DEV 128

Throughout DEV 128, we will use **GitHub** to store our Python files and **GitHub Codespaces** as an online coding environment.

You do **not** need previous GitHub experience. We will use a small set of GitHub features repeatedly throughout the quarter.

Think of the pieces this way:

- **GitHub repository** = your project folder stored online
- **Codespace** = a browser-based version of VS Code connected to your repository
- **Commit** = a saved checkpoint of your work
- **Push** = sends that checkpoint to GitHub
- **Pull** = brings newer files from GitHub into your Codespace

---

# 🚀 Step 1: Create Your DEV 128 Repository

You only need to do this **once** at the beginning of the quarter.

Go to the DEV 128 starter repository:

**professorlaney/dev128-fall2026**

Click:

**Use this template → Create a new repository**

GitHub will make a copy of the course starter files in **your own GitHub account**. A repository made from a template starts as its own independent project. :chatgpt-content-reference{index="1"}

### Name your repository

Use something easy to recognize, such as:

```text
dev128-yourname-fall2026
```

For example:

```text
dev128-alexsmith-fall2026
```

Choose **Private** unless I tell you otherwise.

Then click:

**Create repository**

You now have your own DEV 128 repository.

---

# ⚠️ Important: Your Repository Is YOUR Copy

Your repository belongs to you.

### You should:
- Edit files in **your repository**
- Complete your labs and projects there
- Commit your work regularly
- Push your commits to GitHub

### You should NOT:
- Try to edit the instructor repository
- Submit changes back to the instructor repository
- Delete the `.devcontainer` folder
- Rename major course folders unless instructed
- Change starter files for assignments you haven't reached yet

Your repository might look like this:

```text
dev128-yourname-fall2026/

├── examples/
├── labs/
│   ├── lab01/
│   ├── lab02/
│   └── ...
├── projects/
├── .devcontainer/
├── .gitignore
└── README.md
```

---

# 💻 Step 2: Open Your Repository in Codespaces

From **your GitHub repository**:

1. Click the green **Code** button.
2. Select the **Codespaces** tab.
3. Click **Create codespace on main**.

A browser version of Visual Studio Code will open.

It may take a moment the first time while Python and the course environment are configured.

Once it opens, you should see your folders on the left side.

---

# 📂 Step 3: Open the Assignment Folder

Suppose you are working on **Lab 1**.

In the Explorer on the left:

```text
labs
  └── lab01
       └── main.py
```

Click `main.py`.

Before changing anything, **run the starting program** and make sure it works.

You can open the terminal with:

**Terminal → New Terminal**

Then run:

```bash
python labs/lab01/main.py
```

---

# 💾 Saving vs. Committing

This is an important distinction.

When you press:

**Ctrl+S / Command+S**

you are saving the file **inside your Codespace**.

That does **not necessarily mean your latest work has been saved to your GitHub repository**.

To permanently record your work in GitHub, you need to:

> **Save → Commit → Push**

A commit is like creating a checkpoint in a game.

---

# ✅ After You Finish an Assignment

Let's say you completed:

```text
labs/lab01/main.py
```

You tested it and everything works.

Now save it to GitHub.

## Method 1: Using the Codespaces buttons

This is the method I recommend for beginners.

### 1. Open Source Control

Click the **Source Control** icon on the left side of Codespaces.

It looks like a branching path.

You will see the files you changed listed under:

**Changes**

For example:

```text
M  labs/lab01/main.py
```

`M` means **Modified**.

---

### 2. Stage your changes

Click the **+** next to the file.

Or click the **+** next to **Changes** if you want to include all changed files.

The file moves to:

**Staged Changes**

---

### 3. Write a commit message

At the top of the Source Control panel, enter a short description.

For Lab 1:

```text
Complete Lab 1
```

Good commit messages might be:

```text
Complete Lab 1
Add recursion solutions for Lab 2
Finish inheritance lab
Complete SQLite project
Fix input validation in Project 1
```

Avoid messages like:

```text
stuff
changes
asdf
final final final
```

😄 Future-you deserves better clues.

---

### 4. Commit and Push

Click the dropdown next to **Commit** and choose:

**Commit & Push**

GitHub Codespaces supports committing and pushing directly from the Source Control panel. :chatgpt-content-reference{index="2"}

Your work is now stored in your GitHub repository.

---

# 🔎 Step 4: Verify Your Work Is Actually on GitHub

This is one of the most important habits to build.

After pushing:

1. Open your GitHub repository in another browser tab.
2. Go to:

```text
labs → lab01 → main.py
```

3. Look at the code.

If your latest work is there, you're good.

You should also see your commit message:

```text
Complete Lab 1
```

If your latest work isn't visible on GitHub, you probably **saved the file but didn't push it**.

---

# 🧑‍💻 Example: Completing Lab 1

Imagine you modify:

```text
labs/lab01/main.py
```

Your workflow is:

### Before working

```text
Open Codespace
↓
Open labs/lab01/main.py
↓
Run starter file
```

### During the assignment

```text
Edit code
↓
Save
↓
Run
↓
Debug
↓
Save again
```

### When finished

```text
Source Control
↓
Stage main.py
↓
Commit message:
"Complete Lab 1"
↓
Commit & Push
↓
Check GitHub
```

Done. ✅

---

# 🧪 Example: An Assignment With Multiple Files

Later, your inheritance lab might contain:

```text
labs/lab03/
├── product_viewer.py
└── objects.py
```

You edit **both**.

Source Control will show something like:

```text
M  labs/lab03/product_viewer.py
M  labs/lab03/objects.py
```

Stage both files.

Use the commit message:

```text
Complete Lab 3 inheritance exercise
```

Then:

**Commit & Push**

Both files are now updated in GitHub.

---

# 🗄️ Example: SQLite Assignment

Your database project might contain:

```text
projects/project02/
├── main.py
└── users.db
```

After completing the project, Source Control might show:

```text
M  projects/project02/main.py
M  projects/project02/users.db
```

If the assignment requires you to submit the populated database, commit both.

Example commit:

```text
Complete SQLite database project
```

Then push.

---

# 🖥️ What Happens When We Reach Tkinter?

You can still use GitHub exactly the same way.

Your files might look like:

```text
labs/lab05/
├── ui.py
└── business.py
```

You can:

- Edit them in Codespaces
- Save them in Codespaces
- Commit them
- Push them to GitHub

However, **Tkinter creates desktop windows**, and Codespaces runs on a remote computer without a normal desktop display.

That means the GUI itself may need to be tested using **Python + VS Code on your own computer**.

Your GitHub workflow stays the same:

```text
GitHub repository
       ↓
Edit locally or in Codespaces
       ↓
Test locally
       ↓
Commit
       ↓
Push to GitHub
```

We'll cover that workflow when we reach the GUI unit.

---

# 🔄 Getting New Course Starter Files

Here is the biggest limitation of using a template repository.

When you created your repository from the DEV 128 template, you made an **independent copy**. New assignments that I later add to the instructor repository do **not automatically appear** in your copy. GitHub specifically treats template-generated repositories differently from forks; their histories are unrelated. :chatgpt-content-reference{index="3"}

So before starting a new assignment, you may occasionally need to bring newer starter files into your repository.

I'll tell you when this is necessary.

---

# 🛠️ One-Time Setup for Course Updates

Inside your Codespace terminal, enter:

```bash
git remote add upstream https://github.com/professorlaney/dev128-fall2026.git
```

Press Enter.

Now check your repository connections:

```bash
git remote -v
```

You should see something similar to:

```text
origin    https://github.com/YOURUSERNAME/dev128-yourname-fall2026.git
upstream  https://github.com/professorlaney/dev128-fall2026.git
```

Think of them like this:

```text
origin   = YOUR repository
upstream = PROFESSOR'S repository
```

You only need to add `upstream` **once**.

---

# ⬇️ Getting New Starter Files

Before pulling course updates, make sure your current work is committed and pushed.

Then run:

```bash
git fetch upstream
```

This checks the instructor repository for newer files.

Then:

```bash
git merge upstream/main
```

This brings the instructor updates into your Codespace.

Finally:

```bash
git push origin main
```

Now your GitHub repository also contains those updates.

---

# 🎯 Example: I Add Lab 3 After You Created Your Repository

Originally your copy contains:

```text
labs/
├── lab01/
└── lab02/
```

Later I add:

```text
labs/lab03/
```

to the instructor repository.

You run:

```bash
git fetch upstream
```

then:

```bash
git merge upstream/main
```

Now your Codespace should contain:

```text
labs/
├── lab01/
├── lab02/
└── lab03/
```

Then push your updated copy:

```bash
git push origin main
```

Now `lab03` appears in **your GitHub repository**, too.

---

# ⚠️ Why You Shouldn't Edit Future Starter Files

Suppose I later update:

```text
labs/lab04/main.py
```

but you've already edited that same file.

Git may not know which version to keep.

That can create a:

### Merge conflict 💥

Avoid this by following a simple rule:

> **Only edit the assignment you're currently working on.**

Don't start modifying future starter files just because they're visible.

---

# 🛟 Before Updating From the Instructor Repository

Always do this first:

```bash
git status
```

Ideally you should see:

```text
nothing to commit, working tree clean
```

If Git shows modified files, commit them first.

For example:

```bash
git add .
git commit -m "Complete Lab 2"
git push origin main
```

Then retrieve the course updates.

---

# ⌨️ Optional: Doing Everything With Git Commands

You do **not** have to use commands for normal assignments, but you'll see these often in professional environments.

After finishing Lab 1:

```bash
git status
```

See what changed.

Then:

```bash
git add labs/lab01/main.py
```

Stage the file.

Then:

```bash
git commit -m "Complete Lab 1"
```

Create the checkpoint.

Then:

```bash
git push origin main
```

Send it to GitHub.

The entire workflow is:

```bash
git status
git add labs/lab01/main.py
git commit -m "Complete Lab 1"
git push origin main
```

---

# ⭐ The Four Git Commands Worth Remembering

You do **not** need to memorize dozens of Git commands for this class.

These four will get you surprisingly far:

```bash
git status
```

**What did I change?**

```bash
git add .
```

**Include my changes in the next checkpoint.**

```bash
git commit -m "Complete Lab 1"
```

**Create the checkpoint.**

```bash
git push
```

**Send the checkpoint to GitHub.**

And when I tell you new starter files are available:

```bash
git fetch upstream
git merge upstream/main
```

**Bring Professor Laney's new files into your copy.**

---

# 🧠 GitHub Survival Rule

Think:

> **SAVE → TEST → COMMIT → PUSH → VERIFY**

### SAVE
Save your Python files.

### TEST
Run your program.

### COMMIT
Create a Git checkpoint.

### PUSH
Send that checkpoint to GitHub.

### VERIFY
Open GitHub and make sure the newest code is there.

---

# 🚨 Don't Panic If You Break Something

Git is actually useful here because commits are checkpoints.

If something goes sideways:

**Do not delete your entire repository.**

Instead:

1. Stop editing.
2. Save what you have.
3. Take a screenshot of the error if necessary.
4. Send me a Canvas message or ask in Discord.
5. Tell me what command or button you used right before the problem appeared.

Git mistakes are fixable.

