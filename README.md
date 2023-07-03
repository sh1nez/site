<h1 align='center'> quick start </h1>

<p> <img src="https://i.ibb.co/Yk2z6hj/vsevlod.jpg" alt="vsevlod" border="0" height="45" width="70"> </p>
<p> fork this repo in github and clone it or use it </p>

<h3> Clone repository, use clone </h3>

```pip
if u use ssh: 
    git clone git@github.com:skraler/module4.git
else: 
    git clone https://github.com/skraler/module4.git
```
<p> After this u need change push-repo </p>

```pip
    git remote set-url new_ssh_or_https_link
```

<p> Also u can check push and fetch repo with </p>

```pip
git remote -v
```

<h3> Ok, now u have your local repo, start use it </h3> <br>

* python3 -m venv venv <br>
    + create virtual environment, maybe u need
    + ```pip3 python3 install virtualenv ``` <br>
    <p></p>
* activate venv
    * ```source venv/bin/activate``` for linux enjoyers <br>
    * ```pip3 venv/Scripts/activate``` для виндусятников
    <p></p>
* install libs
    + pip install -r requirements.txt <br>

<p> Enjoy coding </p>
