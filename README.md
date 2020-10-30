# python_learn
## 第一：网站设置
	创建一个repository(项目)
	复制项目地址
## 第二：本地|服务器操作
	1. clone 项目地址
		git clone https://github.com/luyuan410117/python_learn.git
			Cloning into 'python_learn'...
			remote: Enumerating objects: 5, done.
			remote: Counting objects: 100% (5/5), done.
			remote: Compressing objects: 100% (4/4), done.
			remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
			Unpacking objects: 100% (5/5), done.

	2. cd 项目下载路径
		cd python_learn
	3. 配置本地用户名和邮箱
		git config --global user.email "luyuan410117@163.com"
		git config --global user.name "LuYuan"
	4. 将需要上传的文件拷贝到项目下载路径，并进行归档，比如：
		mkdir -p coroutine_learn/script/
		cp ../../coroutine/* ./coroutine_learn
		mv ./coroutine_learn/*py ./coroutine_learn/script/
	5. 将改动添加到暂存区
		git add coroutine_learn # git add .
	6. 提交本次更新内容
		git commit -m "协程学习" -m "yield learn"
			[main dba0251] 协程学习
			 5 files changed, 145 insertions(+)
			 create mode 100644 coroutine_learn/script/cor_consumer_produce.py
			 create mode 100755 coroutine_learn/script/cor_grep.py
			 create mode 100755 coroutine_learn/script/tailf.py
			 create mode 100755 coroutine_learn/script/tailf_grep.py
			 create mode 100644 coroutine_learn/testfile
	7. 查看工作空间状态
		git status
			# On branch main
			# Your branch is ahead of 'origin/main' by 1 commit.
			#   (use "git push" to publish your local commits)
			#
			nothing to commit, working directory clean
	8. 推送到远程仓库
		git push origin master
		报错：error: src refspec master does not match any.
		      error: failed to push some refs to 'https://github.com/luyuan410117/python_learn.git'
		ssh-keygen -t rsa -C "987418490@qq.com" # 一直回车
		# 将公钥id_rsa.pub 中的值复制到远程仓库的ssh中 ssh-rsa ...... 去掉最后的邮箱地址和其前面的空格
		报错：同上，说明不是这个引起的，将其删除
		git push origin HEAD
		# https://stackoverflow.com/questions/4181861/message-src-refspec-master-does-not-match-any-when-pushing-commits-in-git
		Counting objects: 10, done.
		Delta compression using up to 120 threads.
		Compressing objects: 100% (9/9), done.
		Writing objects: 100% (9/9), 2.51 KiB | 0 bytes/s, done.
		Total 9 (delta 2), reused 0 (delta 0)
		remote: Resolving deltas: 100% (2/2), completed with 1 local object.
		To https://github.com/luyuan410117/python_learn.git
		   b551865..dba0251  HEAD -> main
## 第三：修改文件
	1. 编辑文件，并保存，比如修改README.md
	2. git add README.md
	3. git status
		# On branch main
		# Changes to be committed:
		#   (use "git reset HEAD <file>..." to unstage)
		#
		#	modified:   README.md
		#

		# 如果add后，又修改了文件，则git status为

		# On branch main
		# Changes to be committed:
		#   (use "git reset HEAD <file>..." to unstage)
		#
		#	modified:   README.md
		#
		# Changes not staged for commit:
		#   (use "git add <file>..." to update what will be committed)
		#   (use "git checkout -- <file>..." to discard changes in working directory)
		#
		#	modified:   README.md

	4. git commit -m "修改README.md"
	5. git status
	6. git push origin HEAD
