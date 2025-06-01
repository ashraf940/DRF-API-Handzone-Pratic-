# DRF-API-Handzone-Pratic-
1. Repository Banana

git init
Ye command current folder ko Git repository banaata hai.

2. File Add Karna (Staging Area mein)
git add <filename>
git add .
git add . se saari changes staging area mein chali jaati hain.

3. Commit Karna
git commit -m "Commit message"
Ye command staged changes ko commit karta hai.

4. Branch Banani
git branch <branch-name>
Ye command nayi branch banata hai.

5. Branch Pe Switch Karna
git checkout <branch-name>
Ye command specified branch pe switch karta hai.

6. Nayi Branch Banake Switch Karna
git checkout -b <branch-name>
Ye command nayi branch banata hai aur uspe switch karta hai.

7. Changes Ko Remote Repository Pe Push Karna
git push origin <branch-name>
Ye command local commits ko remote repository pe bhejta hai.

8. Remote Repository Se Changes Ko Pull Karna
git pull origin <branch-name>
Ye command remote repository se latest changes ko apni local branch mein merge karta hai.

9. Branch Merge Karna
git merge <branch-name>
Ye command specified branch ke changes ko current branch mein merge karta hai.

10. Commit History Dikhana
git log
Ye command commit history dikhata hai.

 GitHub Workflow: Pull Request Kaise Banayein
1. Fork Karna (Agar Aap External Repository Mein Contribute Karna Chahte Hain)
GitHub pe jaake repository ko fork karein.

2. Apni Local Machine Pe Clone Karna
git clone https://github.com/ashraf940/repository-name.git
cd repository-name
Ye command repository ko apni local machine pe clone karta hai.

3. Nayi Branch Banake Uspe Kaam Karna
git checkout -b <branch-name>
Ye command nayi branch banata hai aur uspe switch karta hai.

4. Changes Karna Aur Commit Karna
git add .
git commit -m "Description of changes"
Ye commands changes ko stage aur commit karti hain.

5. Apni Branch Ko Remote Repository Pe Push Karna
git push origin <branch-name>
Ye command apni branch ko remote repository pe push karta hai.

6. GitHub Pe Pull Request Banana
GitHub pe apni repository pe jaake "Compare & pull request" button pe click karein.

Title aur description likhein, phir "Create pull request" pe click karein.

7. Pull Request Merge Karna
Jab pull request review ho jaye, "Merge pull request" button pe click karein.

Merge hone ke baad, "Delete branch" button pe click karke branch delete kar sakte hain.

