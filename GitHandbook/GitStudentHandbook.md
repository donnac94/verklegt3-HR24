# GitHub Handbook for a Student Project

---
# Getting Started
### Step-by-Step Guide to Create a GitHub Account and Clone a Repository

### Create a GitHub Account

1. **Go to GitHub:** Visit https://github.com.
2.	**Sign Up**:
	- Click on the Sign up button in the top-right corner.
	- Enter your email address, password, and username.
	- Complete the CAPTCHA and click Create account.
3.	**Confirm Email:**
	- GitHub will send a verification email to your address
	- Open your email inbox and click the verification link.
4.	**Complete Setup:**

	- Follow the on-screen prompts to set up your GitHub account preferences

### Install Git (If not already installed) 
Git is the tool GitHub uses for version control.

1. **Download git:**
	- Visit https://git-scm.com/downloads.
2. **Install Git:** 
	- Follow the installation instructions for your operating system (Windows, macOS, or Linux).
3. **Verify installation:** 
	- Open your terminal or command prompt and type: 

	``` bash
	git --version
	````
	- (If Git is installed, it will display the installed version.)

### Install Github Desktop 
GitHub Desktop provides a user-friendly interface for Git and GitHub, we recommend you use Github Desktop if you are a beginner to GitHub 

1.	**Download GitHub Desktop:**
	- Visit https://desktop.github.com/.
2. **Install** 
	- Follow the installation instructions for your operating system.
3. **Sign In:** 
	- Launch GitHub Desktop and log in with your GitHub account credentials.

### Clone a Repository Using GitHub Desktop
1. Find the Repository:
	- Go to the repository’s page on GitHub.
	- Click the green **Code** button and select Open with GitHub Desktop.

2. **Open GitHub Desktop:**
	- A dialog box will appear. Select the local path where you want to store the repository.

3. **Clone:**
	- Click Clone. GitHub Desktop will download the repository to your selected location.

# Introduction to GitHub Flow

The default branch for the project is `main`.

The workflow we follow is called **GitHub Flow** and is documented [here by GitHub](https://docs.github.com/en/get-started/quickstart/github-flow). This guide provides a comprehensive overview of the flow. It's recommended to read this for an in-depth understanding.

All changes to the code should be applied via **Pull Requests** based on the default branch. Below is the step-by-step workflow:

1. Create a branch. (*Remember to Git Pull from main before making any new code changes to avoid conflicts beforehand*) 

2. Make changes to the code.
3. Open a Pull Request (PR).
4. Request a review.
5. Wait for approval.
6. Address review comments.
7. Merge your Pull Request (once approved).
8. Delete the branch.

Pull Requests should contain **ONE** conceptual change to the code, such as a feature, bugfix, or refactor. To enforce this, follow the conventions introduced below.

---

## Branch Naming

Branches should reflect the type of change being made. Use branch prefixes that align with semantic commit message types (detailed below). Branch names should follow the dashed syntax.

### Example: Creating a Branch

```
git checkout -b feat/change-customer-email
```

**Example of valid branch names**

```
feat/change-customer-email

fix/only-accept-valid-emails

refactor/all-button-components-to-typescript
```

**Example of invalid branch names**

```
changeCustomerEmail
newfeature/email-changes
fix/only
```

---
### Types of Commit Messages

Below are the commonly used types for semantic commits:
- feat: A new feature for the user.
- fix: A bug fix for the user.
- docs: Documentation-only changes.
- refactor: Refactoring code without affecting functionality.
- test: Adding or updating tests.

### Basic Git commands 
```
git pull <remote_name> <branch_name>
```
- Fetches changes from a remote repository and merges them into the current branch in one step.


```
git Status 
```
- Shows the status of changes as untracked, modified, or staged. This provides a snapshot of the current state of the working directory and staging area.

```
git add . 
``` 
Displays the commit history for the repository, showing the commits made, who made them, and their commit messages.

```
git push <remote_name> <branch_name>
```
- Uploads local branch commits to the remote repository branch. If the branch doesn’t exist on the remote, it will be created.
